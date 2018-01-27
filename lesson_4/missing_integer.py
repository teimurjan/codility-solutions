def find_missing_integer_up(min, ints):
    """
    Args:
        min (int): Minimum positive integer in arr
        ints (set): Set of positive integers

    Returns:
        if found:
            int: Smallest positive integer greater than min
        else:
            None
    """
    min_ = min
    ints_ = ints
    while min < 1000001:
        min_ += 1
        if min_ not in ints_:
            return min_
    return None


def find_missing_integer_down(min, ints):
    """
    Args:
        min (int): Minimum positive integer in arr
        ints (set): Set of positive integers

    Returns:
        if found:
            int: Smallest positive integer less than min
        else:
            None
    """
    ints_ = ints
    i = 1
    while i != min:
        if i not in ints_:
            return i
        i += 1
    return None


def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Smallest positive integer not occurred in arr
    """
    arr_min_positive_int = None
    positive_ints = set()
    for i in arr:
        if i > 0:
            if arr_min_positive_int is None or i < arr_min_positive_int:
                arr_min_positive_int = i
            positive_ints.add(i)

    if arr_min_positive_int is None:
        return 1

    if arr_min_positive_int == 1:
        return find_missing_integer_up(arr_min_positive_int, positive_ints)
    else:
        min_positive_int_down = find_missing_integer_down(arr_min_positive_int, positive_ints)
        if min_positive_int_down is None:
            return find_missing_integer_up(arr_min_positive_int, positive_ints)
        else:
            return min_positive_int_down


assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([100, 200, 300]) == 1
assert solution([-1, -2]) == 1
