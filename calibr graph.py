import numpy as np
import matplotlib.pyplot as plt


cm=[0, 0.5, 1]
steps=[0, 100, 200]

plt.plot(cm, steps)

plt.scatter(cm, steps, color='orange', s=40, marker='o')


plt.show()