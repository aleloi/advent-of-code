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
from typing import List

InstrDescription = collections.namedtuple("InstrDescription",
                                          "name, arity")

instr_descs = [InstrDescription("acc", 1),
               InstrDescription("jmp", 1),
               InstrDescription("nop", 1)]

instr_descs = {desc.name: desc for desc in instr_descs}

Instr = collections.namedtuple("Instr", "name, args")

def parse_program(program: str) -> List[Instr]:
    lines = program.strip().split("\n")
    tokens = [line.split() for line in lines]
    prog = []
    for (name, *args) in tokens:
        if name not in instr_descs:
            raise ValueError("Unknown instruction name: %s" % name)
        if instr_descs[name].arity != len(args):
            raise ValueError(
                "Wrong arguments to %s: %s" % name, str(args))
        instr = Instr(name, tuple(map(int, args)))
        prog.append(instr)
    return prog


ProgramResult = collections.namedtuple(
    "ProgramResult",
    "acc_value, last_pos, terminated_why, pos_histogram, states_vis"
)
ProgramResult.defaults = (None, None)

def run_program(program: List[Instr],
                terminate_if_position_loop: bool) -> ProgramResult:
    ACC = 0
    POS = 0
    pos_histogram = collections.Counter()
    vis = set()
    def state():
        return (POS, ACC)
    def termination_condition():
        return (POS == len(program) or
                (terminate_if_position_loop and
                 pos_histogram[POS] > 0) or
                state() in vis
        )
    while not termination_condition():
        vis.add(state())
        pos_histogram.update([POS])
        instr = program[POS]
        arg0, *arg_rest = instr.args

        # Update POS
        if instr.name == "jmp":
            POS += arg0
        else:
            POS += 1

        # Update ACC
        if instr.name == "acc":
            ACC += arg0

    # Figure out why it (was?) terminated and collect results
    results = {"acc_value": ACC, "last_pos": POS,
               "pos_histogram": pos_histogram,
               "states_vis": vis
    }
    if POS == len(program):
        terminate_why = "exited"
    elif (state() not in vis and
          pos_histogram[POS] > 0 and
          terminate_if_position_loop):
        terminate_why = "position loop"
    elif state() in vis:
        terminate_why = "state loop"
    results["terminated_why"] = terminate_why

    return ProgramResult(**results)


sample = \
"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
