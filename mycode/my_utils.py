# -*- coding: utf-8 -*- 
__author__ = 'Liujuhao'

import sys

def printp(x):
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    print "line - " + str(f.f_lineno) + " : \n" + str(x)

# def printp(x):
#     line = sys._getframe().f_lineno
#     print "line - " + str(line) + " : \n" + str(x)

