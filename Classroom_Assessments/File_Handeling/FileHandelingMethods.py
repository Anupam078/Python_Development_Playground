#Question 1:Solution
f=open("archive.dat","ab")
#Question 2:Solution
try:
    f=open("exam.txt","x")
except FileExistsError:
    print("File already exists")
