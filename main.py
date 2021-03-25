# Zad. 1
import numpy as np

a = np.arange(3).reshape(1, 3)
b = np.arange(3, 6).reshape(1, 3)
a = a * 4
b = b * 12
c = a * b
print(a)
print(b)
print(c)

# Zad. 2
import numpy as np

a = np.array([5, 10, 1, 6, 7, 9, 10, 21, 3]).reshape(3, 3)
b = np.array([0, 20, 3, 121, 442, 1, 2, 82, 21, 22, 1, 22, 124, 4, 2, 1]).reshape(4, 4)

print("Wartosci minimalne (kolumny): ")
print(f"a: {a.min(axis=0)}")
print(f"b: {b.min(axis=0)}")
print("Wartości minimalne (wiersze): ")
print(f"a: {a.min(axis=1)}")
print(f"b: {b.min(axis=1)}")
print("Wartosci maksymalne (kolumny): ")
print(f"a: {a.max(axis=0)}")
print(f"b: {b.max(axis=0)}")
print("Wartości maksymalne (wiersze): ")
print(f"a: {a.max(axis=1)}")
print(f"b: {b.max(axis=1)}")

# Zad. 3
import numpy as np

a = np.arange(3).reshape(1, 3)
b = np.arange(3, 6).reshape(3, 1)
c = b.dot(a)
print(c)

# Zad. 4
import numpy as np

a = np.array([-10, -5, 5])
b = np.array([-10.3, -5, 20.2])
a = a * 11
b = b * 22
c = a * b
print(a)
print(b)
print(c)

# Zad. 5
import numpy as np
import math as m
mat = np.array([5, 2.5, 0.4, 10, 22, 1]).reshape(2, 3)
a = np.array([m.sin(x) for x in mat.flat]).reshape(2, 3)
print(mat)
print(a)

# Zad. 6
import numpy as np
import math as m

mat = np.array([4, 2, 1, 10, 15, 27]).reshape(2, 3)
b = np. array([m.cos(x) for x in mat.flat]).reshape(2, 3)
print(mat)
print(b)

# Zad. 7
import numpy as np
import math as m

mat1 = np.array([5, 2.5, 0.4, 10, 22, 1]).reshape(2, 3)
a = np.array([m.sin(x) for x in mat1.flat]).reshape(2, 3)

mat2 = np.array([4, 2, 1, 10, 15, 27]).reshape(2, 3)
b = np. array([m.cos(x) for x in mat2.flat]).reshape(2, 3)

apb = a + b
print(apb)

# Zad. 8
import numpy as np

a = np.array([np.random.randint(0, 50) for x in range(9)]).reshape(3, 3)

for x in a:
    print(x)
    print("\n")

# # Zad. 9
import numpy as np

a = np.array([np.random.randint(0, 50) for x in range(9)]).reshape(3, 3)

for x in a.flat:
    print(x)

# Zad. 10
import numpy as np

a = np.array([np.random.randint(0, 100) for x in range(81)]).reshape(9, 9)
a = a.reshape(1, 81)
print(a)
a = a.reshape(81, 1)
print(a)

Odp.: Liczba elementow w tablicy wynosi 81 (wiersze * kolumny), wiec mozemy zmienic jej ksztalt na np. 1x81 lub 81x1. Iloczyn kolumn i wierszy musi byc rowny ilosci elementow w macierzy.

# Zad. 11
import numpy as np

tab = np.array([np.random.randint(0, 50) for x in range(12)]).reshape(1, 12)
print(tab)
a = tab.reshape(3, 4)
b = tab.reshape(4, 3)
c = tab.reshape(2, 6)
print("3x4: ")
print(a)
print("4x3: ")
print(b)
print("2x6: ")
print(c)

# Odp.: Macierze zawieraja te same elementy tylko inaczej poukladane.
