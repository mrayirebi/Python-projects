import random

def easy():
    randm_num = random.randrange(1, 11)
    while True:
        number = int(input("Guess a number between 1 and 10 : "))
        if number ==randm_num :
            print("Good job, you guessed the right number")
            print("Come back next time")
            break
        elif number < randm_num:
            print("Go higher")
            continue

        elif number > randm_num:
            print("Go lower")
            continue
        elif number == 0:
            break
     
def medium():
    randm_num = random.randrange(1, 51)
    while True:
        number = int(input("Guess a number between 1 and 50 : "))
        if number ==randm_num :
            print("Good job, you guessed the right number")
            print("Come back next time")
            break
        elif number < randm_num:
            print("Go higher")
            continue

        elif number > randm_num:
            print("Go lower")
            continue
        elif number == 0:
            break


level = int(input("Please select game level: "))
if level == 1:
    easy()
elif level == 2:
    medium()
else:
    print("Select a level between 1 and 2")
