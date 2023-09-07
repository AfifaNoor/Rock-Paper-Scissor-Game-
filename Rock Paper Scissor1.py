#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

user_points = 0
computer_points = 0
round = 0

while round < 5:
    user_action = input("Choose 'r' for rock, 'p' for paper, 's' for scissor: ")
    computer_action = random.choice(['r', 'p', 's'])

    if user_action == computer_action:
        print("It's a tie!")
    elif (user_action == 'r' and computer_action == 's') or (user_action == 's' and computer_action == 'p') or (user_action == 'p' and computer_action == 'r'):
        user_points += 1
        print(f"You win this round! {user_action} beats {computer_action}")
    else:
        computer_points += 1
        print(f"You lose this round! {computer_action} beats {user_action}")

    round += 1

print("\nGame over! Results:")
print(f"User points: {user_points}\nComputer points: {computer_points}")

if user_points > computer_points:
    print("You win the game!")
elif user_points < computer_points:
    print("Computer wins the game!")
else:
    print("It's a tie game!")


# # Explaination

# In[ ]:


# We import the random module to generate the computer's choice.
# We set up variables to keep track of user points, computer points, and the current round.
# We use a while loop to play a maximum of 5 rounds.
# The user selects their action ('r' for rock, 'p' for paper, 's' for scissors).
# The computer randomly selects its action.
# We compare the user's and computer's actions to determine the winner of the round and update the points accordingly.
# The game continues until 5 rounds are completed.
# After the game, we display the results and determine the overall winner.

