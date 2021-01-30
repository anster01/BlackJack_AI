# BlackJack_AI

Contributors: Ani Hazarika

A project to create and analyse the mathematically optimal Blackjack AI.  
https://www.profitsquad.co.uk/blackjack-strategy-how-to-play-perfect-blackjack/ This website (along with many others) describes a mathematically optimal strategy to playing Blackjack giving a chart for easy execution. Even after deploying this strategy, there is always a House Edge of 0.5%, so you win always lose on average 0.5% of your money.

This project is here to test this hypothesis. First I will play Blackjack using my best intuition (interpret that as you like) to play and then see the distribution of wins/losses that I achieve. Then I will make an AI that uses this optimal method and see if it achieves a better outcome than me.  

First, how to play Blackjack:
1. Every player places a bet and then is dealt 2 cards face up. The dealer gives themself 1 card face up and another face down.
2. Starting left from the dealer, the player will have a choice of Hitting, Sticking and Doubling Down. If both of their cards are the same value they could also choose to Split.
3. If Hit is chosen, they are given another card and given this choice again. If Stick is chosen, then they are stuck on the value they are on. If Double Down is chosen, the player will double their bet and then get given 1 (and only 1) more card. If split is chosen, their two cards are split and are used as teh first card in separate hands.
4. If a hand ever has a value above 21, that player is Bust and loses all their bet. The aim is to get as close to 21 as possible without exceeding it.
5. After every player has been, the dealer will then flip over their face down card. If their hand is below 17, they will keep on Hitting until they are above 17 or Bust.
6. If they lose to the dealer, they lose their bet. If they tie, they keep their bet and they win their bet is doubled.

Second, some of the simplifications I've made to do this project:
1. As this is an experiment seeing how this strategy fairs against the house, there will only be one player and the dealer.
2. Only one deck of cards will be used, and the deck will be shuffled after every round.



