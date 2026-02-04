from sympy import solve, Float, Mul
from tabulate import tabulate
from equations import *
from symbols import *

if __name__ == "__main__":
    print("Solving...")

    sets = solve(equations, dict=True)
    count = len(sets)

    if count == 0:
        print("No solutions found! System might be over-constrained.", end="\n\n")
        exit(1)

    print(f"{len(sets)} solution sets", end="\n\n")

    for index, solutions in enumerate(sets):
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
