import numpy as np
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[7,8],[10,11]])

arr3 = np.hstack((arr1,arr2))
print(arr3,'\n\n')
print(np.hsplit(arr3,2),'\n\n')
arr3 = np.vstack((arr1,arr2))
print(arr3,'\n\n')
arr3 = np.dstack((arr1,arr2))
print(arr3,'\n\n')

arr3 = np.concatenate((arr1,arr2),axis=0)
print(arr3,'\n\n')
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3,'\n\n')

