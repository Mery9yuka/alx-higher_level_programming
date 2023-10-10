#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    y = tuple_a + (0, 0)
    u = tuple_b + (0, 0)
    return (y[0] + u[0], y[1] + u[1])
