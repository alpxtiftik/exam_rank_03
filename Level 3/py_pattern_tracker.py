def pattern_tracker(text: str) -> int:
    i = 0
    j = 1
    result = 0
    while j <= len(text) - 1:
        if text[i].isdigit() and text[j].isdigit() and int(text[j]) == int(text[i]) + 1:
                result += 1
        i += 1
        j += 1
    return result