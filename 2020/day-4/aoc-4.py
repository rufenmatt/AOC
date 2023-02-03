#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:01:19 2020

@author: mattiaruefenacht
"""

import os
import re

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-4')

with open("input.txt") as doc:
    lines = [x.strip() for x in doc]

expected = set("byr iyr eyr hgt hcl ecl pid".split())
passports = []
valids = 0
count = 0

while count < len(lines):
    d = ""
    while len(lines[count]) > 0:
        d += " " + lines[count]
        count += 1
        if count == len(lines):
            break
    passports.append(d)
    count += 1

validsTwo = 0

for p in passports:
    chunks = p.split()
    actual = set([c.split(":")[0] for c in chunks])
    if len(expected - actual) == 0:
        valids += 1
        d = dict([c.split(":") for c in chunks])
        c1 = len(d["byr"]) == 4 and 1920 <= int(d["byr"]) <= 2002
        c2 = len(d["iyr"]) == 4 and 2010 <= int(d["iyr"]) <= 2020
        c3 = len(d["eyr"]) == 4 and 2020 <= int(d["eyr"]) <= 2030
        c4 = (re.match("^\d\d\dcm$", d["hgt"]) is not None and 150 <= int(d["hgt"][:-2]) <= 193) or (re.match("^\d\din$", d["hgt"]) is not None and 59 <= int(d["hgt"][:-2]) <= 76)
        c5 = re.match("^#[a-f0-9]{6}$", d["hcl"]) is not None
        c6 = d["ecl"] in ("amb blu brn gry grn hzl oth".split())
        c7 = re.match("^\d{9}$", d["pid"]) is not None
        if all([c1, c2, c3, c4, c5, c6, c7]):
            validsTwo += 1

if __name__ == "__main__":
    print('Part 1 solution:', valids)
    print('Part 2 solution:', validsTwo)
