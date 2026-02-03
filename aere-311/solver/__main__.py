from sympy import solve, Float, Mul
from tabulate import tabulate
from equations import *

if __name__ == "__main__":
    solution_sets = solve(equations)

    for index, solutions in enumerate(solution_sets):
        knowns = {}
        unknowns = {}

        for key, value in solutions.items():
            if isinstance(value, Float):
                units = output_units[key] if key in output_units else base_units[key]
                knowns[key] = (float(value) * base_units[key]).to(units)
            elif isinstance(value, Mul):
                unknowns[key] = value
            else:
                raise Exception(f"Unknown solution type: {type(value)}")

        if len(knowns) > 0:
            print(f"Set {index + 1} knowns:")
            print(tabulate(knowns.items()), end="\n\n")

        if len(unknowns) > 0:
            print(f"Set {index + 1} unknowns:")
            print(tabulate(unknowns.items()), end="\n\n")
