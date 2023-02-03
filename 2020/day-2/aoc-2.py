#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:20:16 2020

@author: mattiaruefenacht
"""

import os
import re

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-2')

file = open('input.txt')

lines = file.read()
pattern = re.compile(r'(\d+)[-](\d+)\s([a-z]):\s(.*)\n')
matches = pattern.findall(lines)

valid_passwords = 0
for match in matches:
    min = int(match[0])
    max = int(match[1])
    char = match[2]
    password = match[3]
    letter_patt = re.compile(char)
    p_mat_size = len(letter_patt.findall(password))
    
    if min <= p_mat_size <= max:
        valid_passwords += 1

print('Part 1 solution:', valid_passwords)

valid_passwords = 0
for match in matches:
    pos1 = int(match[0])
    pos2 = int(match[1])
    char = match[2]
    password = match[3]

    if (char == password[pos1 - 1] or char == password[pos2 - 1]) and not (char == password[pos1 - 1] and char == password[pos2 - 1]):
        valid_passwords += 1

print('Part 2 solution:', valid_passwords)