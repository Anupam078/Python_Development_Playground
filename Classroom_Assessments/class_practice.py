for i  in range(6,1,-1):
    for j in range (i):
        print(j, end=" ")
    print()

print()

x=0
for i in range(1,10):
    if i % 2 != 0:
        x=x+1
        for j in range(x):
            print(i, end=" ")
    else:
        print()

print()
n = 4
num = 1
for i in range(1, n + 1):
    start = num + i - 1
    for j in range(start, num - 1, -1):
        print(j, end=" ")
    print()
    num += i

print()
for i in range (0,6):
    for j in range (i):
        print(" ",end="")
    for j in range(6-i):
        print("*",end="")
    print()

print()
rows=8
for i in range (0,rows+1):
    for j in range(rows+1-i):
        print("*",end="")
    for K in range(i*2):
        print(" ",end="")
    for j in range(rows+1-i):
        print("*",end="")
    print()

print()
for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

n = 7

for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()


name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

print(float(22//3+3/3))