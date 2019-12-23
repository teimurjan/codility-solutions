def solution(A, B, C):
    A.sort()
    B.sort()
    C.sort()

    n = len(A)

    i, j, k = 0, 0, 0
    a_count, b_count = 0, 0
    result = 0

    while i < n or j < n or k < n:
        a = A[i] if i < n else A[n - 1]
        b = B[j] if j < n else B[n - 1]
        c = C[k] if k < n else C[n - 1]
        if a < b < c:
            a_count += 1
            result += b_count * a_count
            i += 1
        elif b >= c and a < b:
            b_count += 1
            k += 1
        elif a >= b:
            j += 1

    return result


assert solution([29, 50], [61, 37], [37, 70]) == 3
assert solution([29, 29], [37, 37], [70, 70]) == 8
