print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's paly :)")
score = 0

answer = input("wht does CPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else: 
    print("incorrect!")


answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else: 
    print("incorrect!")


answer = input("wht does PSU stand for? ")
if answer.lower() == "power supply":
    print("correct!")
    score += 1
else: 
    print("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")
