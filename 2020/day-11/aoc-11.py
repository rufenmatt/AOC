#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 10:12:05 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-11')

def get(grid, a, b):
    return 0<=a<len(grid) and 0<=b<len(grid[a])

def neighbors(grid, y, x, search):
    a = b = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i or j:
                off_i = i
                off_j = j
                while get(grid, y+off_i, x+off_j) and grid[y+off_i][x+off_j]=="." and search:
                    off_i += i
                    off_j += j
                a += not get(grid,y+off_i,x+off_j) or grid[y+off_i][x+off_j] in "L."
                b += get(grid,y+off_i,x+off_j) and grid[y+off_i][x+off_j] == "#"
    return a,b

def choose(neighbor, currrent, threshold):
    if currrent == ".":
        return "."
    if neighbor[0] == 8:
        return "#"
    if neighbor[1] >= threshold and currrent == "#":
        return "L"
    return currrent

def simulate(grid, search, neigh):
    while True:
        new_grid = [[choose(neighbors(grid,y,x,search), grid[y][x], neigh) for x in range(len(grid[y]))] for y in range(len(grid))]
        if new_grid == grid:
            break
        grid = new_grid
    return sum(x.count("#") for x in new_grid )

if __name__ == "__main__":
    with open("input.txt") as doc:
        grid = [list(line.strip()) for line in doc.readlines()]

    print("Part 1 solution:", simulate(grid, False, 4))
    print("Part 2 solution:", simulate(grid, True, 5))
