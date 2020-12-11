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
