from random import randint

rand=randint(1,55)
counter=0

while True:
    counter+=1 #to count how many guesses you made

    number=int(input("Enter values ​​between 1 and 55 (0 output):"))
    if number==0:
        print("You Canceled the Game")
        break

    elif number<rand:
        print("Enter a Higher Number.")
        continue

    elif number>rand:
        print("Enter a Lower Number.")
        continue

    else:
        print("Randomly selected number : {} ".format(rand))
        print("Your number of guesses : {} ".format(counter)) #number of guesses we made



