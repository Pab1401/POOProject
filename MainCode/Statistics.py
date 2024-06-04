import numpy as np
import pandas as pd
import matplotlib as plt
import random

numbers = []
while True:
    i = input('Is the list full?\n')
    if i == 'y' or i == 'yes':
        break
    else:
        number = int(input('What is the next number?\n'))
        numbers.append(number)

def generate_random_numbers(length, start, end):
    return [random.randint(start, end) for _ in range(length)]

random_numbers = generate_random_numbers(100, 1, 10)
print(random_numbers)
organized = sorted(random_numbers)
print(organized)
        



        

