-----------------------------------------------------------------------
Sudoku Game
-----------------------------------------------------------------------

A fully functional Sudoku game made with Tkinter, using the Sudoku Generator script in this repository.

For this app, I have used the simplest expression of the Tkinter module as I possibly could since this is my initial attempt at it. All elements are fixed and I did not use the grid() or pack() functions as I wanted to begin with the basics of the basics first.

This one is my second contribution to what I expect to be a long list of free Python tools of any kind.

-----------------------------------------------------------------------
Usage
-----------------------------------------------------------------------

Import this module and instantiate a SudokuGame object. A Tkinter root window will launch and the game will begin (make sure to have 'modules' and 'img' directories in the same path as this script for it to work).

Once in game, type a value from 1 to 9 in the difficulty level Entry box that shows up and the Sudoku will generate itself automatically, along with a timer which will start counting up. The game has no time limit (the timer is just for you to keep track of how long it takes to solve the puzzle), but it only gives you three lives to play each sudoku, so mind your answers!

The game gives you the option to play again whether you win or not.

The timer runs in a parallel thread, which will terminate simultaneously alongside the main one when you close the app. Speaking of which, since this app is basically a Tkinter window, keep in mind that it will block the thread from where you instantiate it, so you might want to run it on a secondary thread.

The code is fully commented, but feel free to ask me anything you need to know in detail.

-----------------------------------------------------------------------
About the author
-----------------------------------------------------------------------

Hey! I'm Renzo Nahuel Murina Cadierno (a.k.a. "Max"), a pleasure to meet you!

I've been studying programming for a little more than half a year to date and I find my love for it keeps growing ever since I wrote my first "Hello World".

Out of my three main languages (Java, JS and Python) this is the one I like and enjoy the most, so, naturally, I cannot wait to keep on sharing my attempts at it with you.

Of course, the code certainly looks messy and can be improved lots, I know. I still have a long way ahead to learn, and certainly that is the thing I'm most excited for.
I dream of the day I can drop my current job to dedicate my entire career to the marvelous world of programming. Until then, I'm pretty much satisfied with learning, practising and sharing my improvements whenever possible.

Feel free to contact me at nmcadierno@hotmail.com with any questions.

Thanks for reading!