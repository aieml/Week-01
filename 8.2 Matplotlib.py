import numpy as np

x=np.arange(0,100,1)
y=np.random.randint(0,100,(100))

from matplotlib import pyplot as plt

plt.scatter(x,y)

plt.show()
