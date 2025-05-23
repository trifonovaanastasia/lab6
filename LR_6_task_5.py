# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hqyJl494SYonzXZimve5QO_pGPMS_5kT
"""



import numpy as np
import neurolab as nl

# Створення матриць для літер Т, А, І (5x5 пікселів)
target = [
    [1, 1, 1, 1, 1,  # Т
     -1, 1, -1, 1, -1,
     -1, 1, -1, 1, -1,
     -1, 1, -1, 1, -1,
     -1, -1, -1, -1, -1],

    [1, 1, 1, -1, 1,  # А
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1,
     1, -1, -1, -1, 1,
     1, 1, 1, 1, 1],

    [1, 1, 1, 1, -1,  # І
     -1, 1, -1, 1, -1,
     -1, 1, -1, 1, -1,
     -1, 1, -1, 1, -1,
     1, 1, 1, 1, -1]
]

chars = ['Т', 'А', 'І']

# Перетворення 0 на -1
target = np.asfarray(target)
target[target == 0] = -1

# Створення та навчання мережі
net = nl.net.newhop(target)

# Тестування на навчальних зразках
output = net.sim(target)
print("Test on train samples:")
for i in range(len(target)):
    print(chars[i], (output[i] == target[i]).all())

# Тестування на букві Т з помилками (деякі пікселі змінені)
print("\nTest on defaced Т:")
test_T = np.asfarray([1, 1, 1, 1, 1,
                      -1, 1, -1, 1, -1,
                      -1, 1, -1, -1, -1,  # Один піксель змінено
                      -1, 1, -1, 1, -1,
                      -1, -1, -1, -1, -1])
test_T[test_T == 0] = -1
out_T = net.sim([test_T])
print((out_T[0] == target[0]).all(), 'Sim. steps', len(net.layers[0].outs))

# Тестування на букві А з помилками
print("\nTest on defaced А:")
test_A = np.asfarray([1, 1, 1, -1, 1,
                      1, -1, -1, -1, 1,
                      1, 1, 1, 1, 1,
                      1, -1, -1, -1, 1,
                      1, 1, 1, 1, 1])
test_A[test_A == 0] = -1
out_A = net.sim([test_A])
print((out_A[0] == target[1]).all(), 'Sim. steps', len(net.layers[0].outs))

# Тестування на букві І з помилками
print("\nTest on defaced І:")
test_I = np.asfarray([1, 1, 1, 1, -1,
                      -1, 1, -1, 1, -1,
                      -1, 1, -1, 1, -1,
                      -1, 1, -1, 1, -1,
                      1, 1, 1, 1, -1])
test_I[test_I == 0] = -1
out_I = net.sim([test_I])
print((out_I[0] == target[2]).all(), 'Sim. steps', len(net.layers[0].outs))