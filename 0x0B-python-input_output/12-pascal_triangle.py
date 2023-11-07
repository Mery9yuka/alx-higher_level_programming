#!/usr/bin/python3
""" Pascal triangle Solving ..."""


def pascal_triangle(n):
    """pascal"""
    if n <= 0:
        return []

    pas_tri = [[1]]
    for y in range(n - 1):
        cal = [0] + pas_tri[-1] + [0]
        angle = []
        for u in range(len(pas_tri[-1]) + 1):
            angle.append(cal[u] + cal[u + 1])
        pas_tri.append(angle)
    return pas_tri
