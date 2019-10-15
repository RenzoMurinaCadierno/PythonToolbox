# First thing first:
#   > Make sure the 'cards' folder is in the same path as
#     this .py file.

# try-except clause to cover up the import statement of all tkinter's versions
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import random


def load_images(card_images):
    """Loads all card images (numbers and faces) for each suit and
    store the images and its respective values in the 'card_images'
    list of tuples."""

    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "king", "queen"]

    # get the correct image format depending on the tkinter version
    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # for each suit, retrieve the image for the cards
    # and store them in card_images list of tuples
    for suit in suits:

        # numbers 1 to 10
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # face cards
        for card in face_cards:
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    """Pops the top card of the stack, adds the image to the frame
    passed as an argument, and returns the tuple of the value and
    image of the popped card."""

    # pop the next card off the top of the deck
    #   > pop() will grab it from the bottom of the stack,
    #   > so we use pop(0) to take it from the top.
    next_card = deck.pop(0)

    # and add it back to the bottom of the deck
    deck.append(next_card)

    # add the image to the label and display the label
    tkinter.Label(frame, image=next_card[1], relief="raised")\
        .pack(side="left")

    # and now, return the card's face value
    return next_card


def score_hand(hand):
    """Calculates the total score of all cards in the list.
    Only one ace can hace the value 11, and this will be reduced
    to 1 if the hand would bust."""

    score = 0
    ace = False

    for next_card in hand:

        # get the value of the card
        card_value = next_card[0]

        # if it is an ace and we do not hold one, the value is 11 instead of 1
        if card_value == 1 and not ace:
            ace = True
            card_value = 11

        # add up the value to the score
        score += card_value

        # if we would bust, check if there is an ace and substract
        # 10 from the value (11 - 1). Also, set the ace variable to False.
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def deal_dealer():
    """Since we cannot pass the dealer_card_frame as an argument to the
    command parameter of Button (since it will execute the function
    instantly), we need to specifically create a function that deals
    cards for the player and for the dealer."""

    # calculate and return the score of the dealer's hand.
    dealer_score = score_hand(dealer_hand)

    while 0 < dealer_score < 17:

        # Up to a score of 17 or higher, deal a card to the dealer
        # and append it to their hand.
        dealer_hand.append(deal_card(dealer_card_frame))

        # calculate and return the score of the dealer's hand.
        dealer_score = score_hand(dealer_hand)

        # set the score to the respective label.
        dealer_score_label.set(dealer_score)

    # since the dealer always goes last, we can check for the players's
    # score here, and check if they won or lost.
    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


def deal_player():
    """Almost the same as deal_dealer()"""

    # we append the dealed card to the player's hand.
    player_hand.append(deal_card(player_card_frame))

    # calculate and return the score of the player's hand.
    player_score = score_hand(player_hand)

    # set the score to the respective label.
    player_score_label.set(player_score)

    # if the score surpasses 21, dealer wins.
    if player_score > 21:
        result_text.set("Dealer wins!")


def new_game():
    """Destroys the card frames and recreates them.
    Resets the result label, Resets the hands, deal the first cards
    for the player and the dealer"""

    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    # reset the result label
    result_text.set("")

    # create a list to store dealer's and player's hands.
    dealer_hand = []
    player_hand = []

    # player gets the first card automatically.
    deal_player()

    # deals a card to dealer's hand until they hit 17 or more.
    #   > Check the function deal_dealer
    dealer_hand.append(deal_card(dealer_card_frame))

    # show the initial score for the dealer (otherwise it will be 0)
    dealer_score_label.set(score_hand(dealer_hand))

    # immediately deal the second card to the player
    deal_player()


def shuffle():
    """Shuffles the deck at any point."""

    random.shuffle(deck)


# Set up the screen and frames for the dealer and player

main_window = tkinter.Tk()
main_window.title("Black Jack")
main_window.geometry("500x290")
main_window.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(
    main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(
    card_frame, text="Dealer", background="green", fg="white")\
        .grid(row=0, column=0)
tkinter.Label(
    card_frame, textvariable=dealer_score_label, background="green", fg="white")\
        .grid(row=1, column=0)


# a frame to hold the dealer's card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(
    card_frame, text="Player", background="green", fg="white")\
        .grid(row=2, column=0)
tkinter.Label(
    card_frame, textvariable=player_score_label, background="green", fg="white")\
        .grid(row=3, column=0)

# a frame to hold the player's card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

# A button that deals a card to the dealer's frame (hand)
#   > See def_dealer() docs.
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

# A button that deals a card to the player's frame (hand)
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# A button to start a new game up.
new_game_button = tkinter.Button(button_frame, text="New game", command=new_game)
new_game_button.grid(row=0, column=2)

# And a button to shuffle the deck at any point
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)


# load the cards to a list (format: (index, image object))
cards = []
load_images(cards)

# create a new deck of cards and shuffle them.
deck = list(cards)      # we use the list constructor to create a separate list
                        # from the original one, so it does not conflict when
                        # playing multiple games.

# then shuffle the deck
shuffle()

# create a list to store dealer's and player's hands.
dealer_hand = []
player_hand = []

# start a new game up
new_game()

main_window.mainloop()
