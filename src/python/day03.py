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
