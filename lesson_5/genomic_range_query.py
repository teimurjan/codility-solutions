from collections import deque

from utils import check_time


def get_prefix_sums(s):
    impact_of = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    sums = []
    prev = [0, 0, 0, 0]
    for i, s_i in enumerate(s):
        impact = impact_of[s_i]
        prev = [prev[0] + 1 if impact == 1 else prev[0],
                prev[1] + 1 if impact == 2 else prev[1],
                prev[2] + 1 if impact == 3 else prev[2],
                prev[3] + 1 if impact == 4 else prev[3], ]
        sums.append(prev)
    return sums


@check_time
def solution(s, p, q):
    """
    Args:
        s (str): String consisting of letters A, C, G and T and representing DNA
        p (list): Query start indexes
        q (list): Query end indexes

    Returns:
        list: Minimal impact factors of the queries
    """
    m = len(p)
    prefix_sums = get_prefix_sums(s)
    min_impacts = deque()
    for i in range(m):
        end_i = q[i]
        start_i = p[i]
        for k in range(4):
            end = prefix_sums[end_i][k]
            if start_i > 0:
                end = end - prefix_sums[start_i - 1][k]
            if end > 0:
                min_impacts.append(k + 1)
                break
    return list(min_impacts)


assert solution('CAGCCTA', [2, 5, 0], [4, 5, 6]) == [2, 4, 1]
