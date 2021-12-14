import random
number = random.randint(1,9)
# print(number)
guess = input("enter a number between 1 and 9: ")
print("random number generated is {}". format(number))
count = 0
guess = int(guess)
count +=1
if guess < number:
    print("guessed too low")
elif guess > number:
    print("guessed too high")
else:
    if count == 1:
        print("got it right")

