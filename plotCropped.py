import numpy as np
import matplotlib.pyplot as plt
import math

for name in [f"./{i}mm.csv" for i in range(0,80,10)]:
    data=[]
    lines=[]
    with open(name, 'r') as f:
        lines = [j.strip().split(',') for j in f.readlines()]
        data = np.array([[float(line[0]),float(line[1])] for line in lines])
    # print(data)
    max_x, min_x=0,max(data[:,0])
    for ind in range(len(data[:,0])):
        if data[ind,1] < (min(data[:,1])+10):
            # print(data[ind])
            max_x =max(data[ind,0],max_x)
            min_x =min(data[ind,0],min_x)

    data[:,0]=data[:,0] - ((max_x+min_x)/2)

    new_data=[]
    for i in range(len(data)-1,0,-1):
        if 262 > data[i,0] >= 0:
            new_data.append([-data[i,0],data[i,1]])
        if data[i,1] < 0:
            break
    for i in range(len(new_data)-1,0,-1):
        new_data.append([-new_data[i][0],new_data[i][1]])

    new_data=np.array(new_data)
    V=np.sqrt(-new_data[:,1]*140/(max(new_data[:,1]-173)) + 178)

    # print(new_data)
    plt.plot(new_data[:,0], V,label=name[2:-4])
plt.grid()
plt.legend() 
plt.show()