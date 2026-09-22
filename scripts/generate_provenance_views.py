#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

INTERPRETATION = {"DIRECT", "GENERALIZED", "INFERRED"}
MAPPING_ROLE = {"PRIMARY", "SUPPORT", "DEPENDENCY", "COMPLEMENT", "STATUS"}
CALIBRATION = {
    "NOT_APPLICABLE", "FORMAL_CLOSED", "FORMAL_DERIVED",
    "EMPIRICAL_CALIBRATION_PENDING", "BRIDGE_REQUIRED",
    "CONDITIONAL_THEOREM", "PROVENANCE_REQUIRED", "DOMAIN_SCOPED", "UNKNOWN"
}

def die(msg):
    raise SystemExit(f"provenance validation failed: {msg}")

def load_graph(path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if data.get("format") != "set-calculus-provenance/v1":
        die("unsupported format")
    return data

def unique_ids(records, kind):
    ids = [x.get("id") for x in records]
    if None in ids:
        die(f"{kind} record missing id")
    dup = [k for k,v in Counter(ids).items() if v > 1]
    if dup:
        die(f"duplicate {kind} ids: {', '.join(dup)}")
    return set(ids)

def validate(g):
    source_ids = unique_ids(g.get("sources", []), "source")
    passage_ids = unique_ids(g.get("passages", []), "passage")
    object_ids = unique_ids(g.get("objects", []), "object")
    mapping_ids = unique_ids(g.get("mappings", []), "mapping")
    unique_ids(g.get("audit_findings", []), "audit")

    for p in g.get("passages", []):
        if p.get("source_id") not in source_ids:
            die(f"passage {p['id']} references missing source {p.get('source_id')}")
        if p.get("calibration_status") not in CALIBRATION:
            die(f"passage {p['id']} has invalid calibration_status")

    edge_keys = set()
    for m in g.get("mappings", []):
        if m.get("passage_id") not in passage_ids:
            die(f"mapping {m['id']} references missing passage {m.get('passage_id')}")
        if m.get("object_id") not in object_ids:
            die(f"mapping {m['id']} references missing object {m.get('object_id')}")
        if m.get("interpretation_level") not in INTERPRETATION:
            die(f"mapping {m['id']} has invalid interpretation_level")
        if m.get("mapping_role") not in MAPPING_ROLE:
            die(f"mapping {m['id']} has invalid mapping_role")
        if m.get("calibration_status") not in CALIBRATION:
            die(f"mapping {m['id']} has invalid calibration_status")
        edge = (m["passage_id"], m["object_id"], m["interpretation_level"], m["mapping_role"])
        if edge in edge_keys:
            die(f"duplicate provenance edge at mapping {m['id']}")
        edge_keys.add(edge)
        for dep in m.get("derived_from_mapping_ids", []):
            if dep not in mapping_ids:
                die(f"mapping {m['id']} references missing derived mapping {dep}")

    for o in g.get("objects", []):
        if o.get("calibration_status") not in CALIBRATION:
            die(f"object {o['id']} has invalid calibration_status")

    valid_refs = {
        "source_ids": source_ids,
        "passage_ids": passage_ids,
        "object_ids": object_ids,
        "mapping_ids": mapping_ids,
    }
    for a in g.get("audit_findings", []):
        for field, pool in valid_refs.items():
            for ref in a.get(field, []):
                if ref not in pool:
                    die(f"audit {a['id']} references missing {field[:-1]} {ref}")

def esc(s):
    if s is None:
        return ""
    return str(s).replace("|", "\\|").replace("\n", " ")

def location(p):
    loc = p.get("location") or {}
    parts = []
    if loc.get("section"):
        parts.append(loc["section"])
    ps, pe = loc.get("page_start"), loc.get("page_end")
    if ps:
        parts.append(f"p. {ps}" if not pe or pe == ps else f"pp. {ps}-{pe}")
    ls, le = loc.get("line_start"), loc.get("line_end")
    if ls:
        parts.append(f"lines {ls}-{le or ls}")
    if not parts and loc.get("heading"):
        parts.append(loc["heading"])
    return ", ".join(parts) or "location not yet captured"

def header(title):
    return (
        f"# {title}\n\n"
        "> GENERATED FILE. Do not edit by hand.\n"
        "> Source of truth: `docs/provenance/SOURCE_CATALOG.json`.\n"
        "> Regenerate with: `python scripts/generate_provenance_views.py`.\n\n"
    )

def render_source_ledger(g):
    passages_by_source = defaultdict(list)
    for p in g["passages"]:
        passages_by_source[p["source_id"]].append(p)
    out = [header("Set Calculus Source Ledger")]
    out.append("This ledger covers Set Calculus and registered specializations, including IDGM and CRC.\n\n")
    for s in sorted(g["sources"], key=lambda x: (x["kind"], x["name"], x["id"])):
        out.append(f"## {s['name']}\n\n")
        out.append(f"- **Source ID:** `{s['id']}`\n")
        out.append(f"- **Kind:** `{s['kind']}`\n")
        out.append(f"- **Locator:** `{s['locator']}`\n")
        out.append(f"- **Capture:** `{s.get('capture_status','PENDING')}`\n")
        if s.get("version"): out.append(f"- **Version:** {s['version']}\n")
        if s.get("author"): out.append(f"- **Author:** {s['author']}\n")
        if s.get("date"): out.append(f"- **Date:** {s['date']}\n")
        if s.get("content_sha"): out.append(f"- **Content SHA:** `{s['content_sha']}`\n")
        out.append("\n")
        plist = sorted(passages_by_source.get(s["id"], []), key=lambda x: x["id"])
        if plist:
            out.append("| Passage | Location | Capture | Calibration | Summary |\n")
            out.append("|---|---|---|---|---|\n")
            for p in plist:
                out.append(f"| `{p['id']}` | {esc(location(p))} | `{p['capture']}` | `{p['calibration_status']}` | {esc(p.get('summary'))} |\n")
        else:
            out.append("_No passage-level records registered yet._\n")
        out.append("\n")
    return "".join(out)

def render_matrix(g):
    pmap = {p["id"]: p for p in g["passages"]}
    smap = {s["id"]: s for s in g["sources"]}
    maps_by_object = defaultdict(list)
    for m in g["mappings"]:
        maps_by_object[m["object_id"]].append(m)
    out = [header("Set Calculus Provenance Matrix")]
    out.append("| Calculus object | Kind | Source passage | Source | Location | Interpretation | Role | Calibration | Confidence |\n")
    out.append("|---|---|---|---|---|---|---|---|---:|\n")
    for o in sorted(g["objects"], key=lambda x: (x["calculus"], x["kind"], x["name"], x["id"])):
        mappings = sorted(maps_by_object.get(o["id"], []), key=lambda x: x["id"])
        if not mappings:
            out.append(f"| **{esc(o['name'])}** (`{o['calculus']}`) | `{o['kind']}` | **UNMAPPED** |  |  |  |  | `{o['calibration_status']}` |  |\n")
            continue
        for m in mappings:
            p = pmap[m["passage_id"]]
            s = smap[p["source_id"]]
            out.append(
                f"| **{esc(o['name'])}** (`{o['calculus']}`) | `{o['kind']}` | `{p['id']}` | {esc(s['name'])} | {esc(location(p))} | "
                f"`{m['interpretation_level']}` | `{m['mapping_role']}` | `{m['calibration_status']}` | {m.get('confidence','')} |\n"
            )
    return "".join(out)

def render_reverse(g):
    omap = {o["id"]: o for o in g["objects"]}
    smap = {s["id"]: s for s in g["sources"]}
    maps_by_passage = defaultdict(list)
    for m in g["mappings"]:
        maps_by_passage[m["passage_id"]].append(m)
    out = [header("Set Calculus Reverse Source Index")]
    for p in sorted(g["passages"], key=lambda x: (smap[x["source_id"]]["name"], x["id"])):
        s = smap[p["source_id"]]
        out.append(f"## {p['label']}\n\n")
        out.append(f"- **Passage ID:** `{p['id']}`\n")
        out.append(f"- **Source:** {s['name']} (`{s['id']}`)\n")
        out.append(f"- **Location:** {location(p)}\n")
        out.append(f"- **Calibration:** `{p['calibration_status']}`\n")
        if p.get("summary"): out.append(f"- **Source summary:** {p['summary']}\n")
        out.append("\n")
        mappings = sorted(maps_by_passage.get(p["id"], []), key=lambda x: x["id"])
        if not mappings:
            out.append("**CRC/Set Calculus mappings:** `UNMAPPED`\n\n")
        else:
            out.append("| Calculus object | Calculus | Interpretation | Role | Calibration | Mapping ID |\n")
            out.append("|---|---|---|---|---|---|\n")
            for m in mappings:
                o = omap[m["object_id"]]
                out.append(f"| {esc(o['name'])} | `{o['calculus']}` | `{m['interpretation_level']}` | `{m['mapping_role']}` | `{m['calibration_status']}` | `{m['id']}` |\n")
            out.append("\n")
        if p.get("unmapped_remainder"):
            out.append("**Unmapped remainder:** yes\n\n")
    return "".join(out)

def overlap(a,b):
    la, lb = a.get("location") or {}, b.get("location") or {}
    if a["source_id"] != b["source_id"]:
        return False
    a1,a2,b1,b2 = la.get("line_start"),la.get("line_end"),lb.get("line_start"),lb.get("line_end")
    if all(x is not None for x in [a1,a2,b1,b2]):
        return max(a1,b1) <= min(a2,b2)
    return False

def render_audit(g):
    passage_maps = defaultdict(list)
    object_maps = defaultdict(list)
    for m in g["mappings"]:
        passage_maps[m["passage_id"]].append(m)
        object_maps[m["object_id"]].append(m)
    unmapped_passages = [p for p in g["passages"] if not passage_maps[p["id"]]]
    unmapped_objects = [o for o in g["objects"] if not object_maps[o["id"]]]
    dup_edges = []
    seen = {}
    for m in g["mappings"]:
        k=(m["passage_id"],m["object_id"],m["interpretation_level"],m["mapping_role"])
        if k in seen:
            dup_edges.append((seen[k],m["id"]))
        else:
            seen[k]=m["id"]
    overlaps=[]
    passages=g["passages"]
    for i in range(len(passages)):
        for j in range(i+1,len(passages)):
            if overlap(passages[i],passages[j]):
                overlaps.append((passages[i],passages[j]))

    out=[header("Set Calculus Provenance Coverage Audit")]
    out.append("## Computed coverage\n\n")
    out.append(f"- Sources: **{len(g['sources'])}**\n")
    out.append(f"- Passages: **{len(g['passages'])}**\n")
    out.append(f"- Calculus objects: **{len(g['objects'])}**\n")
    out.append(f"- Mappings: **{len(g['mappings'])}**\n")
    out.append(f"- Passages with no mapping: **{len(unmapped_passages)}**\n")
    out.append(f"- Objects with no mapping: **{len(unmapped_objects)}**\n")
    out.append(f"- Duplicate exact mapping edges: **{len(dup_edges)}**\n")
    out.append(f"- Overlapping captured line windows: **{len(overlaps)}**\n\n")
    out.append("## Source passages with no calculus mapping\n\n")
    if unmapped_passages:
        for p in sorted(unmapped_passages,key=lambda x:x["id"]):
            out.append(f"- `{p['id']}`: {p['label']}\n")
    else:
        out.append("None.\n")
    out.append("\n## Calculus objects with no source mapping\n\n")
    if unmapped_objects:
        for o in sorted(unmapped_objects,key=lambda x:x["id"]):
            out.append(f"- `{o['id']}`: {o['name']} (`{o['calculus']}` / `{o['kind']}`)\n")
    else:
        out.append("None.\n")
    out.append("\n## Duplicate mappings\n\n")
    if dup_edges:
        for a,b in dup_edges:
            out.append(f"- `{a}` duplicates `{b}`\n")
    else:
        out.append("None.\n")
    out.append("\n## Overlapping passage windows\n\n")
    if overlaps:
        for a,b in overlaps:
            out.append(f"- `{a['id']}` overlaps `{b['id']}`\n")
    else:
        out.append("None detected from captured line ranges.\n")
    out.append("\n## Interpretation-level consistency\n\n")
    out.append("All mappings use controlled enum values validated before rendering:\n\n")
    out.append("```text\nDIRECT\nGENERALIZED\nINFERRED\n```\n\n")
    out.append("Mapping role is separately controlled as `PRIMARY | SUPPORT | DEPENDENCY | COMPLEMENT | STATUS`.\n")
    out.append("\n## Registered audit findings\n\n")
    if g["audit_findings"]:
        out.append("| Finding | Class | Severity | Status | Summary | Recommended action |\n")
        out.append("|---|---|---|---|---|---|\n")
        for a in sorted(g["audit_findings"],key=lambda x:x["id"]):
            out.append(f"| `{a['id']}` | `{a['audit_class']}` | `{a['severity']}` | `{a['status']}` | {esc(a['summary'])} | {esc(a.get('recommended_action'))} |\n")
    else:
        out.append("None.\n")
    return "".join(out)

def main():
    ap=argparse.ArgumentParser(description="Validate Set Calculus provenance graph and regenerate markdown views.")
    ap.add_argument("--catalog",default="docs/provenance/SOURCE_CATALOG.json")
    ap.add_argument("--out",default="docs/provenance/generated")
    args=ap.parse_args()
    g=load_graph(Path(args.catalog))
    validate(g)
    outdir=Path(args.out)
    outdir.mkdir(parents=True,exist_ok=True)
    views={
        "SOURCE_LEDGER.md":render_source_ledger(g),
        "PROVENANCE_MATRIX.md":render_matrix(g),
        "REVERSE_SOURCE_INDEX.md":render_reverse(g),
        "COVERAGE_AUDIT.md":render_audit(g),
    }
    for name,content in views.items():
        (outdir/name).write_text(content,encoding="utf-8",newline="\n")
    print(f"validated {len(g['sources'])} sources, {len(g['passages'])} passages, {len(g['objects'])} objects, {len(g['mappings'])} mappings")
    for name in views:
        print(outdir/name)

if __name__ == "__main__":
    main()
