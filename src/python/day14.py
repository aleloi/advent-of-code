# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""https://adventofcode.com/2020/day/14"""
import sys
import math
import copy
import collections
import sys
import prog_runner as pr
import os
from functools import lru_cache


import api

curr_dir = os.path.dirname(os.path.abspath(__file__))
inp = api.get_data(day=14)


sample = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

sample2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

inp = [x for x in inp.strip().split("\n")]

all_one = (1<<36) - 1
def set_bit(num, bit, bit_val):
    if bit_val == 0:
        num &= ((1<<bit) ^ all_one)
    elif bit_val == 1:
        num |= (1<<bit)
    else: assert False
    return num

def apply_mask(mask, val):
    """ The first version where 0/1 means set to 0/1  """
    for i, bit_val in enumerate(reversed(mask)):
        if bit_val != 'X':
            val = set_bit(val, i, int(bit_val))
    return val

def apply_mask2(mask, val):
    """ The second version where 0 means ignore, 1 means flip """
    for i, bit_val in enumerate(reversed(mask)):
        if bit_val == '1':
            val = set_bit(val, i, 1)
    return val


def get_adresses(mask, addr):
    addr_L = [apply_mask2(mask, addr)]
    #print("   ", addr_L)
    for i, x in enumerate(reversed(mask)):
        if x == 'X': # just 9 times:
            addr_L = [set_bit(A, i, 0) for A in addr_L] + \
                     [set_bit(A, i, 1) for A in addr_L]
    return addr_L

mask = None
mem = {}
max_x = 0
for row in inp:
    a, b = row.split(" = ")
    if a.startswith("mask"):
        mask = b
    elif a.startswith("mem"):
        arg = int(b)
        addr = int(a.split('[')[1][:-1])
        adresses = get_adresses(mask, addr)
        for addr in adresses:
            mem[addr] = arg
print("Two: %d" %sum(mem.values()))
