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


"""https://adventofcode.com/2020/day/17"""
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

inp = api.get_data(day=17)

def neighs(pos):
    for dpos in itertools.product([-1, 0, 1], repeat=len(pos)):
        if dpos != tuple([0]*len(pos)):
            yield tuple(x+dx for x, dx in zip(pos, dpos))
    
def sim(d):
    d_c = collections.defaultdict(bool)
    keys = {pos for pos in d if d[pos]}
    all_neighs = set()
    for pos in keys:
        for neig in neighs(pos):
            all_neighs.add(neig)
    
    for pos in keys|all_neighs:
        active_neigh = 0
        for neig in neighs(pos):
            if d[neig]:
                active_neigh += 1
        if d[pos] and active_neigh in [2, 3]:
            d_c[pos] = True
        elif not d[pos] and active_neigh == 3:
            d_c[pos] = True
        else:
            d_c[pos] = False
    return d_c

d3D = collections.defaultdict(bool)
d4D = collections.defaultdict(bool)
for i, row in enumerate(inp.strip().split("\n")):
    for j, col in enumerate(row):
        if col == '#':
            d3D[(i, j, 0)] = True
            d4D[(i, j, 0, 0)] = True

print("Wait for it, it's a little slow...")
for i in range(6):
    d3D = sim(d3D)
    d4D = sim(d4D)
    print("Completed iteration %d of %d" % (i+1, 6))

print("One %d" % sum(d3D.values()))
print("Two %d" % sum(d4D.values()))
