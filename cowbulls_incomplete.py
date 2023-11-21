import random

def compare_numbers(number, user_guess):
    cow = 0 # added variable for cow
    bull = 0 # added variable for bull
    for i in range(4): # added for for loop
        if user_guess[i] == number[i]: # add if statement that if user guesses one digit number placement right, bull variable will increase by one
            bull+=1 # bull variable will increase by one if statement above is met
        elif user_guess[i] in number: # add elif statement that if user input value is in the number value, it will increase the cow variable by one
            cow+=1 # cow variable will increase by one if statement above is met
        cowbull = (cow,bull) # added cowbull variable that stores cow and bull variable
    return cowbull

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print(number) #added brackets

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!") #removed raw_
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
