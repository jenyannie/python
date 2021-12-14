str = input ("enter a string: ")
char = input ("enter any character in the string: ")
length = len(str)
count = 0
for i in range(length):
    if char ==str[i]:
        count += 1
print("occurance of given character is: ",count)