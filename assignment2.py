import random

while (1):

    comp = [random.randint(1,9),random.randint(0,9),random.randint(0,9)]
    if(comp[0]!=comp[1] & comp[0]!=comp[2] & comp[2]!=comp[1]):
        break
    else:
        continue

digits1=int(f"{comp[0]}{comp[1]}{comp[2]}") # converts computers number into 3 digit number


player = 0
noOfGuesses = 0
result = []
score = 10


while (player!=digits1):
    player = int(input("Guess a three digit number :"))
    digits = [int(d) for d in str(player)] # converts players number into array of three numbers

    length=len(digits)

    if (length < 3):
        print(f"Please enter 3 digit number you entered {length} digits.")
        continue

    noOfGuesses+=1
    score-=1

    if (digits[0]==comp[0]):
        result.append("✔ correct digit ")
    elif(digits[0]==comp[1] or digits[0]==comp[2]):
        result.append("👍 correct digit but wrong position ")
    else:
        result.append("❌ wrong digit ")


    if (digits[1]==comp[1]):
        result.append("✔ correct digit ")
    elif(digits[1]==comp[0] or digits[1]==comp[2]):
        result.append("👍 correct digit but wrong position ")
    else:
        result.append("❌ wrong digit ")


    if (digits[2]==comp[2]):
        result.append("✔ correct digit ")
    elif(digits[2]==comp[0] or digits[2]==comp[1]):
        result.append("👍 correct digit but wrong position ")
    else:
        result.append("❌ wrong digit ")


    print(result)
    result=[]

print(f"Correct guess\nYou guessed correct number in {noOfGuesses} guesses.\nYour score is {score}.")