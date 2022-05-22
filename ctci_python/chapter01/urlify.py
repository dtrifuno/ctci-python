# time: O(n)
# space: O(n)
def urlify(s: str, length: int) -> str:
    result = [None] * length
    i = 0
    for c in s:
        if c != " ":
            result[i] = c
            i += 1
        else:
            result[i : i + 3] = ["%", "2", "0"]
            i += 3
    return "".join(result)
