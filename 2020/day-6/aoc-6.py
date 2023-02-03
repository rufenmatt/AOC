#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 12:20:04 2020

@author: mattiaruefenacht
"""

import os
from typing import List
from itertools import chain

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-6')

def grouping() -> List[List[str]]:
    with open("input.txt") as doc:
        return [group.split("\n") for group in doc.read().split("\n\n")]

def count_unique(groups): 
    return sum(len(set(chain(*group))) for group in groups)

def count_common(groups):
    return sum(len(set.intersection(*(set(person) for person in group)))
               for group in groups)

def main():
    input_groups = grouping()
    print('Part 1 solution:', count_unique(input_groups))
    print('Part 2 solution:', count_common(input_groups))

if __name__ == "__main__":
    main()

