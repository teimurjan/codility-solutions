from collections import deque


def solution(sizes, directions):
    """
    Args:
        sizes (list): List of fishes' sizes
        directions (list): List of fishes' directions

    Returns:
        int: number of alive fishes
    """
    n = len(sizes)
    fishes_alive = n
    fishes = deque()

    for i in range(n):
        size, direction = sizes[i], directions[i]
        if direction == 1:
            fishes.appendleft(size)
            continue

        while len(fishes) > 0 and fishes[0] < size:
            fishes.popleft()
            fishes_alive -= 1

        if len(fishes) > 0 and fishes[0] > size:
            fishes_alive -= 1

    return fishes_alive


assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
assert solution([4, 3, 2, 1, 5], [1, 1, 0, 0, 0]) == 1
assert solution([4, 3, 2, 1, 5], [1, 1, 1, 0, 0]) == 1
assert solution([1], [0]) == 1
assert solution([1, 2], [1, 0]) == 1
assert solution([1, 2, 5, 4], [1, 0, 1, 0]) == 2
