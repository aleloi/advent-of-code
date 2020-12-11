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
