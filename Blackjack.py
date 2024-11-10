import random

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
kind = ["Spades", "Hearts", "Clubs", "Diamonds"]


def deck():
    stokk = []
    for k in kind:
        for c in cards:
            stokk.append((c, k))
    return stokk


def total(hand):
    total = 0
    for card in hand:
        if card[0] == "K" or card[0] == "J" or card[0] == "Q":
            total += 10
        elif card[0] == "A":
            if total >= 12:
                total += 1
            else:
                total += 11
        else:
            total += card[0]
    return total


def blackjack_game():
    x = 10
    while True:
        while True:
            print()
            if x == 0:
                print("You have 0 chips to gamble, welcome back anytime.")
                exit()

            # Try-except block to handle non-integer inputs
            try:
                chips_input = int(input(f"you currently have {x} chips, how many would you like to gamble?: "))
                if chips_input not in range(1, (x + 1)):
                    print(f"Not valid amount of chips, you can max bet {x}.")
                else:
                    print(f"{chips_input} chips at stake! Let's begin")
                    print()
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        player_hand = []
        dealer_hand = []

        stokk = deck()
        random.shuffle(stokk)

        while len(dealer_hand) != 2:
            card = stokk.pop()
            dealer_hand.append(card)
            if len(dealer_hand) == 2:
                print(f"Dealer has {dealer_hand[0]} and X")

        while len(player_hand) != 2:
            card = stokk.pop()
            player_hand.append(card)
            if len(player_hand) == 2:
                print(f"Your cards: {player_hand[0]}, {player_hand[1]} which makes {total(player_hand)} total")
            if len(player_hand) == 2 and total(player_hand) == 21:
                player_chips = x + chips_input * 2.5
                print(
                    f"BLACKJACK! you win 2.5 times your bet! you won {chips_input * 2.5}! current chips: {player_chips}")
                new_x = int(player_chips)
                x = new_x

        while total(player_hand) < 21:
            print()
            player_choice = input("Do you want to stand or hit?: ")
            if player_choice.lower() == "hit":
                card = stokk.pop()
                player_hand.append(card)
                print(f"you drew {card}, your total is now {total(player_hand)}")
                if total(player_hand) >= 22:
                    print("you bust, dealer wins.")
                    player_chips = x - chips_input
                    print(f"you lost {chips_input} chips! current chips: {player_chips}")
                    new_x = player_chips
                    x = new_x

            if player_choice.lower() == "stand" or total(player_hand) == 21:
                print(f"dealer has {dealer_hand[0]}, {dealer_hand[1]} which makes {total(dealer_hand)} total")
                while total(dealer_hand) <= 16:
                    card = stokk.pop()
                    dealer_hand.append(card)
                    print(f"Dealer drew {card}, total is now {total(dealer_hand)}")

                if total(player_hand) >= 22:
                    print("You bust, Dealer wins")
                    player_chips = x - chips_input
                    print(f"you lost {chips_input} chips! current chips: {player_chips}")
                    new_x = player_chips
                    x = new_x
                    break

                if total(player_hand) > total(dealer_hand):
                    print("You win!")
                    player_chips = x + chips_input
                    print(f"you won {chips_input * 2} chips! current chips: {player_chips}")
                    new_x = player_chips
                    x = new_x
                    break
                if total(dealer_hand) > total(player_hand):
                    if total(dealer_hand) < 21:
                        print("Dealer wins!")
                        player_chips = x - chips_input
                        print(f"you lost {chips_input} chips! current chips: {player_chips}")
                        new_x = player_chips
                        x = new_x
                        break
                    if total(dealer_hand) >= 22:
                        print("Dealer bust! you win")
                        player_chips = x + chips_input
                        print(f"you won {chips_input * 2} chips! current chips: {player_chips}")
                        new_x = player_chips
                        x = new_x
                        break
                    if total(dealer_hand) == 21 and total(dealer_hand) > total(player_hand):
                        print("Dealer wins!")
                        player_chips = x - chips_input
                        print(f"you lost {chips_input} chips! current chips: {player_chips}")
                        new_x = player_chips
                        x = new_x
                        break
                if total(player_hand) == total(dealer_hand):
                    print(f"dealer shows push! Chips back. Current chips: {x}")
                    break
                if total(player_hand) >= 22:
                    print("you bust, dealer wins.")
                    player_chips = x - chips_input
                    print(f"you lost {chips_input} chips! current chips: {player_chips}")
                    new_x = player_chips
                    x = new_x
                    break
                if total(player_hand) == 21:
                    print("you win!")
                    player_chips = x + chips_input
                    print(f"you won {chips_input * 2} chips! current chips: {player_chips}")
                    new_x = player_chips
                    x = new_x
                    break
        else:
            print()

        while True:
            print()
            play_again = input("Do you want to play again? If so, type Yes: ")
            if play_again.lower() == "yes":
                break
            else:
                print(f"Thanks for playing, you ended up with {x} chips!")
                exit()


while True:
    start = input("Welcome to blackjack, type Yes if you want to start playing: ")
    if start.lower() == "yes":
        blackjack_game()
    elif start.lower() == "no":
        print("Welcome back anytime.")
        exit()
    else:
        print("Please write Yes to start playing, or No to end")
        print()
