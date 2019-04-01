from matplotlib import pyplot as plt
import numpy as np

x=np.arange(0,2*np.pi,0.2)

y1=np.sin(x)
y2=np.cos(x)

plt.plot(x,y1,'r--',label='sin(x)')
plt.plot(x,y2,'g+',label='cos(x)')

plt.xlabel('x values (rads)')
plt.ylabel('sin(x) and cos(x)')

plt.title('sin(x) cos(x)')

plt.savefig('mygraph.png')

plt.legend()

plt.show()
