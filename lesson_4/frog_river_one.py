def solution(x, arr):
    """
    Args:
        x (int): Coordinate of the last leaf before opposite bank
        arr (list): A list where indexes show the time when a leaf will
                    fall and values are the coordinate where the leaf will fall down

    Returns:
        int: The earlier time when the frog will be able to go to the opposite river's bank
    """

    fallen_leaves_count = 0
    fallen_leaves = set()
    for time, coordinate in enumerate(arr):
        if coordinate <= x:
            if coordinate not in fallen_leaves:
                fallen_leaves.add(coordinate)
                fallen_leaves_count += 1
            if fallen_leaves_count == x:
                return time
    return -1


assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
assert solution(5, [1, 3, 2, 4, 5, 3, 5, 4]) == 4
assert solution(5, [1, 3, 1, 4, 2, 3, 4, 4]) == -1
assert solution(2, [2, 2, 2, 2, 2]) == -1
assert solution(3, [1, 3, 1, 3, 2, 1, 3]) == 4
