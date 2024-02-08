# Rules
# All players remaining:
player_list = []
players = 5

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

    # The average of the values will be multiplied by 4/5ths (0.8).
    average = (sum(players_numbers.values()) / len(players_numbers)) * 0.8

    # The person who chooses the number closest to the calculated number wins. This constitutes one round.
    winner = min(players_numbers, key=lambda x: abs(players_numbers[x] - average))
    print("The winner of this round is:", winner)

    # All losers will lose a point.
    for player in player_list:
        if player != winner:
            score[player] -= 1

    print("Updated score:", score)

    # Remove player from the dictionary if their score is 0
    if score[player] == 0:
        del score[player]
        print(score)

# Display the final results
print("Scores:", score)

# At this point we have 4 players alive because a player score went down to 0 and he was eliminated
# To keep playing the game open the King_of_Diamonds_4_players

# A new rule will be introduced:
# 4 players remaining:
# If there are 2 people or more choose the same number, the number they choose becomes invalid,
# meaning they will lose a point even if the number is closest to 4/5ths the average.