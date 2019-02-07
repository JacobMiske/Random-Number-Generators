# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:33:15 2019

@author: Jacob Miske
"""
# import libraries
import math #using the floor func
import numpy
import matplotlib.pyplot as plt
hfont = {'fontname':'Helvetica'}

# generate two constants to derive number pattern
A = 1202;
M = 11;

# Q and R represent the fractional ratio and modulus between the two constants
Q = M / A;
R = M % A;

# In order to call 'number' in a recursive statement, a dummy variable is created
number = 1;

# generate a list of all the random numbers in the sequences
random_numbers = []
random_integers = []

# create 100 random number sequences
for i in range(100):
    number = (A*(number%Q))-(R*math.floor(number/Q));
    
    print(number)
    random_numbers.append(number)
    if (number < 0):
        number = number + M;

# break down list of random_numbers into a list of individual random dist
breakdown_list = []
for i in random_numbers:
    if i < 0:
        i = -i
    breakdown_number = [int(n) for n in str(int(i))]
    breakdown_list.append(breakdown_number)
    print(breakdown_number)
# Get the pseudo random list of many digits between 0 and 9 inclusive
breakdown = [j for i in breakdown_list for j in i]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

pseudo_random_mean = mean(breakdown)
print(pseudo_random_mean)

plt.hist(breakdown, bins=10)
plt.title('Histogram of Random Digits', **hfont)
plt.xlabel('Integers'); plt.ylabel('Number of Instances')
plt.show()


    

