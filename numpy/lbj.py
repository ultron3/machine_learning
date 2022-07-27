print("hello wolrd")

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

elencogiocatori=[]
elencogiocatori.append("cristiano ronaldo")
elencogiocatori.append("lebron james")
print(elencogiocatori)

lbj= np.array([56,67,89,34,67])        
for i in lbj:
    print(i)

lbj= random.rand()#probabilià che lebron james segni
print("probabilità che lebron james segna un canestro:"+str(lbj))

sns.distplot([56,67,89,34,67])

plt.show()