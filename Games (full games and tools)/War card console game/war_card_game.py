#########################################
### WAR GAME with some custom rulings ###
#########################################

# This one is a simple 'War' card game project I've attempted emulating
# to practise OOP in Python. I'm still pretty new to the language and the
# OOP approach, but every single bit of practise counts, right?
#
# In 'War', two players take half a stack of the same shuffled deck.
# Each turn, they draw a card from the deck and show it to each other.
# The one with the highest value adds both cards to the bottom of their
# deck.
#
# If both players draw a card of the same value, then it is war! Both
# players draw an additional card without looking at it or showing it
# to their opponent, and one more card which they show to each another
# as a normal turn. The player that reveals this new highest value gets
# to add all of those cards to the bottom of their deck (which should be
# 6 in this case). If the second shown card for both players have the same
# value, then the 'War' process is repeated.
#
# A player wins by holding all cards of the deck in their hand, in which
# case, the game ends.
#
# The additional rule I've added for this game is that once a 'War' resolves,
# then a normal turn would resolve by drawing three cards. The first two are
# kept unrevealed and the last one is shown to compare values. The player
# with the highest value adds all the cards to the bottom of their deck.
# A normal war after that keeps adding to the following turn's draw stack.
#
# Which means that:
#
# > Before the first war, both players draw and reveal 1 card per turn.
# > After a war, each player draw 3 cards per turn and reveal the last one.
# > After the second war, each player draw 5 per turn and reveal the last one.
# > After the third, 7 per turn, and so on.


from random import shuffle

# Ranks and suites
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    A Deck class to store all 52 cards.

    Attributes:
        _deck (list): a list of tuples that holds the individual cards.

    Methods:
        split(): modifies _deck to hold two lists of half the total cards
                 each.
    """
    def __init__(self):
        self._deck = []
        for s in SUITE:
            for r in RANKS:
                self._deck.append((r, s))

    def split(self):
        """ Splits the deck in half and reassigns _deck to hold both
        stacks in a list of two lists. """

        # Deck must be complete to be split up.
        assert len(self._deck) == 52,\
        "Deck is incomplete, already split up or empty."

        # Shuffle all of the cards
        shuffle(self._deck)

        half_1 = []
        half_2 = []

        # While the deck still has cards, append cards to each half,
        # one by one.
        while self._deck:
            half_1.append(self._deck.pop())
            if self._deck:
                half_2.append(self._deck.pop())

        # Reassign _deck to contain both lists with half a deck each.
        self._deck = [half_1, half_2]

    def __len__(self):
        return len(self._deck)

    def __str__(self):
        return self._deck


class Hand:
    """ A class to store the cards in each players hand and to perform
    all actions available in the game, of course, involving player's
    hands.

    Attributes:
        _hand (list): Holds the player's cards in a list. It starts up
                      by taking a part of the split deck as the initial
                      list.

    Methods:
        convert_values(card) -> str: Takes a card tuple and convert its
                                     value to str. Useful to transform 'J',
                                     'Q', 'K' and 'A' cards to their
                                     corresponding values.
        add(list): Takes a list of card tuples and adds them to the
                   bottom of the hand (or player's deck, it is the same).
        remove(list): Takes a list of tuples and removes them from the
                      player's hand if they exist there.
        pick(num) -> list: Select the first num occurances of tuples of
                           cards in the player's hand and returns a list
                           them in a list of tuples.
    """

    @staticmethod
    def convert_values(card):
        """ Evaluates the rank of the card tuple passed as an argument
        to return its proper integer value as a string. """

        value = card[0]

        if value == 'J':
            value = '11'
        elif value == 'Q':
            value = '12'
        elif value == 'K':
            value = '13'
        elif value == 'A':
            value = '14'

        return value

    def __init__(self, deck):
        assert deck, "Deck empty, cannot create hand."

        self._hand = deck._deck.pop()
        print(self._hand)

    def add(self, cards):
        """ Appends the list of card tuples (cards) to _hand list. """

        assert cards, "Pass a list of minimum 1 card to remove."
        for card in cards:
            self._hand.append(card)

    def remove(self, cards):
        """ Removes the list of card tuples (cards) from _hand list. """

        assert cards, "Pass a list of minimum 1 card to remove."
        for card in cards:
            if card in self._hand:
                self._hand.pop(self._hand.index(card))

    def pick(self, num):
        """ Creates and returns a list num cards from the top of _hand
        list. """

        if len(self._hand) < num:
            num = len(self._hand)

        return [self._hand[i] for i in range(0, num)]

    def __len__(self):
        return len(self._hand)

    def __str__(self):
        return str(self._hand)

class Player:
    """
    A class to initialize a particular player's hand. Only one deck
    splitted in half is available at a time, so only two players are
    allowed per game.
    """

    def __init__(self, deck):
        self.hand = Hand(deck)


def game_flow(p1_hand, p2_hand, quantity, war):
    """
    Main game function. Controls the game flow until a player holds all
    52 cards in their hands, in which case, it returns.
    It picks up cards for both players hands to compare the ranks and calls
    for the corresponding methods to add or remove them to those hands.
    It also summons 'war' when the values of the picked card are the same,
    stacking up the cards and drawing again to resolve it.
    """

    # If any hand is empty at the beginning of the function, return out
    # of it to end the game.
    if not p1_hand or not p2_hand:
        return

    # First check after that would require us to know if both player hold
    # to resolve a war (if their hands are equal to the current stack
    # when war is triggered). If so, set the quantity to be checked to
    # the lowest hand length.
    elif war and (len(p1_hand) in [quantity, quantity+1] or
    len(p2_hand) in [quantity, quantity+1]):
        quantity = len(p1_hand) if len(p1_hand) < len(p2_hand) else len(p2_hand)

    # If the length of the lowest-sized hand is exactly equal to the
    # current stack when war is triggered, we set the quantity to be
    # itself plus 1, in order to make convert_values() down below work.
    elif war and (len(p1_hand) <= quantity or len(p2_hand) <= quantity):
        quantity += 1

    # If war was triggered without hand restrictions, then add two to
    # the current quantity, which sums up to the number of cards to be
    # picked up to resolve the turn.
    elif war:
        quantity += 2

    # After all checks, we can assume this one is a normal turn, so set
    # the amount of cards to be drawn and checked to one.
    else:
        quantity = 1


    while p1_hand or p2_hand:

        # Fill up the stacks of player drawn cards by picking them up
        # according to the current turn's quantity (normally one per
        # turn. On war resolving, 2. On turn-stacked-war, 3, and so on).
        p1_stack = p1_hand.pick(quantity)
        p2_stack = p2_hand.pick(quantity)

        # Try converting the values for each rank of the cards in both
        # player's stacks. If there are no cards to convert, an
        # IndexError will rise, which we catch to return out of
        # game_flow() and end the game.
        try:
            p1_value = int(Hand.convert_values(p1_stack[quantity-1]))
            p2_value = int(Hand.convert_values(p2_stack[quantity-1]))

        except IndexError:
            print(f'P1 final hand: {p1_hand}')
            print(f'P2 final hand: {p2_hand}')

            # Game finishes once no cards are in hand, which rises
            # an index error in the try block
            return

        print("New turn")

        # Inform the players of their current hands before any calculations.
        print_before(p1_hand, p2_hand)

        # If player 1's drawn card has a value higher than player 2's.
        # So, remove the stacked cards from each player's hand and append
        # the stack to player 1's hand.
        if p1_value > p2_value:
            p1_hand.remove(p1_stack)
            p2_hand.remove(p2_stack)
            p1_hand.add(p1_stack + p2_stack)

        # Same logic as above, but for player 2's winning.
        elif p1_value < p2_value:
            p1_hand.remove(p1_stack)
            p2_hand.remove(p2_stack)
            p2_hand.add(p1_stack + p2_stack)

        else:
            # Both players drew a card of the same value. It's war!

            print("Same values! WAR!")

            # First, check if any player holds less or equal amount of
            # cards than the required quantity for war. If they do, then
            # nothing can be compared. (Only the card flipped that
            # triggered war, and that's it). So, add the stuck player's
            # hand to the opponent's hand and call game_flow() again to
            # end the game on the first line.
            if len(p1_hand) <= quantity:
                p2_hand.add(p1_hand(p1_stack))
                p1_hand.remove(p1_hand(p2_stack))
                game_flow(p1_hand, p2_hand, len(p1_hand), True)

            # Same check as above.
            elif len(p2_hand) <= quantity:
                p1_hand.add(p2_hand(p1_stack))
                p2_hand.remove(p2_hand(p2_stack))
                game_flow(p1_hand, p2_hand, len(p2_hand), True)

            # War was triggered and both players hold cards to resolve it,
            # call it! The new quantity of cards to pick in the war would
            # be the current one plus the amount determined in the 'if'
            # check at the beginning of game_flow()
            else:
                print("Entering war")
                game_flow(p1_hand, p2_hand, quantity, True)

        # The turn ended, inform the current results.
        print_after(p1_hand, p2_hand)


def print_before(p1_hand, p2_hand):
    """ A print function to display the players' hands at the
    beginning of the turn. """

    print("Turn")
    print(f'Before turn: p1 -{len(p1_hand)}- {p1_hand}')
    print(f'Before turn: p2 -{len(p2_hand)}- {p2_hand}')

def print_after(p1_hand, p2_hand):
    """ A print function to display the players' hands at the
    end of the turn. """

    print(f'After turn: p1 -{len(p1_hand)}- {p1_hand}')
    print(f'After turn: p2 -{len(p2_hand)}- {p2_hand}')
    print("-" * 120)


def main():

    print("It's war time! Let's go!")

    # Initialize a deck instance and split it up.
    deck = Deck()
    deck.split()

    # Initialize both player's instances, which will create their hands.
    p1 = Player(deck)
    p2 = Player(deck)

    # Let the game begin!
    game_flow(p1.hand, p2.hand, 1, False)

    print("-" * 120)
    print("Game over! Re-run the program to play again.")


if __name__ == '__main__':
    main()
