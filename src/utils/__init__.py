# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:05:28 2023

@author: Nádia Carvalho
"""


def isDigit(x):
    """
    Check if x is a digit
    """
    try:
        float(x)
        return True
    except ValueError:
        return False


def sign_thresh(x, thresh=0):
    """
    Return the sign of x
    """
    if thresh != 0 and x <= -thresh:
        return -2
    elif x < 0:
        return -1
    elif thresh != 0 and x >= thresh:
        return 2
    elif x > 0:
        return 1
    else:
        return 0
