def enter_numbers():
    numbers = []
    sum = 0
    while True:
        user_input = int(input("Enter a number (or 'q' to quit): "))
        if user_input.lower() == 'q':
            break
        else :
            numbers.append(user_input)
            sum += int(user_input)
        print(f"Here is your list of numbers {numbers} and the sum is {sum}")
        

enter_numbers()