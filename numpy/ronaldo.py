print("hello wolrd")

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


elencogiocatori=[]
elencogiocatori.append("cristiano ronaldo")
elencogiocatori.append("lebron james")
print(elencogiocatori)

cr7= np.array([12,45,67,89,56])
for y in cr7:
    print(y)

cr7 = random.rand() #probabili√† che ronaldo segni
print("probabili√† che ronaldo segni:"+str(cr7))

sns.distplot([12,45,67,89,56])

plt.show()









