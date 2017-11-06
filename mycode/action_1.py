# -*- coding: utf-8 -*-
__author__ = 'Liujuhao'

# TODO Array_creation_routines

import numpy as np
import sys
import my_utils as mut

print sys._getframe().f_lineno

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

m = np.arange(1,4,1)
mut.printp(m)