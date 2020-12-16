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


"""https://adventofcode.com/2020/day/13"""
import sys
import math
import copy
import collections
import sys
import prog_runner as pr
import os


import api

inp = api.get_data(day=13)

# 17,x,13,19:
# t % 17 = 0
# t % 13 = 2
# t % 19 = 3
# -----------
def mod_inv(x, mod):

    def egcd(a, b):
        """
        a*A + b*B = gcd(a, b),
        returns (A, B)
        """
        assert a > 0 and b >= 0
        if b == 0:
            return (1, 0)  # 1*a + 0*0 = a
        """
        a, b div by d ==> a % b, b div by d, gcd(a, b) = gcd(b, a % b)
        a = b*k + (a % b), a%b = a-b*k
        A * b + B * (a%b) = d  ==>  A * b + B*(a - b*k) = d ==>
        a * B + b * (A - B*k) = d
        """
        k = a // b
        A, B = egcd(b, a % b)
        return B, A-B*k

    a, b = egcd(x, mod)
    assert a * x + b * mod == 1
    return a % mod

def crt(rems, mods):
    res = 0
    prod = 1
    for m in mods: prod *= m
    """
    Construct this:
    (1, 0, 0 ...) - divisible by m2, m3, ..., has remainder 1 mod m1

    like this:
    mm := m2*m3*... - this is (x, 0, 0, 0, ...) for some x
    find its inverse inv(mm) mod m1 - it is (x**-1, ?, ?, ?, ?)
    multiply together - this is (1, 0, 0, ...)
    
    """
    for r, m in zip(rems, mods):
        mm = prod // m
        res += mod_inv(mm, m) * mm * r
    return res % prod

T, buses = inp.strip().split("\n")
T = int(T)
buses_or_none = [None if x == "x" else int(x) for x in buses.split(",") ]

def solve2(B):
    mods = [b for b in B if b is not None]
    rems = []
    for i, b in enumerate(B):
        if b is not None:
            rems.append(b-i)
    return crt(rems, mods)

def solveOne():
    for t in range(T, T+int(1e6)):
        for b in buses_or_none:
            if b is not None and t % b == 0:
                ans = b * (t-T)
                return ans
    assert False

def submit(ans, lev):
    api.submit(ans, lev, day=13)

print("One: %d" % solveOne())


print("Two: %d" % solve2(buses_or_none))

