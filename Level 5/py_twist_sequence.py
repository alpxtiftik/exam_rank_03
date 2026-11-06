def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    nk = k % len(arr)
    if nk:
        return arr[-nk:] + arr[:-nk]
    else:
        return list(arr)