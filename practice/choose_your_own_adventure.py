name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go left or right. Which way would you like to go ").lower()

if answer == "left":
    answer = input("You come to the river, you can walk around it or swim across")

    if answer == "swim":
        print("You swim across and were eaten bu an alligator!")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game!")
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back cross/back?")

    if answer == "back":
        print("You go back to main road! Now you can decide to go left or right")

    elif answer == "cross":
        answer = input("You cross the bridge and met a stranger. Do you talk to them or no?")

else:
    print("Not a valid option. You lose.")




