arr = [124, 1245, 1256, 6123, 1, 35, 16, 152, 67, 437]

min = arr[0]
minI = 0
i = 0
for elem in arr:
    if elem < min:
        min = elem
        minI = i
    i += 1

print('min: ', min)
print('index: ', minI)
