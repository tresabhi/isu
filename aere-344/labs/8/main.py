import csv
import numpy as np

xs_in = list(range(10)) + list(range(10, 65 + 5, 5))
u_inf = 13

for x_in in xs_in:
    path = f"data/{x_in}in.csv"

    with open(path) as file:
        reader = csv.reader(file)

        chunk1, chunk2, chunk3 = [np.array([0.0] * 16) for _ in range(3)]
        n = 0

        for row in reader:
            row = [float(cell) for cell in row]

            chunk1_i = np.array(row[2:18])
            chunk2_i = np.array(row[36:52])
            chunk3_i = np.array(row[70:86])

            chunk1 += chunk1_i
            chunk2 += chunk2_i
            chunk3 += chunk3_i

            n += 1

        chunk1 /= n
        chunk2 /= n
        chunk3 /= n

        # print(chunk1)
        # print(chunk2)
        # print(chunk3)
