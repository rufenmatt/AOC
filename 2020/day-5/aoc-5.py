#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:03:15 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-5')

def binsearch(lo, hi, goleft, s):
    for c in s:
        midway = (lo + hi) // 2

        if c == goleft:
            hi = midway
        else:
            lo = midway+1
    return lo

def solverA(lines):
    highest = 0

    for line in lines:
        row = binsearch(0, 127, 'F', line[:7])
        col = binsearch(0, 7, 'L', line[7:])
        id = row * 8 + col

        highest = max(highest, id)
    return highest

if __name__ == '__main__':
    lines = []

    with open('input.txt') as doc:
        for line in doc.readlines():
            lines.append(line.strip())

    print('Part 1 solution:', solverA(lines))   

def solverB(lines):
    ids = set()

    for line in lines:
        row = binsearch(0, 127, 'F', line[:7])
        col = binsearch(0, 7, 'L', line[7:])
        id = row * 8 + col
        ids.add(id)
    return [x for x in range(min(ids), max(ids) + 1) if x not in ids][0]

if __name__ == '__main__':
    lines = []

    with open('input.txt') as doc:
        for line in doc.readlines():
            lines.append(line.strip())

    print('Part 2 solution:', solverB(lines))
