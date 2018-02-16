from collections import deque


def find_leaders(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        deque: Equi leaders for every slice
    """
    stack = deque()
    occurrences_in_arr_of = {}
    leaders = deque()
    for i, arr_i in enumerate(arr):
        if occurrences_in_arr_of.get(arr_i) is not None:
            occurrences_in_arr_of[arr_i] += 1
        else:
            occurrences_in_arr_of[arr_i] = 1

        if len(stack) == 0:
            stack.appendleft(arr_i)
        elif stack[0] != arr_i:
            stack.popleft()
        else:
            stack.appendleft(arr_i)

        if len(stack) > 0 and occurrences_in_arr_of[stack[0]] > (i + 1) // 2:
            leaders.append(stack[0])
        else:
            leaders.append(None)

    return leaders


def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: number of equi leaders in arr
    """
    n = len(arr)

    leaders = find_leaders(arr)
    leaders_reverse = find_leaders(arr[::-1])

    equi_leaders = 0
    for i in range(n - 1):
        leader_1 = leaders[i]
        leader_2 = leaders_reverse[n - 2 - i]
        if leader_1 is not None and leader_2 is not None and leader_1 == leader_2:
            equi_leaders += 1

    return equi_leaders


assert solution([4, 3, 4, 4, 4, 2]) == 2
assert solution([1]) == 0
assert solution([1, 1]) == 1
assert solution([4, 4, 2, 5, 3, 4, 4, 4]) == 3
assert solution([-4, -4, 2, 5, 3, -4, -4, -4]) == 3
assert solution([-1, -1, -2, -1, -1, -1, -1, -5, -99]) == 4
