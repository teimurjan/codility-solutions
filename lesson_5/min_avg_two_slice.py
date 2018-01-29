"""
Goal:
    The goal is to find the starting position of a slice of an array
    whose average is minimal in O(n) worst-case time complexity.
Solution:
    In order to find the solution matching needed time complexity
    we'll try to imagine that all slices in the array can be divided into smaller slices
    whose averages will be less then or equal to the average of the parent slice.

    Proof:
        Suppose that we have an array A consisting of n integers from a_0 to a_n.
        Then its average is A_avg = sum(A)/n.
        Let's take two sub-slices of A, say A_1 = [a_0 ... a_i] and A_2 = [a_k ... a_n]
        where 0 < i < k < N and k = i + 1.
        Assume that A_avg less than A_1 and A_2 averages. (*)
        Then we have a group of inequalities:
        |   (a_0 + ... + a_i) / i > sum(A) / n
        <
        |   (a_k + ... + a_n) / (n - i) > sum(A) / n


        |   n * (a_0 + ... + a_i) > i * sum(A)
        <
        |   n * (a_k + ... + a_n) > (n - i) * sum(A)

        Let's combine these inequalities

        n * (a_0 + ... + a_i) + n * (a_k + ... + a_n) > i * sum(A) + (n - i) * sum(A)
        n * ((a_0 + ... + a_i) + (a_k + ... + a_n)) > sum(A) * (n - i + i)
        n * sum(A) > n * sum(A) - Contradiction, then our suggestion (*) was false and at least one slice average will
        be less then or equal to the parent's one.

        But what if n is odd, then by the same way we can prove that any array's average cannot be less then
        all averages of its 3 slices.

    Conclusion:
        We should take slices of the 2 and 3 integers and calculate their average.
        The minimal average will be the global minimal average of the all slices of an array
"""


def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Starting position of a slice of arr with min average
    """

