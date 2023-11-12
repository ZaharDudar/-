import numpy as np
import matplotlib.pyplot as plt


for name in [f"./{i}mm.csv" for i in range(0,10,10)]:
    data=[]
    lines=[]
    with open(name, 'r') as f:
        lines = [j.strip().split(',') for j in f.readlines()]
        data = np.array([[float(line[0]), float(line[1])] for line in lines])
    
    
    acp=[173, max(data[:,1])]
    preasure=[140, 0] #P относительное
    plt.plot(preasure,acp)
    plt.scatter(preasure, acp, color='orange', s=40, marker='o')
    print('P=178-acp*', round(140/(max(data[:,1])-173), 2))


plt.show()
