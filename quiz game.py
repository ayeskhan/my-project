# first game
# ask users question, keep track of answer. If they got right answer then will tell them the score at the end

print("Welcome to capital city of countries quiz")
# now going to ask user if they want to play the game

playing = input("Do you want to play? ")
# user has to say yes for the program to run, have to make sure they say yes

if playing.lower() != "yes":
    quit() 

# .lower() makes the game more user friendly, if player typed "Paris" instead of "paris" they would get the answer wrong

 
print("Okay! Let's play :)")

# implementing notions of score
score = 0


# question 1 
answer = input("What is the Capital of Canada? ")
if answer.lower() == "ottawa":
    print("Good job!")
    score += 1
else:
    print("Incorrect!")

# question 2 
answer = input("What is the Capital of Germany? ")
if answer.lower() == "berlin":
    print("Good job!")
    score += 1
else:
    print("Incorrect!")

# question 3 
answer = input("What is the Capital of South Korea? ")
if answer.lower() == "seoul":
    print("Good job!")
    score += 1
else:
    print("Incorrect!")

# question 4 
answer = input("What is the Capital of Australia? ")
if answer.lower() == "canberra":
    print("Good job!")
    score += 1
else:
    print("Incorrect!")

# question 5 
answer = input("What is the Capital of Fiji? ")
if answer.lower() == "suva":
    print("Good job!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%.")


