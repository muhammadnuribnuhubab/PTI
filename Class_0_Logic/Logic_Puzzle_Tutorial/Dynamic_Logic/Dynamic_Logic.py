# -*- coding: utf-8 -*-
"""Dynamic_Logic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AvudUb2iwXfvcmSdN-U5wc1Y7NMemgI0

# **Dynamic Logic**
"""

print('==== DYNAMIC LOGIC ====')
print('!!! Berapapun Angkanya Logic Harus Tetap Sama !!!')
print('\n')

print('1. Memakan Variabel')
SIZE = 10

for row in range(1, SIZE):
  for col in range(1, SIZE):
    print('*' if((row == col) or (row + col == SIZE)) else ' ', end = '')
  print()
print('\n')


print('2. Memakai Fungsi')
def print_x(n):
  n = n if n % 2 == 0 else n + 1 # !!! Berapapun Angkanya Logic Harus Tetap Sama !!!
  for row in range(1, n):
    for col in range(1, n):
      print('*' if((row == col) or (row + col == n)) else '-', end = '')
    print()

print_x(10)

