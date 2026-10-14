"""PACT dummy module (demo for team branch -> PR -> owner merge workflow)."""


def greet(name: str) -> str:
    return f"Hello from PACT, {name}!"


if __name__ == "__main__":
    print(greet("team-1"))
