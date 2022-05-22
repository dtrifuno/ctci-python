# time: O(n)
# space: O(n)
def is_unique_v1(s: str) -> bool:
    seen = set()
    for c in s:
        if c in seen:
            return False
        seen.add(c)
    return True


# time: O(n^2)
# space: O(1)
def is_unique_v2(s: str) -> bool:
    for i, c1 in enumerate(s):
        for c2 in s[i + 1 :]:
            if c1 == c2:
                return False
    return True
