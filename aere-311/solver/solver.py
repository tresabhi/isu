from pint import Quantity
from sympy import solve as sympy_solve, Float, Mul, Add
from units import output_units, base_units
from tabulate import tabulate


def solve(equations, knowns, find=None):
    print("Solving...\n")

    base_knowns = {
        key: (
            value.to(base_units[key]).magnitude
            if isinstance(value, Quantity)
            else value
        )
        for key, value in knowns.items()
    }
    subbed_equations = [equation.subs(base_knowns) for equation in equations]

    sets = (
        sympy_solve(subbed_equations, dict=True)
        if find is None
        else sympy_solve(subbed_equations, find, dict=True)
    )
    count = len(sets)

    if count == 0:
        raise Exception("No solution sets")

    # if count > 1:
    #     raise Exception("More than 1 solution sets")

    solved = {}
    unsolved = {}

    for index, solutions in enumerate(sets):
        for key, value in solutions.items():
            if isinstance(value, Float):
                units = output_units[key] if key in output_units else base_units[key]
                solved[key] = (float(value) * base_units[key]).to(units)
            elif isinstance(value, Mul) or isinstance(value, Add):
                unsolved[key] = value
            else:
                raise Exception(f"Unknown solution type: {type(value)}")

        if len(solved) > 0:
            print(f"Set {index + 1} knowns:")
            print(tabulate(solved.items()), end="\n\n")

        if len(unsolved) > 0:
            print(f"Set {index + 1} unknowns:")
            print(tabulate(unsolved.items()), end="\n\n")

    return solved
