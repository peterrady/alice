import argparse
import copy
import cowsay
import numpy as np
import pwinput
import sys


def main():
    players = list()
    round_numbers = list()
    scores = dict()
    rou = 1

    # Commend-line arguments
    parser = argparse.ArgumentParser(description='This is a game called "King of Diamonds" from "Alice in Borderland" TV Series. You should input a number of players in command-line arguments then read the rules and type the name of each player.')
    parser.add_argument("-p", "--players", dest='N', default=5, help="number of players (5 players is the minmum and the defult)", type=int)
    ARGS = parser.parse_args()
    if ARGS.N < 5:
        sys.exit("Minumum number of players is 5")

    # Take players' names
    cowsay.cow("Welcome Players")
    print("Rules\n\n- All players select a number between 0 and 100.\n- The average of the values will be multiplied by 4/5ths (0.8).\n- The person who chooses the number closest to the calculated number wins. This constitutes one round.\n- All losers will lose a point.\n- New rule will be introduced when 4 players remaining, 3 players remaining and 2 players remaining.\n\nGame Clear: Be the last person remaining.\n\nGame Over: Reach -10 points.\n")
    for n in range(ARGS.N):
        players.append(input(f"Name of player {n + 1}: "))
        scores[players[n]] = 0
    print()

    # Game is running (for each round)
    while len(players) > 1:
        # Print round number
        cowsay.cow(f"Round {rou}")
        print()
        rou += 1

        # Print new rules
        if len(players) <= 4:
            print("4 players remaining rule: If there are 2 people or more choose the same number, the number they choose becomes invalid, meaning they will lose a point even if the number is closest to 4/5ths the average.\n")
        if len(players) <= 3:
            print("3 players remaining rule: If there is a person who chooses the exact correct number, the loser penalty is doubled.\n")
        if len(players) <= 2:
            print("2 players remaining rule: If someone chooses 0, the player who chooses 100 is the winner.\n")

        # Take numbers between 0 and 100 from players
        print("Wrint an integer between 0 and 100 and press enter.\nNOTE: Input won't appear to other players\n")
        for player in range(len(players)):
            while True:
                try:
                    number = int(pwinput.pwinput(prompt=f"{players[player]}: ", mask=''))
                    if check_range(number):
                        round_numbers.append(number)
                        break
                    else:
                        # Error message if the user write an invalid number
                        print("You should write an integer between 0 and 100")
                # Catch ValueError if the user write a string like "cat" for example
                except ValueError:
                    print("You should write an integer")

        # Calculate the winning number and closest value
        average = sum(round_numbers)/len(round_numbers)
        winning_number = round(average * 0.8, 2)
        closest_value:list = calculate_closest(copy.deepcopy(round_numbers), winning_number)
        print(f"\n{round_numbers}\n{round(average)}x0.8={winning_number}")

        # All players remaining
        if len(players) > 4:
            # Print the name of the winner in this round and calculate new scores
            for i in range(len(round_numbers)):
                if closest_value[0] == round_numbers[i]:
                    print(f"The winner in this round is {players[i]}")
                else:
                    scores[players[i]] -= 1

        # 4 players remaining
        elif 2 < len(players) <= 4:
            winner_flag = 0
            exact_flag = 0
            rep = repeated_numbers(round_numbers)
            for i in range(len(round_numbers)):
                if len(rep) >= 1:
                    if closest_value[0] == round_numbers[i] and closest_value[0] not in rep:
                        print(f"The winner in this round is {players[i]}")
                        winner_flag = 1
                    elif closest_value[2] == round_numbers[i] and closest_value[2] not in rep and len(rep) == 2:
                        print(f"The winner in this round is {players[i]}")
                        winner_flag = 1
                    else:
                        scores[players[i]] -= 1
                        # 3 players remaining
                        if len(players) == 3 and round(winning_number) == closest_value[0] and closest_value[0] not in rep:
                            exact_flag = 1
                            scores[players[i]] -= 1
                else:
                    if closest_value[0] == round_numbers[i]:
                        print(f"The winner in this round is {players[i]}")
                        winner_flag = 1
                    else:
                        scores[players[i]] -= 1
                        # 3 players remaining
                        if len(players) == 3 and round(winning_number) == closest_value[0]:
                            exact_flag = 1
                            scores[players[i]] -= 1
            if winner_flag == 0:
                print("No winner")
            if exact_flag == 1:
                print("Exact match")
                exact_flag = 0

        # 2 players remaining
        else:
            winner_flag = 0
            if round_numbers == [100, 0]:
                print(f"100 overrules 0")
                print(f"The winner in this round is {players[0]}")
                winner_flag = 1
                scores[players[1]] -= 1
            elif round_numbers == [0, 100]:
                print(f"100 overrules 0")
                print(f"The winner in this round is {players[1]}")
                winner_flag = 1
                scores[players[0]] -= 1
            else:
                # 4 players remaining
                rep = repeated_numbers(round_numbers)
                for i in range(len(round_numbers)):
                    if len(rep) == 1:
                        scores[players[i]] -= 1
                    else:
                        if closest_value[0] == round_numbers[i]:
                            print(f"The winner in this round is {players[i]}")
                            winner_flag = 1
                        else:
                            scores[players[i]] -= 1
            if winner_flag == 0:
                print("No winner")

        # Print scores
        print(f"Scores: {scores}")

        # Kill -10 score players
        counter = 0
        while counter < len(players):
            try:
                if scores[players[counter]] == -10:
                    cowsay.cow(f"{players[counter]} is died")
                    del scores[players[counter]]
                    del players[counter]
                    counter -= 1
            except IndexError:
                break
            counter += 1

        # Clear the numbers' list of this round
        round_numbers.clear()

    # Print name of the winner
    if players == []:
        cowsay.cow("No winner")
    else:
        cowsay.cow(f"The winner is {players[0]}")


def check_range(n):
    return 0 <= n <= 100


def calculate_closest(numbers, winning_number) -> list:
    sorted = []
    for _ in range(len(numbers)):
        arr = np.asarray(numbers)
        idx = np.abs(arr - winning_number).argmin()
        sorted.append(arr[idx])
        numbers.remove(arr[idx])
    return sorted


def repeated_numbers(numbers):
    seen = []
    rep = []
    for number in numbers:
        if number in seen:
            rep.append(number)
        else:
            seen.append(number)
    return rep


if __name__ == "__main__":
    main()
