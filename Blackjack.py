#This code is based on the Udemy course milestone project
#This code will take the Class and Card classes to make a 52 card deck
#Will ask the player to make a bet agains the dealer and then play blackjack
#Player will be asek to hit or take another card
#This is a bit unique as I forgot how to play Blackjack and so the program keeps playing
#until all 52 cards are used up

import random

#These are my constants for the future I will UPPER_SNAKE_CASE
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

if __name__=="__main__":

    class Card():

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]

        def __str__(self):
            return f"{self.rank} of {self.suit}"


    class Deck():

        def __init__(self):
            self.all_cards = []
            for suits_card in suits:
                for rank_card in ranks:
                    self.all_cards.append(Card(suits_card, rank_card))

        def shuffle(self):
            random.shuffle(self.all_cards)

        def deal(self):
            return self.all_cards.pop()

        def __str__(self):
            for x in range(0, len(self.all_cards)):
                print(f"{self.all_cards[x]}")
            return f"This is the current cards in the deck"


    class Hand():

        def __init__(self):
            self.all_cards = []
            # player overall value towards 21 = winning! Blackjack
            self.player_value = 0
            # counter to keep track of when an ace is in player hand
            self.ace_counter = 0

        # adding a card to player hand, calculating value towards 21 & Ace counter
        def add_card(self, new_card):
            self.all_cards.append(new_card)
            self.player_value += new_card.value
            if new_card.rank == "Ace":
                self.ace_counter += 1

        # Best way to change the Ace value is by subtracting from the overall value sum
        def adjust_ace(self):
            while self.player_value > 21 and self.ace_counter:
                self.player_value -= 10
                self.ace_counter -= 1

        def __str__(self):
            # for x in range(0,len(self.all_cards)):
            # print(f"{self.all_cards[x]}")
            return f"Hand Value is {self.player_value}"


    class Chips():

        def __init__(self):
            self.total = 100  # lets say this is our starting chips
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet


    def take_bet(chips):

        while True:
            try:
                chips.bet = int(input("Place your bet Player: "))

            except ValueError:
                print("You must bet an integer value")

            else:
                if chips.bet > chips.total:
                    print("You exceeded your total of {chips.total}")
                else:
                    break


    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_ace()


    def hit_or_stand(deck, hand):
        global playing

        while True:

            turn = input("\nWill you (hit) or (stand)? (please type one of the following under paranthesis)\n")

            if turn == "hit":
                hit(deck, hand)
            elif turn == "stand":
                playing = False
            else:
                print('input must be either "hit" or "stand"! Try again')
                continue
            break


    def show_some(player, dealer):
        print("\nShow me only some cards yo ;)")
        print(f"\nDealer's hand:\nhidden\n{dealer.all_cards[1]}")
        print("\nPlayer's hand:", *player.all_cards, player, sep="\n")


    def show_all(player, dealer):
        print("Lay it all on the floor , please yo!")
        print("\nDealer's Hand: \n", *dealer.all_cards, dealer, sep="\n")
        print("\nPlayer's Hand: \n", *player.all_cards, player, sep="\n")


    def player_busts(player, player_chips):
        print("*****************************")
        print("Player busts")
        print("*****************************")
        player_chips.lose_bet()
        # player.all_cards = []


    def player_wins(player, player_chips):
        print("*****************************")
        print("Player wins!")
        print("*****************************")
        player_chips.win_bet()
        # player.all_cards = []


    def dealer_busts(dealer, dealer_chips):
        print("*****************************")
        print("Dealer busts")
        print("*****************************")
        dealer_chips.lose_bet()
        # dealer.all_cards = []


    def dealer_wins(dealer, dealer_chips):
        print("*****************************")
        print("Dealer Wins!")
        print("*****************************")
        dealer_chips.win_bet()
        # dealer.all_cards = []


    def push():
        print("****************************************************")
        print("Its a tie, both Player and Dealer Push Bay-Bee")
        print("****************************************************")
        pass


    the_deck = Deck()
    # player = Hand()
    # dealer = Hand()

    player_chips = Chips()
    dealer_chips = Chips()

    round = 1

    while True:  # This is the overall Blackjack game, until all cards in deck are gone or player quits

        player = Hand()
        dealer = Hand()

        print(
            f"Round {round}: The deck has {len(the_deck.all_cards)}\nPlayer has {player_chips.total} chips\nDealer has {dealer_chips.total} chips")
        playing = True

        take_bet(player_chips)
        dealer_chips.bet = player_chips.bet

        the_deck.shuffle()

        for x in range(0, 2):
            player.add_card(the_deck.deal())

        for y in range(0, 2):
            dealer.add_card(the_deck.deal())

        show_some(player, dealer)

        while playing and player.player_value != 21:  # single game until either the player or dealer wins the bet

            # player turn

            hit_or_stand(the_deck, player)

            show_some(player, dealer)

            if player.player_value >= 21:
                break

                # player bust haha
        if player.player_value > 21:
            player_busts(player, player_chips)

        if player.player_value == 21:
            print("MF Blackjack!!!!!, Dealer Loses")
            player_wins(player, player_chips)
            dealer_chips.lose_bet()

        # Player didn't bust, lets play dealers hand
        if player.player_value < 21:
            print("\nTime to show all the cards\n")
            show_all(player, dealer)

            print("\nDealer's Turn")
            while dealer.player_value < 17:
                hit(the_deck, dealer)

            if dealer.player_value > 21:
                dealer_busts(dealer, dealer_chips)
                player_chips.win_bet()

            elif dealer.player_value == 21:
                dealer_wins(dealer, player_chips)
                player_chips.lose_bet()

            elif player.player_value > dealer.player_value:
                player_wins(player, player_chips)
                dealer_chips.lose_bet()

            elif dealer.player_value > player.player_value:
                dealer_wins(dealer, dealer_chips)
                player_chips.lose_bet()

            elif player.player_value == dealer.player_value:
                push()

        print("\nTime to show all the cards AGAIN!\n")
        show_all(player, dealer)

        print(f"\nPlayer has {player_chips.total} chips\nDealer has {dealer_chips.total} chips")

        while True:
            answer = input("Does player want to go another round? (Y or N): ")
            if answer.lower() == "y" or answer.lower() == "n":
                break
            else:
                print('please only input either a "Y" or a "N"')
                continue

        if answer.lower() == "n" or player_chips.total == 0 or dealer_chips.total == 0:
            print("Sorry you are a sore loser")
            break

        player.all_cards = []
        dealer.all_cards = []
        round += 1
        #This project originated in Jupyter and therefore the clear_output() command was used
        #clear_output()
        print('\n' * 100)
