#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:39:33 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-15')

with open("input.txt", "r") as doc:
    nums = {int(n): i for i, n in enumerate(doc.read().split(","), 1)}

def solve(nums, turns):
    prev = nums.popitem()[0]

    for turn in range(len(nums) + 1, turns):
        nums[prev], prev = turn, turn - nums.get(prev, turn)

    return prev

if __name__ == "__main__":
    print("Part 1 solution:", solve(nums.copy(), 2020))
    print("Part 2 solution:", solve(nums.copy(), 30000000))