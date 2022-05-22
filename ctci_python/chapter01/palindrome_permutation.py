# time: O(n)
# space: O(n)
def is_palindrome_permutation(s: str) -> bool:
    seen_odd_times = set()
    for c in s:
        if c.isalpha():
            c = c.lower()
            if c in seen_odd_times:
                seen_odd_times.remove(c)
            else:
                seen_odd_times.add(c)

    return len(seen_odd_times) <= 1
