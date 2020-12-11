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


import collections
import parglare

desc = open("../inputs/input07.txt").readlines()

grammar = r"""
LINE: COLOR 'contain' CONTENTS;

COLOR: word word BAG;
BAG: 'bag' | 'bags' ;

CONTENTS: 'no' 'other' 'bags' dot
        | BAG_AMOUNT_LIST dot;

BAG_AMOUNT_LIST: number COLOR COMMA_AMOUNT_COLOR* ;

COMMA_AMOUNT_COLOR: ',' number COLOR;

terminals
word: /\w+/;
number: /\d+/;
dot: /[.]/;
"""

# Simplify the syntax tree:
actions = {
    'LINE': lambda _, nodes: (nodes[0], nodes[2]),
    'COLOR': lambda _, nodes: "{} {}".format(nodes[0], nodes[1]),
    'CONTENTS': [lambda _, nodes: [],
                 lambda _, nodes: nodes[0]],
    'BAG_AMOUNT_LIST': lambda _, nodes: [(int(nodes[0]), nodes[1])] + nodes[2],
    'COMMA_AMOUNT_COLOR': lambda _, nodes: (int(nodes[1]), nodes[2])
}

g = parglare.Grammar.from_string(grammar)
parser = parglare.Parser(g, actions=actions)
    

graph = {}
graph_rev = collections.defaultdict(set)
for line in desc:
    color, contents = parser.parse(line)
    assert color not in graph
    graph[color] = contents
    for _, contents_col in contents:
        graph_rev[contents_col].add(color)

# A
contains_shiny_gold = set()
def dfs(n):
    if n in contains_shiny_gold:
        return
    contains_shiny_gold.add(n)
    for x in graph_rev[n]:
        dfs(x)
dfs('shiny gold')
print("Answer A:", len(contains_shiny_gold)-1)

def count_tot(n):
    res = 1 
    for am, what in graph[n]:
        res += am * count_tot(what)
    return res
print("Answer B:", count_tot('shiny gold') - 1)
