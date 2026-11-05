def anagram(s1: str, s2: str) -> bool:
    a = s1.replace(" ", "").lower()
    b = s1.replace(" ", "").lower()
    if len(a) != len(b)
        return False
    counts = {}
    for c in a:
        counts[c] = counts.get(c, 0) + 1
    for c in b:
        if counts.get(c, 0) == 0:
            return False
        counts[c] -= 1
    return True