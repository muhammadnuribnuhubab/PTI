# -*- coding: utf-8 -*-
"""Logic-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AvudUb2iwXfvcmSdN-U5wc1Y7NMemgI0

# **Logic 2**
"""

print('==== LOGIC 2 ====')
print()

SIZE = 9

print('Soal 1')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print((row + col - 1) if (row == col) else ' ', end='')
    print()
print()

print('Soal 2')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print(((col * 2) - 2) if (row + col == SIZE + 1) else ' ', end='')
    print()
print()

print('Soal 3')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        if(row == col):
          print((row + col - 1), end = '')
        elif(row + col == SIZE + 1):
          print(((col * 2) - 2), end = '')
        else:
          print(' ', end = '')
    print()
print()

print('Soal 4')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        if(row == col):
          print((row + col - 1), end = '')
        elif(row + col == SIZE + 1):
          print(((col * 2) - 2), end = '')
        elif(row == 5):
          print(((col * 2) - 2), end = '')
        elif(col == 5):
          print(((row * 2) - 1), end = '' )
        else:
          print(' ', end = '')
    print()
print()

print('Soal 5')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print(((col * 2) - 1) if (row >= col) else ' ', end='')
    print()
print()

print('Soal 6')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        print(((SIZE - row) * 2) if (row + col >= SIZE + 1) else ' ', end='')
    print()
print()

print('Soal 7')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        if(row == col):
          print((row + col - 1), end = '')
        elif(row + col == SIZE + 1):
          print(((col * 2) - 2), end = '')
        elif(row <= col and row + col <= SIZE + 1):
          print('A', end = '')
        elif(row >= col and row + col >= SIZE + 1):
          print('B', end = '')
        else:
          print(' ', end = '')
    print()
print()

print('Soal 8')
print()
for row in range(1, SIZE + 1):
    for col in range(1, SIZE + 1):
        if(row == col):
          print((row + col - 1), end = '')
        elif(row + col == SIZE + 1):
          print(((col * 2) - 2), end = '')
        elif(row >= col and row + col <= SIZE + 1):
          print('A', end = '')
        elif(row <= col and row + col >= SIZE + 1):
          print('B', end = '')
        else:
          print(' ', end = '')
    print()
print()