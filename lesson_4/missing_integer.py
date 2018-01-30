def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Smallest positive integer not occurred in arr
    """
    arr_positives = set()
    arr_min_positive = None
    for i in arr:
        if i > 0:
            arr_positives.add(i)
            if arr_min_positive is None or i < arr_min_positive:
                arr_min_positive = i

    if arr_min_positive is None:
        return 1
    else:
        i = 1
        while i < 1000001:
            if i not in arr_positives:
                return i
            i += 1


assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([100, 200, 300]) == 1
assert solution([-1, -2]) == 1
