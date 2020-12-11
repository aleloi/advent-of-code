import string
groups = open("input06.txt").read().split("\n\n")

# Part A
resA = 0
for group in groups:
    group = group.replace("\n", "")
    resA += len(set(group))

# Part B
resB = 0
for group in groups:
    group = group.strip().split("\n")
    common = 0
    for q in string.ascii_lowercase:
        if all(q in g for g in group):
            common += 1
    resB += common
    
print(resA, resB)
