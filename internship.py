#1 - arithmetic operations
'''
num1 = int(input("first number: "))
num2 = float(input("input decimal: "))

num3 = num1 + num2
print(f"Sum: {num3}")

#2 - times table of a number from 1 to the number

number = int(input("Number: "))
for x in range(number + 1):
    print(f"{number} x {x} = {number * x}")
'''    

#3 - prices of fruit per kg

fruits = {'apple': 50, 
          'banana': 30, 
          'citrus' : 70, 
          'dragonfruit': 100} # prices for 1 kg of fruit

total_price = 0
allowed_options = ['apple', 'banana', 'citrus', 'dragonfruit', 'quit']


fruit = ''
while True:  
    fruit = input("Fruit: ").lower()
    while fruit not in allowed_options:
        print("Not allowed")
        fruit = input("Fruit: ").lower()
    
    if fruit == 'quit':
        print(total_price)
        break
    
    weight = float(input("Weight (kg): "))
    price = fruits[fruit] * weight
    total_price += price


#4 - area of circle / semicircle
import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def radius_of_circle(area):
    return math.sqrt(area / math.pi)

def area_of_semicircle(radius):
    return (math.pi * (radius ** 2)) / 2

def radius_of_semicircle(area):
    return math.sqrt((2 * area) / math.pi)

area_of_circle(5)
radius_of_circle(78.54)
area_of_semicircle(78.54)
radius_of_semicircle(39.27)





#5 - multiplication of matrices
import numpy as np

# 1x2 * 2x2 matrix multiplication
m1 = np.array([2, 2])
m1 = m1.reshape(1, 2)

m2 = np.array([3, 4, 4, 1])
m2 = m2.reshape(2, 2)

# multiply matrices
m3 = np.dot(m1, m2)
m3 = m3.reshape(2, 1)
print(m3)

# 2x2 * 2x2 matrix multiplication

m4 = np.array([6, 7, 6, 7])
m4 = m4.reshape(2, 2)

m5 = np.array([1, 0, 0, 1])
m5 = m5.reshape(2, 2)

id_result = np.dot(m4, m5)
id_result = id_result.reshape(2, 2)
print(id_result)
