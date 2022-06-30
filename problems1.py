#1
name = input("Enter your name: ")
adress = input("Enter your adress: ")
print(f"name: {name},  adress: {adress}")

#2
name = input("Enter your name")
print("Hello", name)

#3
def area(a,b):
    return a * b 
a = float(input("Enter first number"))
b = float(input("Enter second number"))
print(area(a, b))

#4
def plot_area(a,b):
    return a * b / 43560
a = int(input("Enter first num in acre"))
b = int(input("Enter second num in acre"))
print(plot_area(a, b))

#5
def price(m, n):
    return m * 0.10 + n * 0.25
m = int(input("How much bottles do you have less than 1 liter"))
n = int(input("How much bottles do you have more than 1 liter"))
print(price(m,n))

#6
bill = int(input("Enter the price"))
tax = bill * 18 / 100
tip = (bill - tax) * 20 / 100
print(f"tax: {tax}, tip: {tip}, all: {tax + tip}")

#7
def sum_of_nums(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res
n = int(input("Enter the number"))
print(sum_of_nums(n))

#8
m1 = 75
m2 = 112
n1 = int(input("How much souvinir did u buy"))
n2 = int(input("How much small stones did u buy"))
total_weight = ((m1 * n1) + (m2 * n2))
print(total_weight)

#9
investment = int(input("How much money did you invest"))
def years(investment):
    i = 0
    while i < 3:
        investment = investment + investment * 4 / 100
        print(investment)
        i += 1
years(investment)

#10
a = int(input("Enter 1st number"))
b = int(input("Enter your 2nd number"))
def sum(a, b):
    return a +b
def dif(a, b):
    return a - b
def div(a, b):
  return a / b
def div_whole_part(a, b):
    return a // b
def div_frac(a, b):
    return a % b
def log(a):
    import math
    return math.log10(a)
print(sum(a, b), dif(a, b), div(a, b), div_whole_part(a, b), div_frac(a, b), log(a))

#11
mpg = int(input("Enter mpg: "))
def conv(mpg):
    i = 378.5 / (mpg * 1.609)
    return i
print(conv(mpg))

#12
hight1 = int(input("Enter your high in foots"))
hight2 = int(input("Enter your high in inches"))
def sm_hight(hight1, hight2):
    return hight1 * 12 *2.54 + hight2 * 2.54
print(sm_hight(hight1, hight2))

#13
foot = int(input("enter the distance in foot"))
def conv(foot):
    print(f"inches: {12 * foot}")
    print(f"yards: {1 /3 * foot}")
    print(f"miles: {1 / 5280 * foot}")
conv(foot)

#14
r = int(input("Enter radius of circle"))
import math
area = math.pi * r * 2
volume = (4 / 3) * (math.pi * r ** 3)
print(f"area: {area} volume: {volume}")

#15
h = int(input("Enter hight"))
r = int(input("Enter radius"))
import math
volume = math.pi * r ** 2 * h
print(round(volume, 2))

#16
d = int(input("Enter high by meters"))
v = 0
a = 9.8
import math
speed = math.sqrt(v ** 2 + 2 * a * d)
print(round(speed, 2))

#17
b = int(input("Enter lenght: "))
h - int(input("Enter high: "))
def area(b, h):
    return (b * h) / 2
print(area(b,h))

#18
s1 = int(input("Enter length1: "))
s2 = int(input("Enter length2: "))
s3 = int(input("Enter length3: "))
s = (s1 +s2 + s3) / 2
import math
area = math.sqrt(s * (s - s1) * (s -s2) * (s-s3))
print(area)

#19
day = int(input("Enter days: "))
hour = int(input("Enter hours: "))
minute = int(input("Enter minutes: "))
second = int(input("Enter seconds: "))
days_in_seconds = day * 24 * 60 * 60 
hours_in_seconds = hour * 60 * 60
minutes_in_seconds = minute * 60
in_seconds = days_in_seconds + hours_in_seconds + minutes_in_seconds + second
print(in_seconds)

#20
import time
t = time.localtime()
print(time.asctime(t))

#21
month = input("Enter month name:  ")
if month == "February":
   print("There are 28 or 29 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("There are 31 days")
else:
    print("There are 30 days")

#22
letter = input("Write the letter: ")
if letter == "y":
    print("it can be both: and vowel and consonant")
elif letter in ("a", "e", "i", "o"):
    print("The letter isVowel")
else:
    print("The letter is consonant")

#23
month = input("Enter the month name: ")
day = int(input("Enter day: "))
if month in ("December", "January", "Fabruary"):
    print(f"{month}.{day} is Winter")
elif month in ("March","April", "May"):
    print(f"{month}, {day} is Spring")
elif month in ("June", "July", "August"):
    print(f"{month}. {day} is Summer")
else:
    print(f"{month}.{day} is Autmn")

#25
def celsius():
    i = 0
    while i < 100:
        print(f"{i} - {i * 33.8}")
        i += 10
celsius()

#26
for fizz_buzz in range(0, 100):
    if fizz_buzz % 3 == 0 and fizz_buzz % 5 == 0:
        print("Fizzbuzz")
        continue
    elif fizz_buzz % 3 == 0:
        print("Fizz")
        continue
    elif fizz_buzz % 5 == 0:
        print("Buzz")
        continue
    print(fizz_buzz)























