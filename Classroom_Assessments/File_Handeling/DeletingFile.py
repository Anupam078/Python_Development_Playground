import os
if os.path.exists("Temp.txt"):
    os.remove("Temp.txt")
else:
    print("The file does not exist")