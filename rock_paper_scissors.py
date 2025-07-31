import random

user_wins = 0
computer_wins = 0
options = ["rock" , "paper" , "scissors"]

while True:
    users_input = input("Type Rock/Paper/Scissors or Q to quit. ").lower()
    if users_input.lower() == "q":
        break

    if users_input not in options:
        continue
    else:
      random_number = random.randint(0,2)
      # 0 = rock , 1 = paper , 2 = scissors
      computer_pick = options[random_number]
      print("Computer chose", computer_pick +".")

      if users_input == "rock" and computer_pick == "scissors":
          print("You win!")
          user_wins += 1
      elif users_input == "paper" and computer_pick == "rock":
          print("You win!")
          user_wins += 1

      elif users_input == "scissors" and computer_pick == "paper":
          print("You win!")
          user_wins += 1
      elif users_input == computer_pick:
          print("It's a tie!")
      else:
          print("You lost! Computer wins!")
          computer_wins += 1

print("you won", user_wins, "times")
print("computer won", computer_wins, "times")

print("Goodbye")
