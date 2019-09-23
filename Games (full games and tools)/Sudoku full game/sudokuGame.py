import tkinter as tk
from tkinter import ttk
from sys import exit
from time import sleep
from threading import Thread
from modules.sudoku import Sudoku

class SudokuGame():

    def __init__(self):
        """
        Creates all global variables for the instance, renders the initial game
        elements on the main window and waits for a <return> event ("enter" key
        press on the difficulty Entry box) to call for game_setup(), which
        starts the game up.
        """
        self.grid_gui = []
        self.hidden_sudoku = [] 
        self.revealed_sudoku = []
        self.lives = []
        self.timer_flag = True

        self.main_window = tk.Tk()
        self.main_window.title("Sudoku")
        self.main_window.config(width = 400, height = 500, bg = "black")
        self.main_window.resizable(False, False)
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.main_window.bind("<Key>", self.keydown)
        self.main_window.bind("<Return>", self.return_press)

        self.img_heart = tk.PhotoImage(file="img/heart.png")
        self.img_game_over = tk.PhotoImage(file="img/game_over.png")

        self.lbl_title = ttk.Label(
            text = "S u d o k u", font = ("Arial", 24, "bold"), 
            foreground = "white", background = "black")
        self.lbl_title.place(x = 200, y = 30, anchor = "center")

        self.lbl_diff_text = ttk.Label(
            text = "Difficulty level:", font = self.set_font(18), 
            foreground = "white", background = "black")
        self.lbl_diff_text.place(x = 100, y = 75, anchor = "center")

        self.lbl_diff_meter = tk.Entry(
            "", justify = "center", font = self.set_font(18), 
            borderwidth = "3", name = "diff_meter")
        self.lbl_diff_meter.place(
            x = 220, y = 75, width = 33, height = 27, anchor = "center")

        self.lbl_diff_expl = ttk.Label(
            text = "(Values from 1 to 9 only, enter to start)", 
            font = self.set_font(10), 
            foreground = "white", background = "black")
        self.lbl_diff_expl.place(x = 130, y = 105, anchor = "center")

        self.timer_var = tk.StringVar()
        self.timer_var.set("00:00:00")
        self.timer = ttk.Label(
            textvariable = self.timer_var, font = self.set_font(12), 
            foreground = "black", background = "black")
        self.timer.place(x = 350, y = 484, anchor = "center")

        lbl_author = ttk.Label(
            text = "Designed by R.N.M.C., 2019", font = self.set_font(8), 
            foreground = "gray", background = "black")
        lbl_author.place(x = 85, y = 486, anchor = "center")

        # we need to initialize these two as ttk elements for them to be properly
        # destroyed when the game restarts.
        self.lbl_game_over = ttk.Label()
        self.btn_play_again = ttk.Button()

        self.main_window.mainloop()


    #############################################################################
    ###################### G A M E  F L O W  M E T H O D S ######################
    #############################################################################

    def game_setup(self, game_difficulty):
        """ Sets the game up once the difficulty level is entered. """

        self.grid_gui, self.lives, self.hidden_sudoku, self.revealed_sudoku, self.timer_flag

        # set the timer's flag to True, enabling it to start/restart.
        self.timer_flag = True

        # displays the timer on screen and hides the difficulty explanation text.
        self.timer.config(foreground = "white")
        self.lbl_diff_expl.config(foreground = "black")  

        # generates and places all sudoku grid cells on screen and saves a list
        # containing them to the grid_gui variable.
        self.grid_gui = self.generate_cells()

        # initializes a Sudoku instance, displays the hidden answers to the cells
        # according to the set difficuly, and saves the revealed answers to a list 
        # inside the revealed_sudoku variable.
        self.revealed_sudoku = self.assign_cell_values(game_difficulty)

        # creates and renders the three self.lives on screen, and saves the heart 
        # labels in the lives variable.
        self.lives = self.place_hearts()

        # starts up a new thread which will run the timer.
        if __name__ == '__main__':
            t1 = Thread(target = self.initialize_timer, args=())
            t1.start()


    def generate_cells(self):
        """ 
        Generates all individual sudoku cells, places them on main_window
        and returns a list with them in horizontal order. 
        """
        current_cell = ""
        total_cells = []

        # create all sudoku cells, assign their names equal to the current
        # value of i and append them to a single list.
        for i in range(81):
            current_cell = tk.Entry(
                "", justify = "center", font = self.set_font(18), 
                borderwidth = "3", fg = "gray", name = str(i)
            )
            total_cells.append(current_cell)

        cell_x_coord = 32
        cell_y_coord = 120
            
        for i in range(1, 82):

            # place each cell on the main_window. Range begins at one
            # to make it easier to divide using the % operand below.
            total_cells[i-1].place(
                x = cell_x_coord, y = cell_y_coord, 
                width = 30, height = 30, anchor = "center"
            )
            cell_x_coord += 40

            # add spacing to separate the 3x3 subgrids vertically.
            if i in [27, 54]: cell_y_coord += 7

            # if 9 cells are placed horizontally, move to the next row.
            if i % 9 == 0 and i is not 0:
                cell_y_coord += 40
                cell_x_coord = 32
                continue

            # add spacing to separate the 3x3 subgrids horizontally.
            if i % 3 == 0 and i is not 0:
                cell_x_coord += 7
            
        # return the list of cells.
        return total_cells


    def assign_cell_values(self, difficulty = 5):
        """
        Generates a sudoku list and a deep copy of it from a Sudoku class instance.
        Afterwards, it hides values of the instanced object's list according to the 
        set difficulty and renders the revealed ones to the Entry cells on the 
        displayed on the main_window.
        This method returns the deep-copied list which holds all revealed values
        to be compared with the user inputs while answering, and to fill each
        unanswered cell up when the game ends.
        """

        # initialize a Sudoku instance, get it in a list of its rows as lists,
        # copy it and hide its values according to the set difficulty.
        grid = Sudoku()
        grid_rows = grid.get_sudoku_as_rows()
        grid_copy = grid.deepcopy_sudoku()
        grid.hide_values(difficulty, " ")

        hidden_cell_values = []
        revealed_cell_values = []
        
        # convert both nested lists into a single one each.
        for i in range(9):
            for j in range(9):
                hidden_cell_values.append(grid_rows[i][j])
                revealed_cell_values.append(grid_copy[i][j])
        
        # for the hidden list, cast the revealed values to the sudoku Entry 
        # cells, and change their state to "readonly" to immobilize them.
        for i, cell in enumerate(self.grid_gui):
            if hidden_cell_values[i] is " ":
                continue
            cell.insert(0, str(hidden_cell_values[i]))
            cell.config(state="readonly", foreground = "black")

        # return the list with all revealed values.
        return revealed_cell_values


    def place_hearts(self):
        """ 
        Renders the three lives (hearts) on screen and returns a list
        with their respective label elements.
        """
        hearts = []
        x_pos = 270

        for i in range(3):
            heart = tk.Label(
                image = self.img_heart, borderwidth = 0, highlightthickness = 0)
            heart.place(x = x_pos, y = 63)
            hearts.append(heart)
            x_pos += 40

        return hearts


    def lose_1_life(self):
        """ Destroys one life label element. If none is left, it ends the game. """ 
        life_lost = self.lives.pop()
        life_lost.destroy()

        if not self.lives:
            return self.game_over()


    def game_over(self):
        """
        Stops the timer running in the parallel thread, displays the correct
        answers for all empty Entry cells, creates and places the "Game over"
        icon and the "Play again" button.
        """
        self.btn_play_again, self.timer_flag, self.lbl_game_over
        
        # stops the timer in t1 thread.
        self.timer_flag = False

        # displays the correct answer for each unanswered cell.
        for i, cell in enumerate(self.grid_gui):
            if self.grid_gui[i].cget("state") == "normal":
                cell.delete(0, last=10)
                cell.insert(0, str(self.revealed_sudoku[i]))
                cell.config(state="readonly", foreground = "blue")

        # assigns and places the lbl_game_over and the btn_play_again button.
        self.lbl_game_over = tk.Label(
            image = self.img_game_over, borderwidth = 0, highlightthickness = 0)
        self.lbl_game_over.place(x = 21, y = 5)

        self.btn_play_again = ttk.Button(text = "Play again!", command = self.restart_game)
        self.btn_play_again.place(x = 340, y = 32, anchor="center")


    def restart_game(self):
        """ 
        Destroys each element created after the game started and
        reverts all initial ones to their original state.
        """
        self.lbl_game_over.destroy()
        self.btn_play_again.destroy()
        if self.lives:
            for heart in self.lives:
                heart.destroy()
        for cell in self.grid_gui:
            cell.destroy()
        
        self.timer.config(foreground = "black")
        self.lbl_diff_expl.config(foreground = "white")
        self.lbl_diff_meter.config(
            state = "normal", foreground = "black", background = "white")
        self.lbl_diff_meter.delete(0)


    ############################################################################
    ############### W I N D O W  A N D  W I D G E T  E V E N T S ###############
    ############################################################################

    def keydown(self, e):
        """ Assigns a keydown event to all Entry boxes. """

        if isinstance(e.widget, tk.Entry):

            try:
                # get the content. I there is no content, do nothing.
                a = e.widget.get()[-1]
            except IndexError:
                return

            # delete the previous content.
            e.widget.delete(0, last=10)

            # keep the input only if it is a value between 1 and 9.
            if str(a) in [str(b) for b in range(1,10)]:
                e.widget.insert(0, a)
            else:
                return


    def return_press(self, e):
        """ Assigns a return key event to all Entry boxes """

        if isinstance(e.widget, tk.Entry):

            widget_name = None

            # if the user input is not a number, do nothing.
            try:
                user_input = int(e.widget.get())
            except ValueError:
                return
            
            # if you can't cast the Entry's name to int, then it must be
            # the lbl_diff_meter input. Switch it to "readonly" state and
            # start the game up with the user inputted difficulty.
            try: 
                widget_name = int(str(e.widget)[1:])
            except ValueError:
                e.widget.config(state="readonly", foreground = "#008080")
                return self.game_setup(int(e.widget.get()))

            # the user input is on a sudoku cell and it matches the correct
            # answer, so assign it permanently.
            if self.revealed_sudoku[widget_name] == int(user_input):
                e.widget.delete(0)
                e.widget.insert(0, user_input)
                e.widget.config(state="readonly", foreground = "black")

                # if there are cells yet to be completed, return.
                for cell in self.grid_gui:
                    if cell.cget("state") == "normal":
                        return

                # no more cells to be completed, game is over.
                return self.game_over()
            
            # the user input does not match the correct answer, lose 1 life.
            else:
                self.lose_1_life()
            

    def on_closing(self):
        """ 
        Overrides the main_window's closing functionality to be able to
        kill the parallel thread before exiting the game.
        """
        self.main_window
        self.main_window = None
        exit()


    #############################################################################
    ################# P A R A L L E L  T H R E A D :  T I M E R #################
    #############################################################################

    def initialize_timer(self):
        """ Controls the timer and assigns its value to the timer ttk Label. """
        self.timer_flag, self.main_window
        seconds = 0
        minutes = 0
        hours = 0

        # while main window still exists (the game window is active) and the sudoku 
        # is still playable (current game is not over yet), assign the timer value 
        # to the timer ttk label and count 1 second up. Then sleep for one second 
        # and repeat the process.
        while self.main_window and self.timer_flag and hours < 100:
            
            time = []

            if seconds % 60 == 0 and seconds is not 0:
                seconds = 0
                minutes += 1
                if minutes % 60 == 0 and minutes is not 0:
                    minutes = 0
                    hours += 1     

            if hours < 10: 
                time.append("0" + str(hours))
            else: 
                time.append(str(hours))
            if minutes < 10: 
                time.append(":0" + str(minutes))
            else: 
                time.append(":" + str(minutes))
            if seconds < 10: 
                time.append(":0" + str(seconds))
            else: 
                time.append(":" + str(seconds))

            self.timer_var.set("".join(time))
            seconds += 1
            sleep(1)
        
        # if main_window is active but the sudoku is not rendered on screen yet
        # or the game is over either by winning or losing, it sleeps for one
        # second until a new game begins.
        while self.main_window and not self.timer_flag and hours < 100:
            sleep(1)

        # after the last while clause, if a new game begun, it restarts the timer.
        # if the user closed the game, it returns, killing the thread. 
        if self.main_window:
            return self.initialize_timer()
        else:
            return


    #############################################################################
    ##################### L A Z Y  T Y P I N G  M E T H O D #####################
    #############################################################################

    def set_font(self, size):
        return ("Arial", size, "italic")