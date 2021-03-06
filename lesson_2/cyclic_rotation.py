def solution(arr, k):
    """
    Args:
        arr (list): List of integers
        k (int): Times to rotate the list n

    Returns:
        list: List rotated k times
    """
    length = len(arr)
    if length == 0:
        return arr

    k_cut = k % length
    if k_cut == length or k_cut == 0:
        return arr
    else:
        pivot = length - k_cut
        return arr[pivot:] + arr[: pivot]


assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([0, 0, 0], 1) == [0, 0, 0]
assert solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]
assert solution([5, -1000], 1) == [-1000, 5]
assert solution([5, -1000, 7], 1) == [7, 5, -1000]
assert solution([], 1) == []
