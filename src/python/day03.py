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


tree_grid = [x.strip() for x in open('input03.txt').readlines()]

width = len(tree_grid[0])

slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)
]

def go_down(slope):
    dx, dy = slope
    num_trees = 0
    x, y = 0, 0
    while y < len(tree_grid):
        num_trees += tree_grid[y][x % width] == '#'
        x += dx
        y += dy
    return num_trees

res = 1
for slope in slopes:
    res *= go_down(slope)
print(res)
