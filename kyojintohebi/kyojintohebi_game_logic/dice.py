# -*- coding: utf-8 -*-
"""
Created on 08/??/2017 JTS

@Author: Junichi Suetsugu (末次 淳一)
"""

import random

def dice(repeat=1):
    """

    Args:
        repeat(int):

    Returns:
        value(int):
    """
    value = 0
    for i in range(repeat):
        value = value + random.randint(1, 6)
    return value

if __name__ == "__main__":
    pass
