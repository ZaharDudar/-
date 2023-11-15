import numpy as np
import matplotlib.pyplot as plt
import math

Q=[]
for name in [f"./{i}mm.csv" for i in range(0,80,10)]:
    data=[]
    lines=[]
    with open(name, 'r') as f:
        lines = [j.strip().split(',') for j in f.readlines()]
        data = np.array([[float(line[0]),float(line[1])] for line in lines])
        
    V=-data[:,1]*140/(max(data[:,1]-173)) + 178
    for i in range (len(V)):
        V[i]=math.sqrt(V[i])
    data[:,1]=V
    
    #print(data)
    max_x, min_x=0,max(data[:,0])
    for ind in range(len(data[:,0])):
        if data[ind,1] > (max(data[:,1])-10):
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
    # print(new_data)
    new_data[:,0]=new_data[:,0]/20
    x=new_data[:,0]
    p=new_data[:,1]
    q=0
    counter=0
    
    for zxc in range (len(x)-1):
        q=abs((x[zxc]*p[zxc]/1000+x[zxc+1]*p[zxc+1]/1000)*(x[zxc+1]-x[zxc])/1000)
        counter=counter+q
        q=0
        
    counter*=2.6*0.5*1000
    print(counter)
    Q.append(counter)
X=[0, 10 , 20, 30 , 40 , 50, 60, 70]
plt.plot(X, Q, label='Расход Q(0-70мм)')
plt.scatter(X, Q, color='orange', s=40, marker='*')

plt.grid()
plt.legend()
plt.xlabel('Положение трубки отноительно центра (мм)')
plt.ylabel('Расход воздуха (г/с)')
plt.show()