import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("selezioni.csv")

print(df)

features = ['interesse','sesso','distanza','scolarita','iscritto']

X = df[features]
y = df['distanza']

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('grafico.png')

img=pltimg.imread('grafico.png')
imgplot = plt.imshow(img)
plt.show()
