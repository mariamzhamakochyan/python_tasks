def max(data):
    i = 1
    max1 = data[0]
    while i < len(data):
        if data[i] > max1:
            max1 = data[i]
        i +=1
    return max1
print(max(data))
