name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road , it has come to an end and you can go left or right. which would you like to go" ).lower()
if answer == "left":
    answer = input("you came to a river, you can walk around it or swim across it,  Type walk to walk around it or swim to swim across it" ).lower()
    if answer == "walk":
        print("You walked for many miles , and finally you found a village. You are welcome there.")
    elif answer == "swim":
        print("You swam across and were eaten by an alligator")
    else:
        print("You must type walk or swim to continue")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or go back(cross/back)" ).lower()
    if answer == "cross":
        print("You made it to the other side, but the bridge collapsed behind you")
    elif answer == "back":
        print("You went back and lost")
    else:
        print("Cross/walk")
    
    
    print("")

else:
    print("You did not enter a valid direction. You lose")