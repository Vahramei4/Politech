arr = [124, 1245, 1256, 6123, 1, 35, 16, 152, 67, 437]

N = len(arr)
i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1

print(arr)
