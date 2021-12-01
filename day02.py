#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2020 --- Day 1: Report Repair ---
   https://adventofcode.com/2020/day/1
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *


def download_input_data():
    global fin
    global nums
    #advent.setup(2021, 1, dry_run=False)
    #fin = advent.get_input()
    #nums = list(map(int, fin.readlines()))


def part01():
    global fin
    global nums
    global total
    total = 0
    for idx, num in enumerate(nums[1:]):
        if (num>nums[idx]):
            total+=1
    assert total == 1446
    advent.submit_answer(1, total)


def part02():
    global fin
    global nums
    global total
    total = 0
    for idx, num in enumerate(nums[3:], start=3):
        if (num > nums[idx - 3]):
            total += 1
    assert total == 1486
    advent.submit_answer(2, total)


if __name__ == "__main__":
    download_input_data()
    timer_start()
    #part01()
    #part02()