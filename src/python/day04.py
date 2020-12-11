import re
passports = open("input04.txt").read().split("\n\n")
import collections

# My Python (3.6) doesn't have dataclasses :-(
Field = collections.namedtuple(
    "Field",
    ["name", "pattern", "validator"])

def validate_height(hgt):
    hgt_unit = hgt[-2:]
    hgt_value = int(hgt[:-2])
    if hgt_unit == "cm":
        if not 150 <= hgt_value <= 193: return False
    if hgt_unit == "in":
        if not 59 <= hgt_value <= 76: return False
    return True

fields = [
    Field("byr", "\d+", lambda x: 1920 <= int(x) <= 2002),
    Field("iyr", "\d+", lambda x: 2010 <= int(x) <= 2020),
    Field("eyr", "\d+", lambda x: 2020 <= int(x) <= 2030),
    Field("hgt", "\d+(in|cm)", validate_height),
    Field("hcl", "#([0-9a-f]){6}", lambda x: True),
    Field("ecl", ".*",
          lambda x: x in "amb blu brn gry grn hzl oth".split()),
    Field("pid", "\d{9}", lambda x: True)
]

def validate(key_val):
    return (all(f.name in key_val for f in fields) and
            all(re.fullmatch(f.pattern, key_val[f.name]) for f in fields) and
            all(f.validator(key_val[f.name]) for f in fields))

        
if __name__ == "__main__":
    num_valid = 0
    for ppt in passports:
        ppt = ppt.split()
        key_vals = dict(
            x.split(":") for x in ppt
        )
        num_valid += validate(key_vals)
    
    print(num_valid)
