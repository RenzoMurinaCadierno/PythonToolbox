from random import randint
from copy import deepcopy

class Sudoku:

    def __init__(self):
        self.regenerate_sudoku()

    
    def regenerate_sudoku(self):
        """
        Generates a 9x9 sudoku grid (or creates a new one if it was 
        already generated). It is stored as a list of 9 lists with
        9 values each.
        """
        tries_limit = 50
        tries = tries_limit + 1

        while tries > tries_limit:

            # constructs the main 9x9 matrix and fills all of its
            # values with None
            mainMatrix = []

            for i in range(9):
                row = []

                for j in range(9):
                    row.append(None)

                mainMatrix.append(row)

            # a nested for loop iterates over the values of each row in
            # the main matrix
            for row in range(9):

                for column in range(9):
                    currentColumn = []

                    # appends each corresponding row value to the
                    # current column.
                    for i in range(9):
                        currentColumn.append(mainMatrix[i][column])

                    # gets 0, 1 or 2 for the submatrixes' respective
                    # columns and rows to identify their position in the
                    # current submatrix. Then, a nested for loop appends 
                    # the values they hold in the mainMatrix index to the 
                    # subMatrix, which are determined by the actual nested 
                    # iteration values plus 0, 1 or 2 for the current 
                    # subColumn and subRow.
                    subColumn = int(column / 3)
                    subRow = int(row / 3)
                    subMatrix = []

                    for a in range(3):

                        for b in range(3):
                            subMatrix.append(
                                mainMatrix[a + subRow*3][b + subColumn*3])
                    
                    # once inside the main while loop, tries is set to 0
                    # so that all of the logic below for successful and
                    # failed value assignments can begin to apply.
                    # rnd value is nullified if it already contains an int
                    # and the current operative row is selected.
                    tries = 0
                    rnd = None
                    currentRow = mainMatrix[row]
 
                    # loops over each value in the current row, column
                    # and submatrix looking for a repeated randomly assigned
                    # number. If found, assigns a new one to the rnd value
                    # and tries again. If there were too many tries, that
                    # probably means an valid value could not be assigned, so 
                    # it forcefully breaks to evade an infinite loop.
                    while rnd in currentRow \
                       or rnd in currentColumn \
                       or rnd in subMatrix:
                        rnd = randint(1,9)
                        tries += 1

                        if tries > tries_limit: 
                            break 
                    
                    # assigns the randomly generated value to the current
                    # row's column index.
                    currentRow[column] = rnd

                    # if the assiged value was an invalid one, then
                    # the tries variable will be higher than the
                    # tries_limit, so it breaks out of the column loop.
                    if tries > tries_limit: 
                        break 
                
                # following the same logic as above, the row loop
                # breaks and falls into the first while loop which
                # resets all values and restarts the process over 
                # again.
                if tries > tries_limit:
                    break
        
        # while loop was escaped with no invalid values, 
        # (tries < tries_limit), which means that a correct
        # sudoku matrix was generated. The process ends.
        self.sudoku = mainMatrix


    def deepcopy_sudoku(self):
        """
        Makes a deep copy of the sudoku list so that you can safely
        store it in a variable and hide the values of the original one 
        without affecting the copied's.
        """
        return deepcopy(self.get_sudoku_as_rows())


    def hide_values(self, difficulty = 5, placeholder = "."):
        """
        Hides the numbers inside the sudoku according to the
        set difficulty.
        The first parameter is the difficulty level (1 to 9).
        The second parameter is the placeholder for the hidden
        numbers. Only a single string character is allowed. 
        It defaults to "." if you do not provide any.
        """
        if difficulty > 9 or difficulty < 0:
            print('Only integers from 0 to 9 are allowed as difficulty level.')
            return

        if type(placeholder) is not str or len(placeholder) > 1:
            print("Use one string character as a placeholder.")
            return

        diffMeter = [a for a in list(range(1,11)) \
                    if a not in list(range(1,difficulty+1))]

        for a in range(9):

            for b in range(9):
                rnd = randint(1, 10)
                if rnd not in diffMeter:              
                    self.sudoku[a][b] = placeholder


    def print_sudoku(self):
        """ Prints the sudoku to console. """
        i = 0

        for row in self.sudoku: 

            if i == 0:
                print("-------------------------")
            
            print("| {} {} {} | {} {} {} | {} {} {} |".format(
                row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            )

            i += 1
            if i % 3 == 0:
                print("-------------------------")


    def invert_sudoku(self):
        """
        Inverts rows and columns.
        Calling this method twice reverts the sudoku back to its
        original state.
        """
        self.sudoku = self.get_sudoku_as_columns()


    def get_sudoku_as_rows(self):
        """
        Returns the complete sudoku as a list composed of 
        its rows as nested lists.
        """      
        return self.sudoku


    def get_sudoku_as_columns(self):
        """
        Returns the complete sudoku as a list composed of 
        its columns as nested lists.
        """   
        sudoku_as_columns = []

        for i in range(9):
            columns = []
            
            for row in self.sudoku:
                columns.append(row[i])
            
            sudoku_as_columns.append(columns)
        
        return sudoku_as_columns 


    def get_sudoku_as_single_list(self):
        """
        Returns the complete sudoku as a list composed
        of the consecutive values of each row.
        """
        single_list = []
        
        for i in range(9):

            for j in range(9):
                single_list.append(self.sudoku[i][j])

        return single_list
