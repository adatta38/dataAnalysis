import numpy as np

filename = 'iris.data'

data = np.loadtxt(filename, delimiter=',')

print(data)
