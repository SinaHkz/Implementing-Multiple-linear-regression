import tkinter as tk
from tkinter import ttk
import pandas
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy
import scipy
from matplotlib.figure import Figure

df = pandas.read_csv("MIC.csv")

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


def calculate_output():
    try:
        age = int(age_var.get())
        sex = sex_var.get()
        sex = 1 if sex == "male" else 0
        bmi = float(bmi_var.get())
        children = int(children_var.get())
        smoker = smoker_var.get()
        smoker = 0 if smoker == "no" else 1
        region = region_var.get()
        region_mapping = {
            "northeast": 0,
            "northwest": 1,
            "southeast": 2,
            "southwest": 3
        }
        region_int = region_mapping[region]

        output1 = predict(x, age, sex, bmi, children, smoker, region_int)
        output2 = MSE

        output_var.set(f"Predicted charges: {output1}, MSE: {output2}")
    except ValueError:
        output_var.set("Invalid input, please check your values.")


def display_plot():
    for widget in plot_frame.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(9, 6), dpi=100)

    ax1 = fig.add_subplot(2, 3, 1)
    ax2 = fig.add_subplot(2, 3, 2)
    ax3 = fig.add_subplot(2, 3, 3)
    ax4 = fig.add_subplot(2, 3, 4)
    ax5 = fig.add_subplot(2, 3, 5)
    ax6 = fig.add_subplot(2, 3, 6)

    sns.scatterplot(x='age', y='charges', data=df, ax=ax1)
    ax1.set_title('Age vs Charges')

    sns.boxplot(x='sex', y='charges', data=df, ax=ax2)
    ax2.set_title('Sex vs Charges')

    sns.scatterplot(x='bmi', y='charges', data=df, ax=ax3)
    ax3.set_title('BMI vs Charges')

    sns.boxplot(x='children', y='charges', data=df, ax=ax4)
    ax4.set_title('Children vs Charges')

    sns.boxplot(x='smoker', y='charges', data=df, ax=ax5)
    ax5.set_title('Smoker vs Charges')

    sns.boxplot(x='region', y='charges', data=df, ax=ax6)
    ax6.set_title('Region vs Charges')

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


root = tk.Tk()
root.title("Input Form")

age_var = tk.StringVar()
sex_var = tk.StringVar()
bmi_var = tk.StringVar()
children_var = tk.StringVar()
smoker_var = tk.StringVar()
region_var = tk.StringVar()
output_var = tk.StringVar()

tk.Label(root, text="Age:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=age_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sex:").grid(row=1, column=0, padx=10, pady=5)
ttk.Combobox(root, textvariable=sex_var, values=["male", "female"]).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="BMI:").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=bmi_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Children:").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=children_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Smoker:").grid(row=4, column=0, padx=10, pady=5)
ttk.Combobox(root, textvariable=smoker_var, values=["yes", "no"]).grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Region:").grid(row=5, column=0, padx=10, pady=5)
ttk.Combobox(root, textvariable=region_var, values=["southeast", "southwest", "northeast", "northwest"]).grid(row=5,
                                                                                                              column=1,
                                                                                                              padx=10,
                                                                                                              pady=5)

tk.Button(root, text="Calculate", command=calculate_output).grid(row=6, column=0, columnspan=2, pady=10)

tk.Label(root, text="Output:").grid(row=7, column=0, padx=10, pady=5)
tk.Label(root, textvariable=output_var).grid(row=7, column=1, padx=10, pady=5)

# the frame to hold the plot.
plot_frame = tk.Frame(root)
display_plot()
plot_frame.grid(row=8, column=0, columnspan=2, pady=10, padx=10)

root.mainloop()
