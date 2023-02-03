#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 13:28:09 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-3')

with open('input.txt', 'r') as doc:
    tree_map = [line[:-1] for line in doc]

def slope_checkin(run, rise):
    row = 0
    column = 0
    tree_count = 0

    while row < len(tree_map):
        if tree_map[row][column] == '#':
            tree_count += 1
        column = (column + run) % len(tree_map[0])
        row += rise
    return tree_count

slope_1_1 = slope_checkin(1, 1)
slope_3_1 = slope_checkin(3, 1)
slope_5_1 = slope_checkin(5, 1)
slope_7_1 = slope_checkin(7, 1)
slope_1_2 = slope_checkin(1, 2)

if __name__ == "__main__":
    print('Part 1 solution:', slope_3_1)
    print('Part 2 solution:', slope_1_1 * slope_3_1 * slope_5_1 * slope_7_1 * slope_1_2)