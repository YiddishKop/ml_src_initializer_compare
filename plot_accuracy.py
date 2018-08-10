import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1], "r")
accuracy_random = f.read().splitlines()
f.close()
accuracy_random_list = []
for line in accuracy_random:
    accuracy_random_list.append(float(line.split()[6]))

f = open(sys.argv[2], "r")
accuracy_xavier = f.read().splitlines()
f.close()
accuracy_xavier_list = []
for line in accuracy_xavier:
    accuracy_xavier_list.append(float(line.split()[6]))

f = open(sys.argv[3], "r")
accuracy_orthogonal = f.read().splitlines()
f.close()
accuracy_orthogonal_list = []
for line in accuracy_orthogonal:
    accuracy_orthogonal_list.append(float(line.split()[6]))

plt.plot(np.arange(0, 10000, 1000), accuracy_random_list, 'r', label='Truncated normal')
plt.plot(np.arange(0, 10000, 1000), accuracy_xavier_list, 'b', label='Xavier')
plt.plot(np.arange(0, 10000, 1000), accuracy_orthogonal_list, 'g', label='Orthogonal')
plt.xlabel("step")
plt.ylabel("accuracy")
plt.legend()
plt.show()
