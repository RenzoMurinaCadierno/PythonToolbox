'War' Card Game (with some custom rulings)
========================================

Overview
----------------------------------------

This one is a simple console 'War' card game project I've attempted emulating to practise OOP in Python.

I am still pretty new to the language and to the OOP approach, but every single bit of practise counts, right?

Instructions
------------------------------------------

Execute the file and see the results in console. 

Nothing much apart from that. In the end, this was a practise project, so I have added nothing fancy but the game logic itself.

However, nothing stops you from importing it and running it wherever you want. If you are into making a GUI for it, then the game logic is already done and yours to use ;)

About 'War' card game and my custom rulings
------------------------------------------

In 'War', two players take half a stack of the same shuffled deck. 

Each turn, they draw a card from the deck and show it to each other. The one with the highest value adds both cards to the bottom of their deck.

If both players draw a card of the same value, then it is war! Both players draw an additional card without looking at it or showing it to their opponent, and one more card which they show to each another as a normal turn. The player that reveals this new highest value gets to add all of those cards to the bottom of their deck (which should be 6 in this case). If the second shown card for both players have the same value, then the 'War' process is repeated.

A player wins by holding all cards of the deck in their hand, in which case, the game ends.

The additional rule I've added for this game is that once a 'War' resolves, then a normal turn would resolve by drawing three cards. The first two are kept unrevealed and the last one is shown to compare values. The player with the highest value adds all the cards to the bottom of their deck. A normal war after that keeps adding to the following turn's draw stack.

Which means that:

- Before the first war, both players draw and reveal 1 card per turn.
- After a war, each player draw 3 cards per turn and reveal the last one.
- After the second war, each player draw 5 per turn and reveal the last one.
- After the third, 7 per turn, and so on.