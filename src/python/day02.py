inp = [x.split() for x in open('input02.txt').readlines()]
# Example: "4-6" "b:" "bbbdbtbbbj"

def is_valid_TWO(fro, to, lttr, pw):
    return (pw[fro-1] == lttr) ^ (pw[to-1] == lttr)
        

num_valid = 0
for occs, lttr, pw in inp:
    fro, to = occs.split("-")
    fro, to = int(fro), int(to)
    lttr = lttr[0]
    # part ONE:
    # num_valid += (fro <= pw.count(lttr) <= to)
    num_valid += is_valid_TWO(fro, to, lttr, pw)
print(num_valid)
