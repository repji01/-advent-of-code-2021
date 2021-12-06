#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""day01.py: Advent of Code 2021 --- Day 3: Binary Diagnostic ---
   https://adventofcode.com/2021/day/3
"""

__version__ = "1.0"
__maintainer__ = "Jiří Řepík"
__email__ = "jiri.repik@gmail.com"
__status__ = "Submited"

import collections
import datetime

import advent
from utils import *
import numpy


def download_input_data():
    advent.setup(2021, 6, dry_run=False)
    fin = advent.get_input()
    return fin.read()


def part01(lanternfish_input: list, days: int) -> int:
    for day in range(days):
        new_fish =0
        for idx in range(len(lanternfish_input)):
            lanternfish_input[idx] -= 1
            if lanternfish_input[idx] == -1:
                lanternfish_input[idx] = 6
                new_fish += 1
        lanternfish_input.extend([8] *new_fish)
        print(f"After {day + 1} days: {len(lanternfish_input)}")
    print(len(lanternfish_input))


def part02(s: str, days: int) -> int:
    start_date = dt = datetime.datetime.strptime('Jan 1 1970  1:33PM', '%b %d %Y %I:%M%p')

    numbers = collections.Counter(int(line) for line in s.strip().split(','))
    for day in range(days):
        numbers2 = collections.Counter({8: numbers[0], 6: numbers[0]})
        numbers2.update({k - 1: v for k,v in numbers.items() if k > 0})
        numbers = numbers2
        print("[",dt.strftime('%b %d %Y'),"]",day+1, sum(numbers.values()))
        dt += datetime.timedelta(days=1)
        if dt.year>2070:
            break
    return sum(numbers.values())


# assert total == 1446
# advent.submit_answer(2, position*depth)

TST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".splitlines()

if __name__ == "__main__":
    lanternfish_input = download_input_data()
    lanternfish_input_tst = [3, 4, 3, 1, 2]
    timer_start()
    # input = open("inputs\\2021_03.txt").read().splitlines()

    #assert part01(TST_INPUT) == 198
    print(part02(lanternfish_input, 256*256*256))
    # assert part02(TST_INPUT) == 230
    # print(part02(input))


