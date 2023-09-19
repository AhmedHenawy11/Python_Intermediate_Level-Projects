import random
import art
from replit import clear

cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
new = []

# The start of the game function.


def start_game():
    user = [random.choice(cards), random.choice(cards)]
    computer = [random.choice(cards), random.choice(cards)]
    new = {"user": user, "computer": computer}
    return new


# Adding cards function.
def add_card(i):
    i["user"].append(random.choice(cards))
    i["computer"].append(random.choice(cards))
    sum = 0
    sum2 = 0
    for n in i["user"]:
        sum += n
    for n in i["computer"]:
        sum2 += n
    return i
    #cards1["user"].append(random.choice(cards))
    #cards2["computer"].append(random.choice(cards))
    #new = {
    # "user":cards1,
    # "computer": cards2


# }
def sum(i):
    sum = 0
    sum2 = 0
    for n in i["user"]:
        sum += n
    for n in i["computer"]:
        sum2 += n
    return sum, sum2


# The process collection function


def play():
    player_cards = start_game()
    print(
        f'Your cards : {player_cards["user"]}, current score: {sum(player_cards)[0]}'
    )
    print(f'Computer\'s first card: {player_cards["computer"][0]}')

    if sum(player_cards)[0] == 21:
        print(
            f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
        )
        print(
            f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
        )
        print("You win 😃")
        main()

    add = input("Type 'y' to get another card, type 'n' to pass: ")

    if sum(player_cards)[0] > sum(player_cards)[1] and add != "y":
        print(
            f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
        )
        print(
            f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
        )
        main()

    if sum(player_cards)[1] == 21:
        print(
            f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
        )
        print(
            f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
        )
        print("You went over. You lose 😭")
        main()

    while add == "y":

        player_cards = add_card(player_cards)
        if sum(player_cards)[0] == 21 and sum(player_cards)[1] != 21:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("You win 😃")
            main()

        elif sum(player_cards)[0] == 21 and sum(player_cards)[1] == 21:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("Draw")
            main()

        elif sum(player_cards)[1] == 21 and sum(player_cards)[0] != 21:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("You went over. You lose 😭")
            main()

        elif sum(player_cards)[0] > 21 and sum(player_cards)[1] < sum(
                player_cards)[0]:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("You went over. You lose 😭")
            main()

        elif sum(player_cards)[1] > 21 and sum(player_cards)[0] < sum(
                player_cards)[1]:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("You win 😃")
            main()

        elif sum(player_cards)[1] == 21:
            print(
                f'Your cards : {player_cards["user"]}, final score: {sum(player_cards)[0]}'
            )
            print(
                f'Computer\'s final hand: {player_cards["computer"]}, final score: {sum(player_cards)[1]}'
            )
            print("You went over. You lose 😭")
            main()
    else:
        print(
            f'Your cards : {player_cards["user"]}, current score: {sum(player_cards)[0]}'
        )
        print(f'Computer\'s first card: {player_cards["computer"][0]}')
        add = input("Type 'y' to get another card, type 'n' to pass: ")


# The main Function that starts the program


def main():
    again = True
    play_again = ""

    while again == True:

        play_again = input("Do you want to play the game? Type 'y' or 'n':")
        if play_again == "y":
            clear()
            print(art.logo)
            play()
        else:
            again = False


main()
