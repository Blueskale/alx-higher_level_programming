#!/usr/bin/python3
""""
 Function returns the pascal triangle
"""


def pascal_triangle(n):
    """
    Args:
        n: number of lines
    Returns:
        matrix: matrix with the pascal triangle
    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        p1 = -1
        p2 = 0
        for j in range(len(prev) + 1):
            if p1 == -1 or p2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p1] + prev[p2]]
            p1 += 1
            p2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
