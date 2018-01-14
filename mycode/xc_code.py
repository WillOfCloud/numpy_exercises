# -*- coding:utf-8 -*-
_author_ = 'liujihao'

import calendar
import time


def calculating_sum_date(begin, end):
    try:
        time_start = time.strptime(begin, "%Y-%m-%d")
        time_end = time.strptime(end, "%Y-%m-%d")
    except:
        raise Exception("时间格式有误，请使用YYYY-MM-DD")

    if time_start > time_end:
        raise Exception("结束日期不能小于开始日期")

    year_start = time_start.tm_year
    year_end = time_end.tm_year

    month_first = time_start.tm_mon
    month_last = time_end.tm_mon

    day_start = time_start.tm_mday
    day_end = time_end.tm_mday

    sum = 0
    for year in range(year_start, year_end + 1):
        month_left = 1
        month_right = 12
        if year == year_start:
            month_left = month_first
        if year == year_end:
            month_right = month_last

        for month in range(month_left, month_right + 1):
            # print(year, month)
            sum += calendar.monthrange(year, month)[1]

    day_out_1 = day_start - 1
    day_out_2 = calendar.monthrange(year_end, month_last)[1] - day_end
    sum = sum - day_out_1 - day_out_2
    # print(day_out_1, day_out_2)
    return sum


count = calculating_sum_date("2017-01-03", "2017-01-28")
print(count)
