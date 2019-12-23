def solution(s):
    """
    Args:
        s (str): String of passwords

    Returns:
        int: length of the longest valid password
    """
    valid_chars = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    }

    digits = {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    }

    digits_count, chars_count, is_valid = 0, 0, True
    longest_pass_length = -1

    for i in s:
        if i == ' ':
            if digits_count % 2 != 0 and chars_count % 2 == 0 and is_valid:
                longest_pass_length = max(longest_pass_length, digits_count + chars_count)
            digits_count, chars_count, is_valid = 0, 0, True
        elif is_valid:
            if i in valid_chars:
                chars_count += 1
            elif i in digits:
                digits_count += 1
            else:
                is_valid = False

    if digits_count % 2 != 0 and chars_count % 2 == 0 and is_valid:
        longest_pass_length = max(longest_pass_length, digits_count + chars_count)

    return longest_pass_length


assert solution('test 5 a0A pass007 ?xy1') == 7
assert solution('test') == -1
assert solution('55') == -1
assert solution('555') == 3
assert solution('zaq123edc') == 9
