#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:20:16 2020

@author: mattiaruefenacht
"""

import os
import numpy
from itertools import *

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-1')

file = open('input.txt')

input = file.read()

split_input = input.split("\n")

expenses = [int(string) for string in split_input]

all_expense_pairs = list(combinations(expenses, 2))

len(all_expense_pairs)

def sums(values):
    return sum(values) == 2020

result = list(filter(sums, all_expense_pairs))

product_result = numpy.prod(result)

all_expense_triplets = list(combinations(expenses, 3))

result2 = list(filter(sums, all_expense_triplets))

product_result2 = numpy.prod(result2)

if __name__ == "__main__":  
    print('Part 1 solution:', product_result)
    print('Part 2 solution:', product_result2)