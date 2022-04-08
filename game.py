import time

print("Hello, welcome to my game. The objective of this game is I will give you either State or Capital. If I give you a State you must guess its Capital City. \
If I give you a Capital, you must then list its State. ")
time.sleep(2)

playing = input("Do you want to play States and Capitals? ")
if playing.lower() != "yes":
    quit()
print("Okay, lets play!")
time.sleep(1)
score = 0

answer = input("What is the Capital City of Ohio? ")
if answer.lower() == "columbus":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The answer is Columbus.")

answer = input("What States Capital is Harrisburgh? ")
if answer.lower() == "pennsylvania":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The correct answer is Pennsylvania.")

answer = input("What is the Capital of Florida? ")
if answer.lower() == "tallahassee":
    print("Correct!")
    score += 1
else: 
    print("Sorry, the correct answer is Tallahassee.")

answer = input("What States Capital is Denver? ")
if answer.lower() == "colorado":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The correct answer is Colorado.")

answer = input("What States Capital is Juneau? ")
if answer.lower() == "alaska":
    print("Correct!")
    score += 1
else: 
    print("Sorry, the correct answer was Alaska.")

answer = input("What is the Capital of California? ")
if answer.lower() == "sacramento":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The answer we were looking for is Sacramento.")

answer = input("What is the Capital of Mississippi? ")
if answer.lower() == "jackson":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. Jackson is the Capital of Mississippi.")

answer = input("What States Capital is Lansing? ")
if answer.lower() == "michigan":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The correct answer is Michigan.")

answer = input("What is the Capital of Kansas? ")
if answer.lower() == "topeka":
    print("Correct!")
    score += 1
else: 
    print("Sorry, Topeka was the answer we were looking for.")

answer = input("What is the Capital of Georgia? ")
if answer.lower() == "atlanta":
    print("Correct!")
    score += 1
else: 
    print("Sorry, that's not correct. The correct answer is Atlanta.")

print("You got " + str(score) + " of 10 questions correct!")