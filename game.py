import time
print("Hello, welcome to my game. ")

playing = input("Do you want to play States and Capitals? ")
if playing.lower() != "yes":
    quit()
print("Okay, lets play!")

time.sleep(1)
print("The objective of this game is I will give you either State or Capital. If I give you a State you must guess its Capital City. \
If I give you a Capital, you must then its State.")
score = 0

answer = input("What is the Capital City of Ohio? ")
if answer.lower() == "columbus":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct.")

answer = input("What States Capital is Harrisburgh? ")
if answer.lower() == "pennsylvania":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct.")

answer = input("What is the Capital of Florida? ")
if answer.lower() == "tallahasee":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct.")

print("You got " + str(score) + " questions correct!")