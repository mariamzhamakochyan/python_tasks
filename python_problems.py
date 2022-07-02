#1
num = int(input("Enter your nums "))
print(str(num)[::-1])

#3
list = []
num = int(input("Enter the numbers "))
while num != '':
    list.append(num)
    num = input()
n = max(list)
m = min(list)
print(m + n)

#9
from random import randint
min_ASCII = 33
max_ASCII = 126
def random_passwd():
    random_length = randint()
    res = ""
    for i in range(random_length):
        random_char = chr(randint(min_ASCII, max_ASCII))
        res = res + random_char
    return res
print(f"passwd: , {random_passwd()}")

#6
def smallest_prime(n):
    if k > n:
        for i in range(n+1, k):
            if k % i == 0:
                break
            else:
                return k

#7
def get_median(data):
    if len(data) % 2 != 0:
        m = int((len(data) + 1 / 2) - 1)
        return data[m]
    else:
        m1 = int((len(data) / 2) - 1)
        m2 = int(len(data) / 2)
        return (data[m1] + data [m2]) / 2
data = [1, 2, 3]
print(get_median(data))


#4
list = []
num = int(input("Enter your numbers: "))
while num != "":
    list.append(num)
    num = input()
    lst1 = []
    for i in list:
        if i % 2 == 0:
            lst1.append(list[i])
    print(lst1)

#5
str = input("Enter your word: ")
str1 == str[::-1]
print(str1)

