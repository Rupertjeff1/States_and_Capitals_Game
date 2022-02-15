print("Hello, welcome to my game. ")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay, lets play!")
score = 0

answer = input("What is the Capital City of Ohio?")
if answer.lower() == "Columbus":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct.")

print("You got " + str(score) + " questions correct!")