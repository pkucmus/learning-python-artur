import random

if __name__ == '__main__':
    number = random.randint(1,20)
    name = raw_input("What's your name?\n")

    print "Hello {0},".format(name),
    guessedNumber = input('guess the number (between 1 and 20)\n')

    while guessedNumber != number:
        if guessedNumber > number:
            guessedNumber = input('You missed! The number is lower!\n')
        else:
            guessedNumber = input('You missed! The number is higher!\n')
    else:
        print 'Nice one, you have made it!'

    print number, guessedNumber