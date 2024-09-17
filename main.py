import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import numpy
import scipy



df = pandas.read_csv("MIC.csv")
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
sns.scatterplot(x='age', y='charges', data=df)
plt.title('Age vs Charges')

plt.subplot(2, 3, 2)
sns.boxplot(x='sex', y='charges', data=df)
plt.title('Sex vs Charges')

plt.subplot(2, 3, 3)
sns.scatterplot(x='bmi', y='charges', data=df)
plt.title('BMI vs Charges')

plt.subplot(2, 3, 4)
sns.boxplot(x='children', y='charges', data=df)
plt.title('Children vs Charges')

plt.subplot(2, 3, 5)
sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Smoker vs Charges')

plt.subplot(2, 3, 6)
sns.boxplot(x='region', y='charges', data=df)
plt.title('Region vs Charges')

plt.tight_layout()

plt.show()


df['sex'] = df['sex'].map({'female': 0, 'male': 1})
df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})
df['region'] = df['region'].map({'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3})

x1 = df["age"]
x2 = df["sex"]
x3 = df["bmi"]
x4 = df["children"]
x5 = df["smoker"]
x6 = df["region"]
y = df["charges"]

auxiliaryArr = [1, x1, x2, x3, x4, x5, x6]

n = len(auxiliaryArr)
a = [[0 for _ in range(n)] for _ in range(n)]
b = [0 for _ in range(n)]

a[0] = [len(x1), numpy.sum(x1), numpy.sum(x2), numpy.sum(x3), numpy.sum(x4), numpy.sum(x5), numpy.sum(x6)]
for i in range(1, n):
    for j in range(n):
        a[i][j] = numpy.sum(numpy.multiply(auxiliaryArr[i], auxiliaryArr[j]))

for i in range(n):
    b[i] = numpy.sum(numpy.multiply(auxiliaryArr[i], y))

x = scipy.linalg.solve(a, b)


def predict(x, x1, x2, x3, x4, x5, x6):
    return x[0] + x[1] * x1 + x[2] * x2 + x[3] * x3 + x[4] * x4 + x[5] * x5 + x[6] * x6


sum = 0
for i in range(len(x1)):
    sum += numpy.pow(y[i] - predict(x, x1[i], x2[i], x3[i], x4[i], x5[i], x6[i]), 2)
MSE = sum / len(x1)

print("predicted data is" , predict(x, 20, 0, 19.46, 0, 1, 3))
inp = input("Do you want to get MSE? (Y/N): ")
if inp.lower() == "y":
    print(MSE)