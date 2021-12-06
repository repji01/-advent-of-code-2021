#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2021 --- Day 1: Report Repair ---
   https://adventofcode.com/2020/day/2
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import advent
from utils import *


def download_input_data():
    global lines
    advent.setup(2021, 2, dry_run=False)
    fin = advent.get_input()
    lines = get_lines(fin.readlines())


def part01():
    global lines
    aim = position = depth = 0
    for command in lines:
        cmd, amount = command.split()
        if cmd == "up":
            depth -= int(amount)
        if cmd == "down":
            depth += int(amount)
        if cmd == "forward":
            position += int(amount)
        print(f"[{command.ljust(15)}] DEPTH: {depth} POS: {position}")

    #assert total == 1446
    advent.submit_answer(1, position*depth)


def part02():
    global lines
    aim = position = depth = 0
    for command in lines:
        cmd, amount = command.split()
        if cmd == "up":
            aim -= int(amount)
        if cmd == "down":
            aim += int(amount)
        if cmd == "forward":
            position += int(amount)
            depth += aim * int(amount)
        print(f"[{command.ljust(15)}] DEPTH: {depth} POS: {position}")

    #assert total == 1446
    advent.submit_answer(2, position*depth)


if __name__ == "__main__":
    download_input_data()
    timer_start()
    part01()
    #part02()