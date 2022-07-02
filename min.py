def min(data):
    i = 1
    min1 = data[0]
    while i < len(data):
        if data[i] < min1:
            min1 = data[i]
        i += 1
    return min1
print(min(data))
