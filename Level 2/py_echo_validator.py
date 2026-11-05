def echo_validator(text: str) -> bool:
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        return False
    return letters == letters[::-1]