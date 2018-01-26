def solution(arr):
    """
    Args:
        arr (list): List of numbers

    Returns:
        int: Max gap size in the binary representation of a number
    """
    binary_string = '{:b}'.format(arr)
    if len(binary_string) < 3:
        return 0

    is_gap_open = False
    gap_size = 0
    max_gap_size = 0
    i = 0
    while i < len(binary_string):
        si = binary_string[i]

        if si == '1':
            if is_gap_open:
                if gap_size > max_gap_size:
                    max_gap_size = gap_size
                gap_size = 0
                is_gap_open = False
                continue
            else:
                is_gap_open = True
        else:
            gap_size += 1
        i += 1
    return max_gap_size
