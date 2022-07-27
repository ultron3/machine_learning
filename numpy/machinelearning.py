import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import  r2_score
import numpy
import matplotlib.pyplot as plt
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def predice(x):
  return slope * x + intercept

mymodel = list(map(predice, x))
anni=input("anni auto: ")
print("macchina di dieci anni:",predice(int(anni)))
print("r:", r, "p:", p, "std_err:",std_err)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()



z = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
w = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(z, w, 3))
print("codice  relazione 3: ",r2_score(w,mymodel(z)))
mymodel = numpy.poly1d(numpy.polyfit(z, w, 4))
print("codice  relazione 4:  ",r2_score(w,mymodel(z)))
mymodel = numpy.poly1d(numpy.polyfit(z, w, 5))
print("codice  relazione 5: ",r2_score(w,mymodel(z)))


myline = numpy.linspace(1, 22, 100)


plt.scatter(z, w)
plt.plot(myline, mymodel(myline))
plt.show()


df = pandas.read_csv("cars.csv")

px = df[['Weight', 'Volume']]
py = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(px, py)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
peso=2300;
volume=1300;
co2=regr.coef_[0]*peso+regr.coef_[1]*volume+regr.intercept_;
print(co2)
print(predictedCO2)


scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()

