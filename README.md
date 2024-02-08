This code implements a game called "King of Diamonds" based on rules inspired by the series "Alice in Borderland". 
Correct order of running the .py to play the game:

You will need 5 different players!
First, run King_Of_Diamonds_5_Players.
Second, run King_Of_Diamonds_4_Players.
Third, run King_Of_Diamonds_3_Players.
Fourth run King_Of_Diamonds_2_Players.

Here's a breakdown of its capabilities and stages:

Capabilities:
1. Player Input: It allows players to input their names at the beginning of the game.
2. Player Selection: Players select a number between 0 and 100.
3. Scoring: Each player starts with a score of 10, which decreases when they lose rounds.
4. Winner Determination: The player whose chosen number is closest to 4/5ths of the average of all chosen numbers wins each round.
5. Elimination: Players whose score reaches 0 are eliminated from the game.
6. Special Rules:
   When 4 players remain, if there are duplicates in the chosen numbers, all players who chose a duplicate number lose a point.
   When 3 players remain, if one of them chooses the exact correct number, the penalty for the losers is doubled.
   When 2 players remain, if one chooses 0 while the other chooses 100, the latter wins the game.


Stages:
1. Initialization:
   Players enter their names.
   The initial score for each player is set to 10.
2. Game Loop:
   Players repeatedly choose numbers until one player's score reaches 0.
   For each round:
      Players input their chosen numbers.
      The average of the chosen numbers is calculated.
      The winner of the round is determined based on proximity to the calculated average.
      Scores are updated accordingly.
      Eliminated players are removed from the game.
3. Special Rule Introduction:
   As the number of players decreases, special rules are introduced.
   These rules change the gameplay dynamics and add complexity to the decision-making process.
4. Game Conclusion:
   The game concludes when only one player remains or when the special rule for two players is triggered.
   The winner is announced.

Explanation:
   The code is organized into sections based on the number of players remaining and the corresponding special rules.
   It utilizes loops and conditionals to manage player input, score calculation, and game progression.
   The code employs dictionaries to store player names and their corresponding scores.
   Functions such as min() and abs() are used to determine the winner based on the rules of the game.
   Special rules are introduced dynamically based on the number of players remaining, adding depth and unpredictability to the gameplay.
   Throughout the game, informative messages are printed to provide feedback to players and keep them engaged.
   Overall, this code simulates a strategic and competitive game experience, offering players a challenging and immersive gameplay environment reminiscent of the "King of Diamonds" game from the "Alice in Borderland" series.
