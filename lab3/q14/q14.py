with open("c:/jeny/python/lab3/q14/file.txt") as f1, open("c:/jeny/python/lab3/q14/test.txt") as f2:
    for l1,l2 in zip(f1,f2):
        print(l1+l2)