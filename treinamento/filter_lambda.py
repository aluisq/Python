

x = range(50)


y = []

for n in filter(lambda x: x%2 ==0, x):
    y.append(n)

print(y)
