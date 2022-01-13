#Testing - adding this comment from my local main in git kraken
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

        for ranks_count in ranks:
            for suits_count in suits:
                self.all_cards.append(Card(suits_count, ranks_count))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def take_one(self):
        return self.all_cards.pop()


class Player():

    def __init__(self, name):

        self.all_cards = []
        self.name = name

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # List of multiple card objects
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # Only for a single card
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# War Game Main

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

hand_1 = []
hand_2 = []

flag_1 = 0
flag_2 = 0

player_1 = Player("Alvaro")
player_2 = Player("Krystal")

war_deck = Deck()

war_deck.shuffle()

for index in range(0, 26):
    player_1.add_cards(war_deck.take_one())

for index in range(0, 26):
    player_2.add_cards(war_deck.take_one())

round_num = 1

while True:

    if len(player_1.all_cards) == 52:
        print(f"THE WINNER OF THIS WAR GAME IS PLAYER 1 {player_1}")
    elif len(player_2.all_cards) == 52:
        print(f"THE WINNER OF THIS WAR GAME IS PLAYER 2 {player_2}")

    # Checking to see if any player has won before restarting the roud
    if len(player_1.all_cards) == 0 or len(player_2.all_cards) == 0:
        break

    print(f"Round {round_num}")
    round_num += 1

    print(f"Player 1 has {len(player_1.all_cards)} and Player 2 has {len(player_2.all_cards)}!")

    print(f"Player 1 has {player_1.all_cards[0]} and Player 2 has {player_2.all_cards[0]}")

    # **************************************** WAR SCENARIO *****************************************************
    # checking to see if War is inevitable, if it is, then while loop to continue checking if still
    # in war until a clear winner is decided
    if player_1.all_cards[0].value == player_2.all_cards[0].value:
        print("***War has started***")
        while player_1.all_cards[0].value == player_2.all_cards[0].value:
            try:
                for index in range(0, 4):
                    hand_1.append(player_1.remove_one())
            except IndexError:
                print("Player 1 is empty")
                for index in range(0, len(player_1.all_cards)):
                    hand_1.append(player_1.remove_one())
                flag_1 = 1

            try:
                for index in range(0, 4):
                    hand_2.append(player_2.remove_one())
            except IndexError:
                print("Player 2 is empty")
                for index in range(0, len(player_2.all_cards)):
                    hand_1.append(player_2.remove_one())
                flag_2 = 1

            try:
                print(f"Player 1 has {player_1.all_cards[0]} cards and Player 2 has {player_2.all_cards[0]} cards")

            except IndexError:
                break
        print(f"flag 1 = {flag_1} and flag 2 = {flag_2}")

        if flag_1 == 1:
            print("Player 2 has won\n")
            player_2.add_cards(hand_1)
            player_2.add_cards(hand_2)

        elif flag_2 == 1:
            print("Player 1 has won\n")
            player_1.add_cards(hand_1)
            player_1.add_cards(hand_2)

        # War outcome if player 1 wins
        try:
            if player_1.all_cards[0].value > player_2.all_cards[0].value:
                print("Player 1 has won\n")
                player_1.add_cards(hand_1)
                player_1.add_cards(hand_2)
                player_1.add_cards(player_2.remove_one())
                player_1.add_cards(player_1.remove_one())
                hand_1 = []
                hand_2 = []

            # War outcome if player 2 wins
            else:
                print("Player 2 has won\n")
                player_2.add_cards(hand_1)
                player_2.add_cards(hand_2)
                player_2.add_cards(player_1.remove_one())
                player_2.add_cards(player_2.remove_one())
                hand_1 = []
                hand_2 = []

        # War outcome to make sure either player 1 or player 2 receives all cards in order to win the game
        # This only occurs when on war happened and the player had just enough cards to draw 3 more cards
        # but not enough to have player.all_cards[0] so an IndexError occurs
        except IndexError:
            print("War happened and someone ran out of cards lol")
            print(f"Player 1 has {len(player_1.all_cards)} and Player 2 has {len(player_2.all_cards)}!")
            if len(player_1.all_cards) == 0 and flag_1 == 0:
                player_2.add_cards(hand_1)
                player_2.add_cards(hand_2)
            elif len(player_2.all_cards) == 0 and flag_2 == 0:
                player_1.add_cards(hand_2)
                player_1.add_cards(hand_1)

    # **************************************** PLAYER 1 WINS *****************************************************
    # Player 1 wins round
    elif player_1.all_cards[0].value > player_2.all_cards[0].value:
        print("Player 1 has won\n")
        player_1.add_cards(player_2.remove_one())
        player_1.add_cards(player_1.remove_one())


    # **************************************** PLAYER 2 WINS *****************************************************
    # Player 2 wins round
    elif player_1.all_cards[0].value < player_2.all_cards[0].value:
        print("Player 2 has won\n")
        player_2.add_cards(player_1.remove_one())
        player_2.add_cards(player_2.remove_one())