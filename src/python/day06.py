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
