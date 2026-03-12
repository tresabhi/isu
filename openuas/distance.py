true_min = 1
true_max = 2

width = 0.3
padding = width * 3 / 2
gap = width / 4

x1_min = true_min - padding + width / 2
x1_max = true_max + padding + width / 2

x2_min = true_min - padding - width / 2
x2_max = true_max + padding - width / 2

print(f"x1_min = {x1_min}")
print(f"x1_max = {x1_max}")
print(f"x2_min = {x2_min}")
print(f"x2_max = {x2_max}")
