import matplotlib.pyplot as plt
import json

from blackjack_card import Card
from blackjack_deck import Deck
from blackjack_hand import Hand
  



with open('chart_pairs.json') as file1:
    chart_pairs = json.load(file1)
with open('chart_ace.json') as file2:
    chart_ace = json.load(file2)
with open('chart_totals.json') as file3:
    chart_totals = json.load(file3)




class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.num = 0

    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.player_hand_split = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("------------")
            print("You:")
            self.player_hand.display()
            print()
            print("Dealer:")
            self.dealer_hand.display()
            print()

            game_over = False
            is_first_round = True
            split = False

            while not game_over:
                has_blackjack = (self.player_hand.get_value() == 21) or (self.player_hand_split.get_value() == 21)
                choice = ""
                
                if not has_blackjack:
                    if (self.player_hand.cards[0].value == self.player_hand.cards[1].value) and is_first_round:
                        choice = input("Hit(h), Stick(s), Split(p) or Double Down(d): ").lower()
                        if choice in ['p']:
                            split = True
                            self.player_hand_split.cards.append(self.player_hand.cards[1])
                            self.player_hand.cards.pop(1)
                        is_first_round = False
                    else:
                        choice = input("Hit(h), Stick(s), or Double Down(d): ").lower()
                        is_first_round = False
                if choice in ['h','p']:
                    if self.player_hand.get_value() < 21:
                        self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    if split == True:
                        if self.player_hand_split.get_value() < 21:
                            self.player_hand_split.add_card(self.deck.deal())
                        print("--------")
                        self.player_hand_split.display()
                    print()

                    if split == True:
                        if self.player_hand.get_value() > 21 and self.player_hand_split.get_value() > 21:
                            print("You are Bust!")
                            self.losses += 1
                            game_over = True
                    else:
                        if self.player_hand.get_value() > 21:
                            print("You are Bust!")
                            self.losses += 1
                            game_over = True

                elif choice in ['s','d'] or choice == "":
                    player_hand_split_value = 0
                    if choice == 'd':
                        self.player_hand.add_card(self.deck.deal())
                        self.player_hand.display()
                        if split == True:
                            self.player_hand_split.add_card(self.deck.deal())
                            print("--------")
                            self.player_hand_split.display()
                        print()
                    player_hand_value = self.player_hand.get_value()
                    player_hand_split_value = self.player_hand_split.get_value()

                    while self.dealer_hand.get_value() < 17:
                        self.dealer_hand.add_card(self.deck.deal())

                    dealer_hand_value = self.dealer_hand.get_value()

                    player_value = 0
                    if split:
                        if player_hand_value <= 21 and player_hand_split_value <= 21:
                            if player_hand_value == player_hand_split_value:
                                player_value = player_hand_value
                            elif player_hand_value > player_hand_split_value:
                                player_value = player_hand_value
                            else:
                                player_value = player_hand_value_split
                        elif player_hand_value > 21 and player_hand_split_value <= 21:
                            player_value = player_hand_split_value
                        else:
                            player_value = player_hand_value
                    else:
                        player_value = player_hand_value
                    
                    print()
                    print("Final Results")
                    print("-------------")
                    print("You:", player_value)
                    if player_value > 21:
                        print("Dealer Wins!")
                        self.losses += 1
                    else:
                        print("Dealer:", dealer_hand_value)

                        if player_value > dealer_hand_value:
                            print("You Win!")
                            self.wins += 1
                        elif player_value == dealer_hand_value:
                            print("Tie!")
                            self.ties += 1
                        else:
                            if dealer_hand_value <= 21:
                                print("Dealer Wins!")
                                self.losses += 1
                            else:
                                print("You Win!")
                                self.wins += 1
                    game_over = True
            self.num += 1
            again = input("Play Again? [Y/N] ")
            if again.lower() == "n":
                playing = False
                print("Wins: ",self.wins)
                print("Ties: ",self.ties)
                print("Losses: ",self.losses)
            else:
                game_over = False
                print()


if __name__ == "__main__":
    game = Game()
    game.play()
    scoreToAdd = (game.wins-game.losses)/game.num
    with open("player_scores.txt","a") as file:
        file.write("\n"+str("{:.2f}".format(scoreToAdd)))
    file1 = open("player_scores.txt","r")
    scores = file1.read().split("\n")
    plt.hist(scores,100)
    plt.show()
    
