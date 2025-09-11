import matplotlib
import numpy

print("matplotlib.__version__:", matplotlib.__version__)
print("numpy.__version__:", numpy.__version__)

print()

print(matplotlib.get_data_path())
print(numpy.get_include())

print()

print(numpy.linspace(0, 10, 11))
