#creating a claculator
a= int(input("Enter the first number "))
b = int(input("enter the second number " ))
which_operation = input("Which operation do you wat to perfom  ")

sum = a + b
subtraction = a - b
multiplication = a * b
division = a / b

if which_operation == "+":
    print(f"{a} + {b} = {sum}")
elif which_operation == "-":
    print(f"{a} - {b} ={subtraction}")
elif which_operation == "*":
    print(f"{a} * {b}= {multiplication}")
elif which_operation == "/":
        print(f"{a} / {b}= {division}")
else :
    print("Invalid operation")



