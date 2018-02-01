from collections import deque

from utils import check_time


@check_time
def solution(arr):
    """
    Args:
        arr (list): List where index is disc's center and value is radius.

    Returns:
    Returns:
        int: Number of (unordered) pairs of intersecting discs
    """
    events = deque()

    for center, radius in enumerate(arr):
        events.append((center - radius, 1))
        events.append((center + radius, -1))

    events = list(events)
    events.sort(key=lambda x: (x[0], -x[1]))

    active_circles = 0
    intersections = 0
    for event in events:
        if event[1] > 0:
            intersections += active_circles
            if intersections > 10000000:
                return -1
        active_circles += event[1]

    return intersections


assert solution([1, 5, 2, 1, 4, 0]) == 11
assert solution([1, 1, 1]) == 3
assert solution([1, 0, 1, 0, 1]) == 6
