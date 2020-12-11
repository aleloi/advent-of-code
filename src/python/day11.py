"""https://adventofcode.com/2020/day/9"""
import copy
import collections
import sys
import prog_runner as pr
import os
from functools import lru_cache

curr_dir = os.path.dirname(os.path.abspath(__file__))

grid_start = [list(x.strip()) for x in
              open(os.path.join(
                  curr_dir, "../../inputs/input11.txt")).readlines()]

N = len(grid_start)
M = len(grid_start[0])

def inside(n, m):
    return 0 <= n < N and 0 <= m < M

vecs = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]

def neigh_one(grid, n, m):
    res = 0
    for i, j in vecs: 
        nn, mm = n+i, m+j
        if inside(nn, mm):
            if grid[nn][mm] == '#':
                res += 1
    return res

def neigh_two(grid, n, m):
    res = 0
    for i, j in vecs: 
        nn, mm = n, m
        occ = False
        while inside(nn+i, mm+j):
            nn, mm = nn+i, mm+j
            if grid[nn][mm] == '#':
                occ = True
                break
            if grid[nn][mm] == 'L':
                occ = False
                break    
        res += int(occ)
    return res

class State:
    def __init__(self, grid):
        self.grid = grid

def turn(state, part_two = False):
    grid = state.grid
    grid_copy = copy.deepcopy(grid)
    neigh_f = (neigh_two if part_two else neigh_one)
    max_occupied = (5 if part_two else 4)

    for n, row in enumerate(grid):
        for m, pos in enumerate(row):
            if grid[n][m] == 'L' and neigh_f(grid, n, m) == 0:
                grid_copy[n][m] = '#'
            elif grid[n][m] == '#' and neigh_f(grid, n, m) >= max_occupied:
                grid_copy[n][m] = 'L'
    state.grid = grid_copy
    
def plot(state):
    for row in state.grid:
        print(''.join(row))


def solve(part_two = False):
    prev_occ = None
    occ = 0
    state = State(copy.deepcopy(grid_start))
    while prev_occ != occ:
        turn(state, part_two = part_two)
        prev_occ = occ
        occ = sum(row.count('#') for row in state.grid)
        # plot(state)
    for _ in range(10):
        turn(state, part_two = part_two)
    print("Part", ("two" if part_two else "one"), ":",
          sum(row.count('#') for row in state.grid))
    
solve(part_two = False)
solve(part_two = True)
