import sys
data = []
counter = 0
for k in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; size in bytes: {1:4d}'.format(a, b))
    data.append(counter)
    counter += 1

print(data)