f = open("c:/jeny/python/lab3/q3/file.txt","a")
f.write("adding more contents")
f.close()
f = open("c:/jeny/python/lab3/q3/file.txt","r")
print(f.read())