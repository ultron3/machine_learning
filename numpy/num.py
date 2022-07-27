print("qwe")
import numpy as np
import pandas as pd


arr = np.array([[1,1,1,1],[0,0,0,0],[0,0,0,0],[1,1,1,1]])
for el in arr:
    print(el)


arr = np.array([[0,1,0,1],[0,0,0,0],[0,1,1,0],[1,1,1,1]])
for e in arr:
    print(e)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

from numpy import random

x = random.rand()

print(x)

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])


df = pd.read_csv('data.csv')

print(df.to_string()) 

plt.show()

import numpy
speed=[12,56,78,90]
x=numpy.std(speed)
print(x)














































