print("Options: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10")
user = input("What problem do you want to run?: ")
user = int(user)
if user == 1:
    print("Running problem 1")
    for numbers in range(1, 1001):
        print(numbers)
elif user == 2:
    print("Running Problem 2")
    for numbers in range(1, 1001, 2):
        if numbers % 3 != 0:  # != is not divisable by 3
            print(numbers)
elif user == 3:
    print("Running Problem 3")
    for numbers in range(1, 1001):
        if numbers % 3 == 0:  # == is is divisable by 3
            print(numbers)
elif user == 4:
    print("Running Problem 4")
    for numbers in range(1, 1001):
        if numbers % 3 == 0 or numbers % 5 == 0:
            print(numbers)
elif user == 5:
    print("Running Problem 5")
    user = int(input("Enter a number: "))
    if user > 200:
        print(input("Try again: "))
    for numbers in range(1, 1001):
        if numbers % 11 == 0 or numbers % 13 == 0:
            print(numbers)
elif user == 6:
    print("Running Problem 6: ")
    word = input("Enter a word: ")
    for achar in word:
        print(achar)
elif user == 7:
    print("Running Problem 7: ")
    word = input("Enter a word: ")
    if len(word) > 10:
        for achar in word[0::2]:
            print(achar)

    else:
        print("Try Again!")
        newWord = input("Word has to be more than 10 letters: ")
        if len(newWord) > 10:
            for achar in newWord[0::2]:
                print(achar)
elif user == 8:
    print("Running Problem 8: ")
    import random
    dice1 = 0
    dice2 = 0
    dice3 = 0
    dice4 = 0
    dice5 = 0
    dice6 = 0
    for i in range(1, 1001):
        diceRoll = random.randrange(1, 7)
        if diceRoll == 1:
            dice1 += 1
        elif diceRoll == 2:
            dice2 += 1
        elif diceRoll == 3:
            dice3 += 1
        elif diceRoll == 4:
            dice4 += 1
        elif diceRoll == 5:
            dice5 += 1
        elif diceRoll == 6:
            dice6 += 1
    print("1 was rolled", f'{dice1}', "times")
    print("2 was rolled", f'{dice2}', "times")
    print("3 was rolled", f'{dice3}', "times")
    print("4 was rolled", f'{dice4}', "times")
    print("5 was rolled", f'{dice5}', "times")
    print("6 was rolled", f'{dice6}', "times")

elif user == 9:
    print("Running Problem 9: ")
    userinput = int(input("Enter a number: "))
    if userinput == 1:
        print("Your number is NOT a prime number!")
    elif userinput > 1:
        # checking for factors
        for i in range(2, userinput):
            if (userinput % i) == 0:
                print("Your number is NOT a prime number!")
                print(i, "times", userinput//i, "is", userinput)
                break
        else:
            print("YAY! your number is a prime number!")
    else:
        print(userinput, "is NOT a prime number!")
elif user == 10:
    print("Running Problem 10: ")
    lower = 1
    upper = 1000

    print("The prime numbers between", lower, "and", upper, "are: ")

    for numbers in range(lower, upper + 1):
        # Prime numbers are greater than 1
        if numbers > 1:
            for i in range(2, numbers):
                if (numbers % i) == 0:
                    break
            else:
                print(numbers)
