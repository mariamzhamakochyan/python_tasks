#1
lst = []
lst1 = input("Enter words  ")
while lst1 != "":
    lst.append(lst1)
    lst1 = input("Enter words ")
    if lst1 in lst:
        lst.remove(lst1)
print(lst)

#2
n = int(input("Enter the number "))
def divider(n):
    return [i for i in range(1, n) if n % i == 0]
print(divider(n))

#3
n = int(input("Enter your number "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("True")
else:
    print("False")

#4
def zip(data1, data2):
    data = []
    for i in range(len(data1)):
        data.append(data1[i])
        data.append(data2[i])
    return data
lst1 = [1, 1, 1, 1, 1, 1]
lst2 = [2, 2, 2, 2, 2, 2]
print(zip(lst1, lst2))

#5
s = input("enter your text ")
s = s.lower()
s = s.split(", ")
if s == s[::-1]:
    print("It is palidrome")
else:
    print("It is not palidrome")

#7
from random import sample
num = []
i = 1
while i < 50:
    num.append(i)
    i += 1
num = [int(x)for x in num]
tick = sample(num, 6)
print(sorted(tick))

#8
list = []
res = input("Enter your nums ")
while res != '':
    list.append(res)
    res = input("Enter your nums ")
print(list)
if list == sorted(list):
    print("It is sorted")
else:
    print("Ot is not sorted")














