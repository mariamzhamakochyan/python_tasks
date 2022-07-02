def pop(data, i):
    if i ==  None:
        result = data[len(data) - 1]
        del data[len(data) - 1]
    elif i > 0 and i < len(data):
        result = data[index]
        del data[index]
    else:
        raise IndexError
    return result
