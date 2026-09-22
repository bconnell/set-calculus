from .engine import run
from .model import Authority, AuthorityRule, Intent, Requirement, State, Transform


def main() -> None:
    intent = Intent(
        intent_id="INT-DEMO",
        version=1,
        objective="Produce a reviewed and published artifact.",
        acceptance_criteria=(
            Requirement("AC-1", "drafted", True, "Artifact is drafted."),
            Requirement("AC-2", "reviewed", True, "Artifact is reviewed."),
            Requirement("AC-3", "published", True, "Artifact is published."),
        ),
        invariants=(
            Requirement("INV-1", "source_preserved", True, "Source remains preserved."),
        ),
        provenance=("example",),
    )

    authority = Authority(
        rules=(
            AuthorityRule("agent", "draft", "artifact"),
            AuthorityRule("agent", "review", "artifact"),
            AuthorityRule("agent", "publish", "artifact"),
        )
    )

    state = State(
        facts={
            "drafted": False,
            "reviewed": False,
            "published": False,
            "source_preserved": True,
        }
    )

    transforms = (
        Transform(
            "T-DRAFT",
            "agent",
            "draft",
            "artifact",
            effects={"drafted": True},
        ),
        Transform(
            "T-REVIEW",
            "agent",
            "review",
            "artifact",
            preconditions=(Requirement("P-1", "drafted", True),),
            effects={"reviewed": True},
        ),
        Transform(
            "T-PUBLISH",
            "agent",
            "publish",
            "artifact",
            preconditions=(Requirement("P-2", "reviewed", True),),
            effects={"published": True},
        ),
    )

    result = run(intent, authority, state, transforms)

    print(f"Resolution: {result.resolution.value}")
    print(f"Final state version: {result.state.version}")
    print("Trace:")
    for line in result.trace:
        print(f"  {line}")


if __name__ == "__main__":
    main()
