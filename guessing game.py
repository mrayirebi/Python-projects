import random

def prize():
    #pine tree goes here
    #Get the number of rows for the tree
    tree_height = input("How tall do you want the tree: ")

    #convert to integer
    tree_height = int(tree_height)

    #Get the start spaces for the top of the tree
    spaces = tree_height - 1

    # There is one hash to start and will be incremented
    hashes = 1

    #Save stump spaces till later
    stump_space = tree_height - 1

    #make sure the right number of rows are printed
    while tree_height != 0:

    #Print the spaces
        for i in range(spaces):
            print(" ", end='')

    #Print the hashes
        for i in range(hashes):
            print('#', end="")
    #Newline after row is printed
        print()

    #The spaces is decremented by 1 each time
        spaces -=1

    # That hashes is incremented by 2 each time
        hashes += 2

    # Decrement tree height each time to jump out of the loop
        tree_height -= 1

    #Print the spaces before the stump and the hash
    for i in range(stump_space):
            print(' ', end="")
    print('#')
    print('Congratulation on beating the game')

    
def print_message():
    print(r'''

     /\                             
    /  \    _____   _ _ __ ___      
   / /\ \  |_  / | | | \'__/ _ \    
  / ____ \  / /| |_| | | |  __/     
 /_/    \_\/___|\__,_|_|  \___|     

        ''')
    print('\nWelcome to the guessing game \nBeat the game to unlock the pine tree')

def easy():
    randm_num = random.randrange(1, 11)
    while True:
        number = int(input("Guess a number between 1 and 10 : "))
        if number ==randm_num :
            print("Good job, you guessed the right number")
            print("Come back next time")
            prize()
            break
        elif number < randm_num:
            print("Go higher")
            continue

        elif number > randm_num:
            print("Go lower")
            continue
        
     
def medium():
    randm_num = random.randrange(1, 51)
    while True:
        number = int(input("Guess a number between 1 and 50 : "))
        if number ==randm_num :
            print("Good job, you guessed the right number")
            print("Come back next time")
            prize()
            break
        elif number < randm_num:
            print("Go higher")
            continue

        elif number > randm_num:
            print("Go lower")
            continue
        


def hard():
    randm_num = random.randrange(1, 100)
    while True:
        number = int(input("Guess a number between 1 and 100 : "))
        if number ==randm_num :
            print("Good job, you guessed the right number")
            print("Come back next time")
            prize()
            break
        elif number < randm_num:
            print("Go higher")
            continue

        elif number > randm_num:
            print("Go lower")
            continue
        

    
print_message()
#print("WELCOME TO THE GUESSING GAME, Beat the game to unlock the pine tree")
print('OPTIONS: \n 1. Easy \n 2. Medium \n 3. Hard')
level = int(input("Please select game level: "))
if level == 1:
    easy()
elif level == 2:
    medium()
elif level == 3:
    hard()
else:
    print("Select a level between 1, 2 or 3")
