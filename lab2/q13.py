l = [1,2,3]
l1 = [[]]
for i in range(len(l)+1):
    for j in range (i):
        l1.append(l[j: i])

print("sublist is : ",l1)