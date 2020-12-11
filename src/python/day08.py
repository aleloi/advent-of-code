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
import prog_runner as pr

inp = open("../../inputs/input08.txt").read()
# sample is pr.parse_program(pr.sample)

prog = pr.parse_program(inp)
prog_results_one = pr.run_program(
    prog, terminate_if_position_loop=True)
print("Part one:", prog_results_one.acc_value)


def flip(instr_name):
    if instr_name == "jmp": return "nop"
    elif instr_name == "nop": return "jmp"
    assert False

for i in range(len(prog)):
    instr_i = prog[i]
    name, args = instr_i.name, instr_i.args
    if name in ["jmp", "nop"]:
        prog[i] = pr.Instr(flip(name), args)
        prog_results_two = pr.run_program(
            prog, terminate_if_position_loop=True)
        
        if prog_results_two.terminated_why == "exited":
            print("Part two:", prog_results_two.acc_value)
            break
        else:
            prog[i] = instr_i
            
    
    
