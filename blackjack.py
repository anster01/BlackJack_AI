from blackjack_card import Card
from blackjack_deck import Deck
from blackjack_hand import Hand
  

class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def play(self):
        playing = True

        while playing:
            self.deck = Deck()
            self.deck.shuffle()

            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer=True)

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())

            print("You:")
            self.player_hand.display()
            print()
            print("Dealer:")
            self.dealer_hand.display()
            print()

            game_over = False

            while not game_over:
                has_blackjack = (self.player_hand.get_value() == 21)
                choice = ""
                if not has_blackjack:
                    choice = input("Hit(h), Stick(s), or Double Down(d): ").lower()
                if choice in ['h']:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                    print()

                    if self.player_hand.get_value() > 21:
                        print("You are Bust!")
                        self.losses += 1
                        game_over = True

                elif choice in ['s','d']:
                    if choice == 'd':
                        self.player_hand.add_card(self.deck.deal())
                        self.player_hand.display()
                        print()
                    player_hand_value = self.player_hand.get_value()

                    while self.dealer_hand.get_value() < 17:
                        self.dealer_hand.add_card(self.deck.deal())

                    dealer_hand_value = self.dealer_hand.get_value()
                    
                    print()
                    print("Final Results")
                    print("-------------")
                    print("You:", player_hand_value)
                    print("Dealer:", dealer_hand_value)

                    if player_hand_value > dealer_hand_value:
                        print("You Win!")
                        self.wins += 1
                    elif player_hand_value == dealer_hand_value:
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
