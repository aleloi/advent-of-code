import sys

inp = [int(x) for x in open('input01.txt').readlines()]
PART_A = False
if PART_A:
    for x in inp:
        for y in inp:
            if x+y == 2020:
                print(x*y)
                sys.exit()
else:
    for x in inp:
        for y in inp:
            for z in inp:
                if x+y+z == 2020:
                    print(x*y*z)
                    sys.exit()

print("Numbers summing to 2020 not found")
