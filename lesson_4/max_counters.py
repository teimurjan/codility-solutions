def solution(n, arr):
    """
    Args:
        n (int): Length of the counters array
        arr (list): List of integers

    Returns:
        list: List the values of the counters
    """
    counters = [0] * n
    local_max_counter = 0
    global_max_counter = 0
    for i, arr_i in enumerate(arr):
        if 1 <= arr_i <= n:
            if global_max_counter > counters[arr_i - 1]:
                counters[arr_i - 1] = global_max_counter

            counters[arr_i - 1] += 1
            if counters[arr_i - 1] > local_max_counter:
                local_max_counter = counters[arr_i - 1]
        else:
            global_max_counter = local_max_counter

    for i, counter in enumerate(counters):
        if counter < global_max_counter:
            counters[i] = global_max_counter

    return counters


assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
