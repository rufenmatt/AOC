#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:43:03 2020

@author: mattiaruefenacht
"""

import os
import re
import math
import functools

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-14')

def maskBits(number, mask0, mask1):
    masked = number | mask0
    masked = masked & mask1
    return int(masked)

with open("input.txt", "r") as doc:
    operationsOne = {}
    value = 0
    mask1 = 0
    mask0 = 0
    mask = ""
    rmask = r'mask = ([X01]{36})'
    roperation = r'mem\[(\d+)\] = (\d+)'

    for line in doc:
        if re.match(rmask, line):
            mask = re.split(rmask, line)[1]
            mask1 = int(mask.replace("X", "1"), 2)
            mask0 = int(mask.replace("X", "0"), 2)

        else:
            op = re.split(roperation,line)
            operationsOne[op[1]] = maskBits(int(op[2]), mask0, mask1)

print("Part 1 solution:", sum(operationsOne.values()))

def processMask(masks, mask0, mask1, bit):
    if bit == 36:
        masks.append((int(mask0,2), int(mask1,2)))
    else:
        if mask[bit] == "X":
            lmask00 = mask0[0:bit] + "0" + mask0[bit+1: ]
            lmask01 = mask0[0:bit] + "1" + mask0[bit+1: ]
            lmask10 = mask1[0:bit] + "0" + mask1[bit+1: ]
            lmask11 = mask1[0:bit] + "1" + mask1[bit+1: ]
            processMask(masks,lmask00,lmask01,bit+1)
            processMask(masks,lmask10,lmask11,bit+1)
        else:
            lmask1 = mask1[0:bit] + "1" + mask1[bit+1: ]
            lmask0 = mask0[0:bit] + "0" + mask0[bit+1: ]
            processMask(masks, lmask0, lmask1, bit+1)

def modifyBit(n, p, b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)

def makeFloatingBits(number, index, floatingBits,numbers):
    if index >= len(floatingBits):
        numbers.append(number)
    else:
        makeFloatingBits(modifyBit(number, 35 - floatingBits[index], 0), index + 1, floatingBits, numbers)
        makeFloatingBits(modifyBit(number, 35 - floatingBits[index], 1), index + 1, floatingBits, numbers)

with open("input.txt", "r") as doc:
    operationsTwo = {}
    masks = []
    orMask = 0
    rmask = r'mask = ([X01]{36})'
    roperation = r'mem\[(\d+)\] = (\d+)'

    for line in doc:
        if re.match(rmask, line):
            mask = re.split(rmask, line)[1]
            masks = []
            orMask = int(mask.replace("X","0"), 2)
            floating = [i for i, ltr in enumerate(mask) if ltr == "X"]
        else:
            op = re.split(roperation, line)
            numbers = []
            masked = int(op[1]) | orMask
            makeFloatingBits(masked, 0, floating, numbers)
            for number in numbers:
                operationsTwo[number] = int(op[2])

    print("Part 2 solution:", sum(operationsTwo.values()))