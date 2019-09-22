-----------------------------------------------------------------------
Sudoku
-----------------------------------------------------------------------

A basic sudoku generator with extended functionality.
My initial contribution to what I expect to be a long list of free Python tools of any kind.

-----------------------------------------------------------------------
Usage
-----------------------------------------------------------------------

Just instantiate it and a list of lists containing nine valid sudoku rows will be generated and saved to the variable you assigned. From there on, use any method in the class to manipulate it.

-----------------------------------------------------------------------
Methods (extended functionality)
-----------------------------------------------------------------------

> regenerate_sudoku():
    Generates a 9x9 sudoku grid (or creates a new one if it was already generated). It is stored as a list of 9 lists with 9 values each.

> hide_values(difficulty, placeholder):
    Hides the numbers inside the sudoku according to the set difficulty.
    The first parameter is the difficulty level (1 to 9). 
    The second parameter is the placeholder for the hidden numbers. Only a single string character is allowed. It defaults to "." if you do not provide any.

> deepcopy_sudoku(): 
    Makes a deep copy of the sudoku list so that you can safely store it in a variable and hide the values of the original one without affecting the copied's.

> print_sudoku():
    Prints the sudoku to console.

> invert_sudoku():
    Inverts rows and columns.
    Calling this method twice reverts the sudoku back to its original state.

> get_sudoku_as_rows():
    Returns the complete sudoku as a list composed of its rows as nested lists.

> get_sudoku_as_columns():
    Returns the complete sudoku as a list composed of its columns as nested lists.

> get_sudoku_as_single_list():
    Returns the complete sudoku as a list composed of the consecutive values of each row.

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