f = open("c:/jeny/python/lab3/q16/file.txt","r")
contents = f.readlines()
# print(contents)
contents = [i.strip("\n") for i in contents]
print(contents)