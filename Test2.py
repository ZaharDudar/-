import numpy as np
import matplotlib.pyplot as plt
import math


for name in [f"./{i}mm.csv" for i in range(0,80,10)]:
    data=[]
    lines=[]
    with open(name, 'r') as f:
        lines = [j.strip().split(',') for j in f.readlines()]
        data = np.array([[float(line[0]), float(line[1])] for line in lines])

    
    V=-data[:,1]*140/(max(data[:,1]-173)) + 178
    
    for i in range (len(V)):
        V[i]=math.sqrt(V[i])
    for i in range (0, (len(V)//2)):
        V[i]=V[len(V)-i-1]
    p=data[:,1]
    x=data[:,0]
    srez=[]
    xsrez=[]
    for i in range (len(p)):
        if p[i]>max(data[:,1])-290:
            srez.append(p[i])
            xsrez.append(x[i])
    ser=(max(xsrez)-min(xsrez))/2
    print(ser)
    

    plt.plot((data[:,0]-ser), V, label=name[2:-4])


plt.xlabel('Положение трубки отноительно центса (мм)')
plt.ylabel('Скорость воздуха (м/с)')
plt.grid()
plt.legend()
plt.show()
