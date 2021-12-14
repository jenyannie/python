f = open("c:/jeny/python/lab3/q8/file.txt","r")
words = f.read().split()
max_length_word = max(words,key=len)
print("maximum length word in the file is: ",max_length_word)