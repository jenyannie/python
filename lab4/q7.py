n = int(input("enter a number: "))
def sum(n):
    if(n<=0):
        return 0
    else:
        return n +sum(n-2)

print(sum(n))