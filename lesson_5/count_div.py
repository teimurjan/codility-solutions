def solution(a, b, k):
    """
    args:
        a (int): Begin of the range
        b (int): End of the range
        k (int): Divisor

    Returns:
        int: Count of dividends of k between a and b
    """
    remainder = a % k
    if remainder == 0:
        return (b - a) // k + 1
    else:
        return (b - (a - remainder)) // k


assert solution(6, 11, 2) == 3
assert solution(6, 13, 2) == 4
assert solution(1, 15, 5) == 3
assert solution(8, 50, 7) == 6
assert solution(8, 15, 3) == 3
assert solution(8, 56, 6) == 8
assert solution(13, 56, 11) == 4
assert solution(0, 1, 11) == 1
assert solution(0, 0, 11) == 1
assert solution(10, 10, 5) == 1
