def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Max slice sum
    """
    n = len(arr)
    if n == 0:
        return 0

    max_profit = 0
    prev_price = best_price = arr[n - 1]

    for i in range(n - 2, -1, -1):
        curr_price = arr[i]

        if prev_price > best_price:
            best_price = prev_price

        one_step_profit = prev_price - curr_price
        best_step_profit = best_price - curr_price

        if one_step_profit > best_step_profit:
            best_step_profit = one_step_profit

        if best_step_profit > max_profit:
            max_profit = best_step_profit
        prev_price = curr_price
    return max_profit


assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
assert solution([1, 2, 9, 6, 3, 5]) == 8
