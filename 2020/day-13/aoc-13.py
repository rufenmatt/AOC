#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:10:11 2020

@author: mattiaruefenacht
"""

import os
import re
import numpy as np

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-13')

with open('input.txt') as doc:
    content = doc.read()
time = int(content.splitlines()[0])
buses = [int(bus) for bus in re.findall('\d+', content.splitlines()[1])]

waiting_times = []
for bus in buses:
    time = bus - time%bus
    waiting_times.append(time)

next_bus = buses[np.argmin(waiting_times)]
print("Part 1 solution:", next_bus * min(waiting_times))

bus_line = content.splitlines()[1].split(',')

parts = ['t%'+bus_line[0]+'==0']
for i, bus in enumerate(bus_line[1:],1):
    if bus=='x':
        continue
    else:
        while i > int(bus):
            i -= int(bus)
        parts.append(f"{bus}-t%{bus}=={i}")

t = buses[0]
ups = buses[0]
for part in parts[1:]:
    inc = []
    while len(inc)<2:
        if eval(part.replace('t',str(t))):
            inc.append(t)
        t += ups
    t = inc[0]
    ups = inc[1] - inc[0]
print("Part 2 solution:", t)
