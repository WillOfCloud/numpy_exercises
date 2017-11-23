# -*- coding: utf-8 -*- 
__author__ = 'Liujuhao'


def binary_search(lst, key, start, end):
    if not isinstance(lst, list):
        return False

    if len(lst) == 0:
        return False

    if len(lst) == 1:
        return True if key == lst[0] else False

    center_index = end / 2  # 向下取舍

    left_index = start

    right_index = end

    center_value = lst[center_index]

    if key == center_value:
        return True

    if key > center_value:
        binary_search(lst, key, center_index, right_index)

    if key < center_value:
        binary_search(lst, key, left_index, center_index)


lst = [11, 24, 33, 46, 59, 66, 72, 83, 95]

print binary_search(lst, 47, 0, len(lst))
