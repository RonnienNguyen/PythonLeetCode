a = []

for i in range (0, 1000):
    if (i%8==0) and (i%5 != 0):
        a.append(str(i))
print(' , '.join(a))