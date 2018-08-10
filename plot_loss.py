import sys
import numpy as np
import matplotlib.pyplot as plt

f = open(sys.argv[1], "r")
loss_random = f.read().splitlines()
f.close()
loss_random_list = []
for line in loss_random:
    loss_random_list.append(float(line.split()[6]))

f = open(sys.argv[2], "r")
loss_xavier = f.read().splitlines()
f.close()
loss_xavier_list = []
for line in loss_xavier:
    loss_xavier_list.append(float(line.split()[6]))

f = open(sys.argv[3], "r")
loss_orthogonal = f.read().splitlines()
f.close()
loss_orthogonal_list = []
for line in loss_orthogonal:
    loss_orthogonal_list.append(float(line.split()[6]))

plt.plot(np.arange(0, 10000, 10), loss_random_list, 'r', label='Truncated normal')
plt.plot(np.arange(0, 10000, 10), loss_xavier_list, 'b', label='Xavier')
plt.plot(np.arange(0, 10000, 10), loss_orthogonal_list, 'g', label='Orthogonal')
plt.xlabel("step")
plt.ylabel("loss")
plt.legend()
plt.show()
