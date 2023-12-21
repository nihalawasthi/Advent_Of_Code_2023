import re
from itertools import product
from functools import partial

with open("D:\My\Problem Solutions\Advent_of_code_2023\Day_19\input.txt") as file:
    rules, parts = [g.split("\n") for g in file.read().strip().split("\n\n")]

def A(x, m, a, s):
    return x + m + a + s

def R(x, m, a, s):
    return 0

def generate_function(name, workflow):
    workflow = workflow[:-1].replace(":", ": return ")
    if name == "in":
        name = "_in"
    rule_parts = [f"{x}(x,m,a,s)" for x in workflow.split(",")]
    function_body = f"def {name}(x,m,a,s):\n"
    for i, part in enumerate(rule_parts):
        if i == 0:
            pre = "if "
        elif i == len(rule_parts) - 1:
            pre = "else: return "
        else:
            pre = "elif "
        function_body += f"    {pre}{part}\n"
    exec(function_body)
    return locals()[name]

# Generating functions based on rules
for l in rules:
    name, workflow = l.split("{")
    generated_func = generate_function(name, workflow)

# Part 1 - Evaluating generated functions
print(sum(eval(f"_in({g[1:-1]})") for g in parts))
