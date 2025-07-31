
def add_to_set():
    global firstset
    global secondset
    add_to_firstset = (input("Enter the elements to  add to the  first set separated by space "))
    firstset = set(add_to_firstset.split())
    add_to_second_set = (input("Enter the elements to add to the second set separated by space "))
    secondset = set(add_to_second_set.split())
    print("First set: ", firstset)
    print("Second set: ", secondset)


add_to_set()
common_set = firstset.intersection(secondset)
print(f"Your common set is {common_set}")
