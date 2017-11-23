# -*- coding: utf-8 -*-
__author__ = 'Liujuhao'

# TODO Array_creation_routines

import numpy as np
import my_utils as mut

mut.printp(np.empty([2, 2], int))

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
mut.printp(np.empty_like(x))

mut.printp(np.eye(4, 5, 0, np.int32))

mut.printp(np.identity(3))  # 一定是方阵

mut.printp(np.ones([3, 2], np.float64))

mut.printp(np.arange(1, 20, 4))  # 等差

mut.printp(x)
mut.printp(np.ones_like(x))

x = np.zeros([2, 3], np.int32)
mut.printp(x)

x = np.full([3, 4], 6, np.int32)
mut.printp(x)
y = np.ones_like(x) * 5
mut.printp(y)

m = np.arange(1, 4, 1)
mut.printp(m)

x = [1, 2]
y = np.asarray(x)
mut.printp(type(y))

x = np.array([[1, 2], [3, 4]])
y = np.asmatrix(x)
mut.printp(type(y))

x = [3, 4]
y = np.asfarray(x)
y = np.asarray(x, float)

x = np.array([30])  # can only convert an array of size 1 to a Python scalar
y = np.asscalar(x)
mut.printp(type(y))

x = np.array([1, 2, 3])
y = np.copy(x)
mut.printp(id(x))
mut.printp(id(y))
print x, y

x = np.linspace(3., 10, 20)
mut.printp(x)

x = np.logspace(3., 10, 20, endpoint=False)
y = np.logspace(3., 10, 20)
mut.printp(x)
mut.printp(y)
