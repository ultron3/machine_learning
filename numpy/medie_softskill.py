import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
x = np.array(["savin","crosetti","morini","goncalves","d'ancelli","de paoli","tarantino","cantavenera"])
y = np.array([3.7,4.5,4,3.7,4.3,3.8,3.7,4])

plt.plot(x, y)

plt.xlabel("candidati")
plt.ylabel("medie_punteggi")

plt.show()

df = pd.read_csv('softskill.csv')

print(df.to_string()) 

plt.show()












