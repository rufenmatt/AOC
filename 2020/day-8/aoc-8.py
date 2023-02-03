#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:47:51 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-8')

def hasInfiniteLoop(data):
    visited = set()
    accumulated = 0
    counter = 0

    while True:
        if counter == len(data) - 1:
            return (False, accumulated)

        instruction = data[counter]

        if counter in visited:
            return (True, accumulated)
        elif instruction[0] == "acc":
            accumulated += int(instruction[1])
        elif instruction[0] == "jmp":
            counter += int(instruction[1])
            continue

        visited.add(counter)
        counter += 1

def findWrongInstruction(data):
    for ind, instr in enumerate(data):
        if instr[0] == "jmp" or instr[0] == "nop":
            data_copy = data.copy()
            new_instr = "nop" if instr[0] == "jmp" else "jmp"
            data_copy[ind] = [new_instr, data[ind][1]]

            test = hasInfiniteLoop(data_copy)
            if not test[0]:
                return test[1]

def main():
    doc = open("input.txt", "r")
    data = [x.strip().split() for x in doc.read().strip().split("\n")]

    print('Part 1 solution:', hasInfiniteLoop(data)[1])
    print('Part 2 solution:', findWrongInstruction(data))

if __name__ == "__main__":
    main()

