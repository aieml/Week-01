import numpy as np

a=np.array(([1,2,3],[4,5,6]))

#print(a.shape)

b=np.ones((5,2),dtype=np.int)
#b=np.zeros((5,2),dtype=np.int)

#print(b)

c=np.random.randint(0,5,(4,10))

#print(c)

x=np.random.randint(0,10,(1000,500))
y=np.random.randint(0,10,(500,1000))

#print(x)
#print(y)

z=np.matmul(x,y)

print(z)
