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


"""https://adventofcode.com/2020/day/9"""
import sys
import prog_runner as pr
import os
from functools import lru_cache

curr_dir = os.path.dirname(os.path.abspath(__file__))

inp = [int(x) for x in open(os.path.join(curr_dir, "../../inputs/input10.txt")).readlines()]
inp = [0] + list(sorted(inp))

diff1 = 0
diff3 = 0
curr = 0

for i in inp:
    assert abs(i-curr) <= 3
    if abs(i-curr) == 1:
        diff1 += 1
    if abs(i-curr) == 3:
        diff3 += 1
    curr = i

print("Part one:", diff1 * (diff3+1))

@lru_cache(maxsize=None)
def count2(pos):
    if pos == 0:
        return 1
    res = 0
    for offset in (-3, -2, -1):
        prev_pos = pos+offset
        if prev_pos >= 0:
            if abs(inp[prev_pos] - inp[pos]) <= 3:
                res += count2(prev_pos)
    return res

print("Part two:", count2(len(inp)-1))

