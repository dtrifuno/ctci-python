# time: O(1)
# space: O(1)
def insertion(n: int, m: int, i: int, j: int) -> int:
    # clear all bits up to the jth
    clear_bottom = (n >> (j + 1)) << (j + 1)

    # put m in place
    add_m = clear_bottom | (m << i)

    # restore all of n's lowest bits up to before the ith
    result = add_m | (n & (2**i - 1))

    return result
