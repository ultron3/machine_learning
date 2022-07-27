import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("malattie.csv")

print(df)


features = ['covid', 'vaiolo-scimmie', 'influenza']

X = df[features]
y = df['covid']

print(X)
print(y)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mymalattie.png')

img=pltimg.imread('mymalattie.png')
imgplot = plt.imshow(img)
plt.show()









