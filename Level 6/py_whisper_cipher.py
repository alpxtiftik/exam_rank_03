def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for c in text:
        if 'a' <= c <= 'z':
            result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += c
    return result