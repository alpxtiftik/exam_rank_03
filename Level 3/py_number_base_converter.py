def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not (2 <= from_base <= 36 and 2 <= to_base <= 36):
        return "ERROR"
    if not isinstance(number, str):
        return "ERROR"
    number = number.strip().upper()
    negative = number.startswith(-)
    if negative:
        number = number[1:]
    if number == "":
        return "ERROR"
    value = 0
    for c in number:
        d = digits.find(c)
        if d == -1 or d >= from_base:
            return "ERROR"
        value = value * from_base + d
    if value == 0:
        return "0"
    out = ""
    while value > 0:
        out