from collections import deque


def solution(s):
    """
    Args:
        s (str): String of brackets

    Returns:
        int: 1 if s is nested 0 otherwise
    """

    n = len(s)
    if n == 0:
        return 1

    if n % 2 != 0:
        return 0

    reverse_of = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    opening_brackets = ('(', '[', '{')

    brackets = deque()
    for i in s:
        if i in opening_brackets:
            brackets.append(i)
        elif len(brackets) == 0 or reverse_of[brackets.pop()] != i:
            return 0

    return 1 if len(brackets) == 0 else 0


assert solution('{[()]}') == 1
assert solution('{[(]]}') == 0
assert solution('{[[()()]]}') == 1
assert solution('([)(])') == 0
assert solution('){') == 0
assert solution(')(') == 0
assert solution('))') == 0
assert solution('{{{{') == 0
