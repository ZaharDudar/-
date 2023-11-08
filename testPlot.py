import numpy as np
import matplotlib.pyplot as plt


for name in [f"./{i}mm.csv" for i in range(0,80,10)]:
    data=[]
    lines=[]
    with open(name, 'r') as f:
        lines = [j.strip().split(',') for j in f.readlines()]
        data = np.array([[float(line[0]),900-float(line[1])] for line in lines])
    print(lines)
    plt.plot(data[:,0], data[:,1],label=name)
plt.grid()
plt.legend()
plt.show()