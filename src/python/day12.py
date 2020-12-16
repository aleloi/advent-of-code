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


"""https://adventofcode.com/2020/day/12"""
import copy
import collections
import sys
import prog_runner as pr
import os

import api

def parse(x):
    return x[0], int(x[1:])

def parse_input(inp):
    return [parse(x.strip()) for x in inp.strip().split("\n")]
            
inp = parse_input(api.get_data(day=12))

sample = parse_input(
"""F10
N3
F7
R90
F11
""")

        
"""
# For writing the code below:

   (1, 0)
     N
   (0,0) E (0, 1)
     S
   (-1, 0)

^
|  * (4, 3)
|
|
|
#--------->
|     * rot right, (-3, 4)
|
|    


"""

dirs2vecs = {'N': (1, 0), 'E': (0, 1), 'S': (-1, 0), 'W': (0, -1)}
rotate_full_right = [dirs2vecs[x] for x in "ESWNESWN"]

def rotate_right(vec):
    x, y = vec
    return -y, x
    
    
def follow(pos, vec, times):
    x, y = pos
    dx, dy = vec
    return (x + times*dx, y + times*dy)

def to_str(pos):
    return "east {}, north {}".format(pos[1], pos[0])

def go(pos, dr, commands):
    for cmd, arg in commands:
        if cmd in dirs2vecs:
            vec = dirs2vecs[cmd]
            pos = follow(pos, vec, arg)
            
        elif cmd in 'LR':
            if cmd == 'L':
                cmd, arg = 'R', 360-arg
            assert 0 <= arg < 360
            assert arg % 90 == 0
            turns = arg // 90
            curr_dr = rotate_full_right.index(dr)
            dr = rotate_full_right[curr_dr+turns]
        elif cmd == 'F':
            pos = follow(pos, dr, arg)
    return pos


def go2(pos, waypoint, commands):
    for cmd, arg in commands:
        if cmd in dirs2vecs:
            vec = dirs2vecs[cmd]
            waypoint = follow(waypoint, vec, arg)
            
        elif cmd in 'LR':
            if cmd == 'L':
                cmd, arg = 'R', 360-arg
            assert 0 <= arg < 360
            assert arg % 90 == 0
            turns = arg // 90
            for _ in range(turns):
                waypoint = rotate_right(waypoint)
        elif cmd == 'F':
            pos = follow(pos, waypoint, arg)
    return pos

res = go(pos = (0, 0), dr = (0, 1), commands=inp)
print(to_str(res))
print("Part one: %d" % (abs(res[0]) + abs(res[1])))


res2 = go2(pos = (0, 0), waypoint = (1, 10), commands=inp)
print(to_str(res2))
print("Part two: %d" % (abs(res2[0]) + abs(res2[1])))

