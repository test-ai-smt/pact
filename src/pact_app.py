"""PACT dummy module (demo for team branch -> PR -> owner merge workflow)."""

GREETINGS = {
    "en": "Hello from PACT, {name}!",
    "ar": "مرحباً من PACT، {name}!",
}


def greet(name: str, lang: str = "en") -> str:
    if lang not in GREETINGS:
        raise ValueError(f"Unsupported language: {lang!r}")
    return GREETINGS[lang].format(name=name)


if __name__ == "__main__":
    print(greet("team-1"))
    print(greet("team-1", "ar"))
