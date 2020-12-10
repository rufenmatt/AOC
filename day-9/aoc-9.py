#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:37:29 2020

@author: mattiaruefenacht
"""

import os
from typing import List
from itertools import combinations, product

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-9')

def get_data() -> List[int]:
    with open("input.txt") as doc:
        return list(map(int, doc.readlines()))

def find_error(numbers: List[int], preamble: int) -> int:
    for i in range(preamble, len(numbers)):
        if not any(sum(c) == numbers[i] for c in combinations(numbers[i-preamble:i], r=2)):
            return numbers[i]
    raise ValueError("value not found")

def find_encryption_weakness(numbers: List[int], first_error: int) -> int:
    for i, j in product(range(len(numbers)), range(1, len(numbers) + 1)):
        if i >= j:
            continue
        slice = numbers[i:j]
        if sum(slice) == first_error:
            return min(slice) + max(slice)
    raise ValueError("weakness not found")

def main():
    numbers = get_data()
    first_error = find_error(numbers, 25)

    print('Part 1 solution:', first_error)
    print('Part 2 solution:', find_encryption_weakness(numbers, first_error))

if __name__ == "__main__":
    main()