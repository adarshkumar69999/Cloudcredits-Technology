import random
def main():
    print("Welcome to Dice Simulator Game \n ")
    a=int(input("Enter how many dices you want to draw :- "))
    print("Total number of Random Dices Simulated will be :- ",a)
    for i in range(1, a + 1):
        print(f"{i}. Dice draw is:", end=" ")
        draw = diceSimulator()
        print(draw)

def diceSimulator():
    choices=[1,2,3,4,5,6]
    result=random.choice(choices)
    return result

main()