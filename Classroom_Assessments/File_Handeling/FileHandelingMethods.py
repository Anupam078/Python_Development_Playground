#Question 1:Solution
f=open("archive.dat","ab")
#Question 2:Solution
try:
    f=open("exam.txt","x")
except FileExistsError:
    print("File already exists")

#Question 1:Solution
with open("data.txt","r") as file:
    line_list=file.readlines()
    print(line_list[0],line_list[1])

#Question 2:Solution
f=open("log.txt","r")
Status=f.read(4)
print(Status)
Var2=f.read(5)
print(Var2)
f.close()


#Question 1:Solution
with open("students.txt","a") as f:
    f.write("\nEmma")

#Question 2:Solution
import os
if(os.path.exists("temp.txt")):
    os.remove("temp.txt")
    print("Delete")
else:
    print("Not Found")

