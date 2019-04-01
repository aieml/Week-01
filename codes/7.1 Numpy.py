import numpy as np

array=np.random.randint(0,20,(5,10))

print(array)
print('=================================')
#print(array[0:2,3:8])

print(np.sum(array))
print(np.sum(array,axis=0))
print(np.sum(array,axis=1))
print(np.sum(array[2:4,0:5]))
