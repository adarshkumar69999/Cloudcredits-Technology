import random
def main():
    print("........................")
    print("Welcom to Guess a number Game ")
    print("instruction : \n To start this game you have to mention a range in which you will guess the number ")
    a,b=eval(input("Enter the two numbers Of the range separated by comma = "))
    num=randomNumber(a,b)
    guess=0
    while num!=guess:
        guess=int(input("Now Guess the Number from your given range :- "))
        if guess!=num:
            print("Guess again !!!")
    print("Correct guess")


def randomNumber(a,b):
    return random.randint(a,b)
main()