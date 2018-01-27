def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: 1 if arr is a permutation else 0
    """
    n = len(arr)
    elements = set()
    for i in arr:
        if i > n:
            continue
        if i in elements:
            return 0
        else:
            elements.add(i)

    for i in range(1, n + 1):
        if i not in elements:
            return 0
    return 1


assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0
assert solution([1]) == 1
assert solution([3]) == 0
