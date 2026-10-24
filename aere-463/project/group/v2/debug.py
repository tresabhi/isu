import matplotlib.pyplot as plt


def render_airfoil(airfoil):
    coords = airfoil.coordinates

    plt.figure(figsize=(9, 4))
    plt.plot(coords[:, 0], coords[:, 1], "b.-")
    plt.axis("equal")
    plt.xlabel("x / c")
    plt.ylabel("y / c")
    plt.grid(True)
    plt.legend()
    plt.show()


def render_airplane(method):
    method.airplane.draw()
