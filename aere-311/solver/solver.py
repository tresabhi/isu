from pint import Quantity
import sympy as sp
from units import output_units, base_units
from tabulate import tabulate
from symbols import *

headers = ["", "Symbol", "Value"]


def solve(equations, knowns, find=None):
    knowns = {
        key: (
            value.to(base_units[key]).magnitude
            if isinstance(value, Quantity)
            else value
        )
        for key, value in knowns.items()
    }

    last_knowns = 0
    subbed_equations = []

    while len(knowns) > last_knowns:
        last_knowns = len(knowns)
        subbed_equations = [equation.subs(knowns) for equation in equations]

        for equation in subbed_equations:
            symbols = equation.free_symbols

            if len(symbols) != 1:
                continue

            [symbol] = symbols
            solution = sp.nsolve(equation, symbol, 1)
            knowns[symbol] = solution

    solved = []

    for symbol, value in knowns.items():
        is_wanted_symbol = find is not None and symbol in find
        icon = "⭐" if is_wanted_symbol else ""

        units = output_units[symbol] if symbol in output_units else base_units[symbol]
        solved.append((icon, symbol, (float(value) * base_units[symbol]).to(units)))

    print("Things I solved for:\n")
    if len(solved) > 0:
        print(tabulate(solved, headers=headers), end="\n\n")

    print("Equations I couldn't solve with ⭐ wanted symbols:\n")
    if find is not None:
        for subbed in subbed_equations:
            symbols = subbed.free_symbols
            has_wanted_symbol = any(symbol in symbols for symbol in find)

            if not has_wanted_symbol:
                continue

            sp.print_jscode(subbed)

    print("\nEquations I couldn't solve without wanted symbols:\n")
    if find is not None:
        for subbed in subbed_equations:
            symbols = subbed.free_symbols
            has_wanted_symbol = any(symbol in symbols for symbol in find)

            if has_wanted_symbol:
                continue

            sp.print_jscode(subbed)

    return solved


# def solve(equations, knowns, find=None):
#     print("Solving...\n")

#     base_knowns = {
#         key: (
#             value.to(base_units[key]).magnitude
#             if isinstance(value, Quantity)
#             else value
#         )
#         for key, value in knowns.items()
#     }
#     subbed_equations = [equation.subs(base_knowns) for equation in equations]

#     for subbed in subbed_equations:
#         print(subbed)

#     sets = (
#         sympy_solve(subbed_equations, dict=True)
#         if find is None
#         else sympy_solve(subbed_equations, find, dict=True)
#     )
#     count = len(sets)

#     if count == 0:
#         raise Exception("No solution sets")

#     # if count > 1:
#     #     raise Exception("More than 1 solution sets")

#     solved = {}
#     unsolved = {}

#     for index, solutions in enumerate(sets):
#         for key, value in solutions.items():
#             if isinstance(value, Float):
#                 units = output_units[key] if key in output_units else base_units[key]
#                 solved[key] = (float(value) * base_units[key]).to(units)
#             elif isinstance(value, Mul) or isinstance(value, Add):
#                 unsolved[key] = value
#             else:
#                 raise Exception(f"Unknown solution type: {type(value)}")

#         if len(solved) > 0:
#             print(f"Set {index + 1} knowns:")
#             print(tabulate(solved.items()), end="\n\n")

#         if len(unsolved) > 0:
#             print(f"Set {index + 1} unknowns:")
#             print(tabulate(unsolved.items()), end="\n\n")

#     return solved
