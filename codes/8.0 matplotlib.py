from matplotlib import pyplot as plt
#pyplot used for plotting graphs
import numpy as np

x=np.arange(0,100,2)    # +1 for numpy
y1=10*x
y2=np.power(x,2)

plt.plot(x,y1,'r+')
plt.plot(x,y2,'g.')

plt.show()
