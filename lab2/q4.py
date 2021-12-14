str = input ("enter a string: ")
length = len(str)
print("No of repeated characters")
for i in range(0,length):
    count = 1
    for j in range(i+1, length):
        if (str[i] == str[j] and str[i] != ''):
            count +=1
            str = str[:j] + '0' + str[j+1:]
    if count >1 and str[i] != '0':
        print(str[i],"-", count)


