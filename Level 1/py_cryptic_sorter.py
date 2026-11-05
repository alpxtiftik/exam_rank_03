def cryptic_sorter(strings: list[str]) -> list[str]:
    def key(s):
        sesli = 0
        for c in s:
            if c in 'aeiouAEIOU':
                sesli += 1
        return (len(s), s.lower(), sesli)

    result = list(strings)
    for i in range(1, len(result)):
        cur = result(i)
        j = i - 1
        k = key(cur)
        while j >= 0 and key(result[j]) > k:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = cur
    return result