# -*- coding: utf-8 -*-
"""BelajarPython3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AvudUb2iwXfvcmSdN-U5wc1Y7NMemgI0

**Belajar Python 3**
"""

# Cetak dengan baris baru
print('di bawah ini: Cetak dengan baris baru')
print('Hello')
print('World!')

# Cetak tanpa baris baru
print('di bawah ini: Cetak dengan baris baru')
print('Hello', end=' ')
print('World!')

# Variabel
print('di bawah ini: Variabel')
x = 1
print(x)
x = 5
print(x)
x = 'Ini Variabel'
print(x)

# Operasi matematika
print('di bawah ini: Operasi matematika')
print(10 * 6)
print(10 / 6)
print(10 // 6)
print(10 + 6)
print(10 - 6)
print(10 % 6)

# Perulangan
print('di bawah ini: Perulangan 1 parameter')
for i in range(2):
  print(i)
print('di bawah ini: Perulangan 2 parameter')
for i in range(2, 4):
  print(i)

# Pengkondisian
print('di bawah ini: Pengkondisian')
if (1 + 2) == 4:
  print('Benar')
else:
  print('Salah')

# Pengkondisian dengan boolean
print('di bawah ini: Pengkondisian dengan boolean')
if(2 - 1) == 1 and (3 % 2) == 1:
  print('Benar')
else:
  print('Salah')

# Fungsi
print('di bawah ini: Fungsi')
def greet(name):
  print('Hello {}'.format(name))

greet('Ibnu')

