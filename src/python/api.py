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


import os
import datetime
import requests

# Read from ~/.config/aoc/session
AOC_SESSION = open("/Users/aleloi/.config/aoc/session").read()

now = datetime.datetime.now()
year, month, day = now.year, now.month, now.day
assert month == 12

curr_dir = os.path.dirname(os.path.abspath(__file__))
cache_path = lambda day: os.path.join(curr_dir,
                                      "../../inputs/input{:0>2}.txt".format(int(day)))

def get_data(day=day, year=year):
    assert year == 2020
    if os.path.isfile(cache_path(day)):
        with open(cache_path(day), 'r') as f:
            return f.read()
    r = requests.get(
        "https://adventofcode.com/{year}/day/{day}/input".format(
            year=year, day=day
        ),
        cookies={'session': AOC_SESSION}
    )
    
    # Request result copied from
    # https://github.com/exoji2e/aoc20/blob/main/runner.py.
    if 'Puzzle inputs' in r.text:
        log.w('Session cookie expired?')
        return r.text
    if "Please don't repeatedly request this endpoint before it unlocks!" in r.text:
        log.w('Output not available yet')
        return r.text
    if r.status_code != 200:
        log.w('Not 200 as status code')
        return r.text
    
    with open(cache_path(day),'w') as f:
        f.write(r.text)

    return r.text

def submit(answer, level, day=day, year=year):
    """Use kwargs for day, year!"""
    assert year == 2020
    assert level in [1, 2]
    r = requests.post("https://adventofcode.com/{year}/day/{day}/answer".format(
        year=year, day=day),
                        cookies={'session': AOC_SESSION},
                        data = {'level': str(level), 'answer': str(answer)}
    )
    if "That's the right answer" not in r.text:
        print(r.text)
    else:
        print("AC!")
    
