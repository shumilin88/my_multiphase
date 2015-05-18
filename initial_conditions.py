#!/usr/bin/python

import numpy as np

def IC_test_interpolation_u(mesh):
    value=np.array([[ 1,  3,  7,  8,  2,  4,  0],
               [ 9,  6,  0,  0,  2,  3,  8],
               [ 4,  4,  8, 10, 10,  2,  2],
               [ 0,  9,  6, 10, 10,  8,  0],
               [ 9,  3,  1,  3,  7,  0,  1],
               [ 3,  3,  1,  0, 10,  4,  9],
               [ 5,  0,  4, 10,  9,  6,  9],
               [ 2,  9,  7,  1,  2,  0,  7],
               [ 8,  7,  3, 10,  8,  4,  0]])
    return value 

def IC_test_interpolation_v(mesh):
    value=np.array([[ 3,  2,  8,  3,  0,  0,  3],
           [ 6,  5,  0,  3,  4,  1,  1],
           [ 2, 10,  0,  8,  4, 10,  8],
           [ 7,  5,  9,  7,  1,  2,  7],
           [ 7,  4,  3,  9,  5,  4, 10],
           [ 9,  3,  1,  2,  8,  6,  1],
           [ 2,  1,  1,  3, 10,  1,  8],
           [10, 10,  5,  5,  3,  1,  5],
           [ 6,  3,  9,  9, 10,  4,  9]])
    return value