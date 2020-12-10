#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 05:47:16 2020

@author: mattiaruefenacht
"""

import os

os.getcwd()

os.chdir(r'/Users/mattiaruefenacht/Desktop/AOC2020/day-7')

  
def parseRaw(raw_data):
    data = {}

    for bag_type in raw_data:
        key = bag_type[0] + " " + bag_type[1]
        contained_bags = iter(bag_type[4:])
        contained_dict = {}

        if "no" not in bag_type:
            for contained in contained_bags:

                bag_amt = contained
                bag_tp = next(contained_bags) + " " + next(contained_bags)
                next(contained_bags)
                contained_dict[bag_tp] = int(bag_amt)

        data[key] = contained_dict
    return data


def canContain(my_bag_type, other_bag_type, data, decision):
    if my_bag_type in data[other_bag_type]:
        decision.append(my_bag_type)
        # print(decision)
        return True
    else:
        for bag_type in data[other_bag_type]:
            can_hold_this = canContain(my_bag_type, bag_type, data, decision)
            if can_hold_this:
                decision.append(bag_type)
                return True
        return False


def howManyWaysToContain(my_bag_type, data):
    total = 0
    for bag_type in data:
        if (canContain(my_bag_type, bag_type, data, [])):
            # print(bag_type)
            total += 1
    return total


def howManyBagsIn(my_bag_type, data):
    total = 0
    if len(data[my_bag_type]) == 0:
        return 1
    else:
        for sub_bag in data[my_bag_type]:
            total += data[my_bag_type][sub_bag] * howManyBagsIn(sub_bag, data)
        return total + 1


def main():
    f = open("input.txt", "r")
    raw_data = [x.strip().split() for x in f.read().strip().split("\n")]
    data = parseRaw(raw_data)

    print('Part 1 solution:', howManyWaysToContain("shiny gold", data))
    print('Part 2 solution:', howManyBagsIn("shiny gold", data) - 1)


if __name__ == "__main__":
    main()