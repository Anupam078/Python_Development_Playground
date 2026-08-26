str=input()
upperCount = 0
lowerCount = 0
for i in str:
    if i.isupper():
        upperCount += 1
    elif i.islower():
        lowerCount += 1

print("Number of uppercase letters:", upperCount)
print("Number of lowercase letters:", lowerCount)