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
            
    
    
