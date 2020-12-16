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


"""https://adventofcode.com/2020/day/16"""
import sys
import math
import copy
import collections
import sys
import prog_runner as pr
import os
from functools import lru_cache


import api

inp = api.get_data(day=16)

valid, your, others = inp.split("\n\n")


def parse_range(x):
    a, b = x.split("-")
    return (int(a), int(b))

d = collections.defaultdict(list)
valid_ranges = []
for v_row in valid.split("\n"):
    #print(v_row)
    name, v_row = v_row.split(": ")
    A, B = v_row.split(" or ")
    for x in [A, B]:
        valid_ranges.append(parse_range(x))
        d[name].append(parse_range(x))


def some_valid(x, valid_range):
    for a, b in valid_range:
        assert a <= b
        if a <= x <= b:
            return True
    return False

scan_error_rate = 0
    
for ticket in others.strip().split("\n")[1:]:
    nums = [int(x) for x in ticket.split(",")]
    for x in nums:
        if not some_valid(x, valid_ranges):
            scan_error_rate += x
            
print(len(others.strip().split("\n")[1:]), "tickets in total")
print("One: %d" % scan_error_rate)

# Part 2:
valid_tickets = []
for ticket in others.strip().split("\n")[1:]:
    nums = [int(x) for x in ticket.split(",")]
    if all(some_valid(x, valid_ranges) for x in nums):
        valid_tickets.append(nums)

print(len(valid_tickets), "are valid")

def all_valid(column, valid_ranges):
    for c in column:
        for a, b in valid_ranges:
            if a <= c <= b:
                break
        else:
            return False
    return True

num_cols = len(valid_tickets[0])
assert num_cols == len(d)
matches = collections.defaultdict(list)
for col_num in range(num_cols):
    col = [x[col_num] for x in valid_tickets]
    for field in d:
        if all_valid(col, d[field]):
            matches[col_num].append(field)

def find_matching(m):
    curr_match = dict()
    left_A = set(m.keys())
    left_B = set()
    for lst in m.values():
        for x in lst:
            left_B.add(x)

    final_matching = None
    rec_invocations = 0
            
    def rec():
        nonlocal final_matching
        nonlocal rec_invocations
        rec_invocations += 1
        
        if not left_A:
            print("Found matching!")
            assert final_matching is None
            final_matching = copy.copy(curr_match)
            return

        # Optimization for DFS-match:
        # Sort the remaining ones by number of possible matches.
        left_A_sorted = list(left_A)
        left_A_sorted.sort(key = lambda x:
                           len(set(m[x]) & left_B))

        x = left_A_sorted[0]
        for y in m[x]:
            if y in left_B:
                curr_match[x] = y
                left_A.remove(x)
                left_B.remove(y)
                rec()
                del curr_match[x]
                left_A.add(x)
                left_B.add(y)
    rec()
    print("%d invocations of DFS-backtracking matching finder" % rec_invocations)
    return final_matching

matching = find_matching(matches)

your = [int(x) for x in your.strip().split("\n")[-1].split(",")]
res = 1
for i, x in enumerate(your):
    field = matching[i]
    if field.startswith("departure"):
        res *= x
print("Two: %d" % res)

