# Linear Regression

## Introduction
Nowadays artificial intelligence is a part of our life and lots of tasks can be done quickly and easily with AI powered devices. There are lots of methods to equip machines and softwares to predict an event based on the previous experiences that we provided.

## What is Regression?
One of the most useful and powerful tools to train a model is regression. In this method we provide a data set and train a model based on its formulation to equip the program. Its formulation provides a function based on independent variables to predict the dependent variable.

## Linear Regression
Linear regression is a subset of Regression methods. It just use the linear relation between dependent and independent variable means if 𝑥1, 𝑥2, ... , 𝑥𝑛 are independent variable and 𝑦 is dependent there is a relation between them like below:

<img width="371" alt="Screenshot 2024-09-18 at 7 15 43 PM" src="https://github.com/user-attachments/assets/1c08a165-c122-4dda-a0b4-d6adc1e158d7">

Linear Regression has these types:

1. Simple linear regression
2. Multiple linear regression

### 1. Single linear regression
Single regression is an analysis for those models that contains only one independent variable and have the form like below:

<img width="298" alt="Screenshot 2024-09-18 at 7 17 49 PM" src="https://github.com/user-attachments/assets/e9039e9c-4bbc-4ce3-821e-a50a4636af00">

This line equation must represent a line with the least amount of ∑ (𝑦𝑖 − 𝑦𝑖) that 𝑦𝑖 is the exact value and 𝑦^ is the predicted value of the same input.

Given S as shown below:

<img width="312" alt="Screenshot 2024-09-18 at 7 19 22 PM" src="https://github.com/user-attachments/assets/a53c4665-b0a8-4d22-8315-9210495d79bb">

To evaluate the global minimum of S:

<img width="542" alt="Screenshot 2024-09-18 at 7 19 43 PM" src="https://github.com/user-attachments/assets/dfb43dbe-d94d-4a7a-bf96-49b9f3d28c78">

This is a linear system with two variables 𝑎0 and 𝑎1. by solving this system we get this formulation for slope and intercept:

<img width="241" alt="Screenshot 2024-09-18 at 7 20 04 PM" src="https://github.com/user-attachments/assets/6c1e2a4f-0686-452f-b434-42fcba6608ed">

### 2. Multiple linear regression
If a data set contains more than one independent variable we must use this method that is an extension of single linear regression. Assume that we have two independent variable, the equation is shown below:

<img width="314" alt="Screenshot 2024-09-18 at 7 20 32 PM" src="https://github.com/user-attachments/assets/38a6e70c-9e25-4532-aca7-27e0e664d699">

To find the optimal slopes and intercept use previous procedure as below:

<img width="593" alt="Screenshot 2024-09-18 at 7 20 53 PM" src="https://github.com/user-attachments/assets/d2f8ea32-0686-4d54-a7c4-0b0e27258487">

By simplifying this linear system this formulations be yielded:

<img width="628" alt="Screenshot 2024-09-18 at 7 21 11 PM" src="https://github.com/user-attachments/assets/34e0ada2-c19b-42df-bd14-9c9aaf479ded">

Now we can use the Gauss-elimination method to find the slopes and intercept. 

Coefficient matrix has a sequence that we can use to generate it for any amount of independent variables.

<img width="817" alt="Screenshot 2024-09-18 at 7 21 18 PM" src="https://github.com/user-attachments/assets/c9038e53-05eb-4f77-9f4b-c493f6747bac">

This formulation will work for every possible amount of independent variable and one dependent variable.


## Condition for applying linear regression
1. **Linearity**: The relationship between the independent and dependent variable should be linear. It means that if the relation is not linear the model will predict an ineligible data

2. **Independence**: Observations should be independent of each other, meaning that the independent variables must not have any relation with each other.

## Conclusion
Linear Regression is one the most powerful methods to predict something depending on different situations, keep in mind that linear regression is a good method when the relation between dependent and independent variables is somehow linear like car price that is dependent on its power.
