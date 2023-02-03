#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:10:21 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-10')

def main():
    doc = open("input.txt", "r")
    xs = [int(line.strip()) for line in doc.readlines() if line.strip()]
    xs.sort()
    xs = [0] + xs + [xs[-1] + 3]
    last = 0
    a, b = 0, 0
    for x in xs:
        assert x - last <= 3
        if x - last == 1:
            a += 1
        elif x - last == 3:
            b += 1
        last = x
    print('Part 1 solution:', a * b)

    dp = [1]
    for i in range(1, len(xs)):
        ans = 0
        for j in range(i):
            if xs[j] + 3 >= xs[i]:
                ans += dp[j]
        dp.append(ans)

    print("Part 2 solution:", dp[-1])

if __name__ == "__main__":
    main()