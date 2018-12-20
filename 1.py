a = [1, 2, '+', 2, 5]
ind = a.index('+')
b = int(''.join(a[(ind + 1):]))
c = a[:ind]
print(b, c)