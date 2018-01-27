def solution(arr):
    """
    Args:
        arr (list): List of cars moving east(0) and west(1)

    Returns:
        int: number of passing cars
    """
    moving_west_cars_count = 0
    passing_cars_count = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 1:
            moving_west_cars_count += 1
        else:
            passing_cars_count += moving_west_cars_count
            if passing_cars_count > 1000000000:
                return -1
    return passing_cars_count


assert solution([0, 1, 0, 1, 1]) == 5
