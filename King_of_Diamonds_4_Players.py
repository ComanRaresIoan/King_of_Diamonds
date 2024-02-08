# Rules
# 4 Players remaining
player_list = []
players = 4

for i in range(0, players):
    player = str(input("Enter the name of the player: "))
    player_list.append(player)

print("The list of players is:\n", player_list)

score = {}
for index, player in enumerate(player_list):
    score[player] = 10

while any(score[player] > 0 for player in player_list):  # Continue until someone reaches a score of 0
    # All players select a number between 0 and 100 in the given time.
    players_numbers = {}
    for player in player_list:
        valid_input = False
        while not valid_input:
            try:
                number = int(input(f"{player}, enter a number between 0 and 100: "))
                if 0 <= number <= 100:
                    players_numbers[player] = number
                    valid_input = True
                else:
                    print("Error: The number must be between 0 and 100. ")
            except ValueError:
                print("Error: Please enter a valid number")

    print("The list of numbers is: ", players_numbers)

    # Check for duplicates
    seen = set() # We declare a set of values where we check for no duplicates
    duplicates = set(x for x in players_numbers.values() if x in seen or seen.add(x))

    # The average of the values will be multiplied by 4/5ths (0.8).
    average = (sum(players_numbers.values()) / len(players_numbers)) * 0.8

    # The person who chooses the number closest to the calculated number wins. This contitutes one round
    if len(duplicates) >= 2: # If there are duplicates, penalize those players
        for player,number in players_numbers.items():
            if number in duplicates:
                score -=1
        print("There are duplicates. All players who chose a duplicate number lose a point. ")
    else:
        winner = min(players_numbers, key=lambda x: abs(players_numbers[x] - average))
        print("The winner of this round is:",winner)
        # All players will lose 1 point
        for player in player_list:
            if player != winner:
                score[player]-=1

    print("Update score: ",score)

    # Remove player from the dictionary if their score is 0
    for player in player_list:
        if score[player] <= 0:
            print(f"{player} has been eliminated.")  # We print the message for eliminated player
            del score[player]
            player_list.remove(player)

# Display the final results
print("Scores:", score)

# with that being said, once reach 3 players remaining, a new rule will be introduced:
# If there is a person who chooses the exact correct number, the loser penalty is doubled.