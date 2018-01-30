def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Max product of any triplet of arr
    """
    n = len(arr)
    if n == 3:
        return arr[0] * arr[1] * arr[2]

    arr.sort()
    biggest = arr[n - 1]
    bigger = arr[n - 2]
    big = arr[n - 3]

    lowest = arr[0]
    lower = arr[1]
    low = arr[2]

    p_1 = biggest * bigger * big
    p_2 = lowest * lower * biggest
    p_3 = lowest * lower * low
    return max([p_1, p_2, p_3])


assert solution([-3, 1, 2, -2, 5, 6]) == 60
assert solution([1, 2, 3]) == 6
assert solution([-4, -6, 3, 4, 5]) == 120
