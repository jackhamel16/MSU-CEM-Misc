#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:10:28 2016

@author: jack
"""

import numpy as np

array_tuples = np.array([(1,2),(3,4)])

list_of_tups = [(1,2),(3,4)]
array2 = np.array([[5,6],[7,8]])
array_test = np.array(list_of_tups)
for i,n in np.ndenumerate(array_test):
    print(i,n)
    print(array2[i])
    print()