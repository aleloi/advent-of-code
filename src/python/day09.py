"""https://adventofcode.com/2020/day/9"""
import sys
import prog_runner as pr
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

inp = [int(x) for x in open(os.path.join(curr_dir, "../../inputs/input09.txt"))]

def check(window, x):
    for a in window:
        for b in window:
            if a+b == x:
                return True
    return False

def part_one(inp):
    for i, x in enumerate(inp):
        # Skip preamble:
        if i < 25: continue

        # Look back 25 steps:
        window = inp[i-25:i]
        if not check(window, x):
            return(x)
    assert False
    
invalid_number = part_one(inp)
print("Part one:", invalid_number)

def part_two(inp):
    """O(N**2), N is only 1000 in the problem. Checks which substring of the input
    sums to `invalid_number` from part one"""

    # Sliding window approach to avoid O(N**3) - which would also
    # have worked and been faster to write :/
    inp.insert(0, 0) # To avoid a special case in the beginning.
    for win_length in range(2, len(inp)+1):
        prev_sum = sum(inp[:win_length])
        for first_idx in range(1, len(inp)):
            last_idx = first_idx + win_length - 1
            
            if last_idx >= len(inp): break

            # Update sliding window sum
            prev_sum += inp[last_idx] - inp[first_idx-1]
            if prev_sum == invalid_number:
                window = inp[first_idx : first_idx + win_length]
                return min(window) + max(window)
    assert False

print("Part two:", part_two(inp))
