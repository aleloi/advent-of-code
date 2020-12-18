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


"""https://adventofcode.com/2020/day/18"""
import sys
import math
import copy
import collections
import itertools
import sys
import os
from functools import lru_cache

import prog_runner as pr
import api

inp = api.get_data(day=18) #  "1 + 2 * 3 + 4 * 5 + 6"  # 

inp = inp.strip().split("\n")

def do_parse(row):
    """Parses 

    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2".
        

    into 

    [[[2, '+', 4, '*', 9], '*', [6, '+', 9, '*', 8, '+', 6], '+', 6], '+', 2, '+', 4, '*', 2]
    """
    tokens = row.replace('(', ' ( ').replace(')', ' ) ').split()
    lst = []
    _do_parse(tokens, lst)
    return lst

def _do_parse(tok_stack, res_stack):
    """Recursive parsing, pops tokens from stack until it finds an extra
    ')', appends parsed result to res_stack.

    Example:
    when tok_stack = [2 + 3 - 4 * ( 5 / 6 + 2 ) ) * 2 ... ] will pop
    the tokens `2 + 3 - 4 * ( 5 / 6 + 2 )` from the stack, parse them as 
    [2 + 3 - 4 * [5 / 6 + 2]] and push them to the result stack

    """
    while tok_stack:
        x = tok_stack.pop(0)
        if x not in '()':
            if x not in '+*':
                res_stack.append(int(x))
            else: res_stack.append(x)
        elif x == '(':
            res_stack_rec = []
            _do_parse(tok_stack, res_stack_rec)
            res_stack.append(res_stack_rec)
            assert tok_stack[0] == ')'
            tok_stack.pop(0)
        elif x == ')':
            tok_stack.insert(0, x)
            return

def eval_one(thing, part_two):
    if type(thing) is int:
        return thing
    assert type(thing) is list
    return do_eval(thing, part_two)

def fix_prec(lst):
    """Hack to add paretheses to fix the precedence, + evaluated before *"""
    if '*' not in lst: return lst
    lst2 = []
    while '*' in lst:
        nxt = lst.index('*')
        lst2.append(lst[:nxt])
        lst2.append('*')
        lst = lst[nxt+1:]
        
    lst2.append(lst)
    return lst2

def do_eval(lst, part_two = False):
    lst = copy.deepcopy(lst)
    while True:
        if len(lst) == 1:
            return eval_one(lst[0], part_two)
        if part_two: 
            lst = fix_prec(lst)
        a, op, b, rest = *lst[:3], lst[3:]
        assert op in '*+'
        a, b = eval_one(a, part_two), eval_one(b, part_two)
        if op == '*':
            res = a * b
        else: 
            res = a+b
        lst = [res] + rest
                    

res_one = 0
res_two = 0
for row in inp:
    parsed = do_parse(row)
    res_one += do_eval(parsed, False)
    res_two += do_eval(parsed, True)
print("One: %d" % res_one)
print("Two: %d" % res_two)

def submit(answer, level):
    api.submit(answer, level, day=18, year=2020)
