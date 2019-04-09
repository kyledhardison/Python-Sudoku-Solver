#TODO: Write code to verify rows/cols/cells

class Sudoku:
    def __init__(self, filename):
        self.puzzle = []    #array to store original puzzle
        
        self.puzzle = self.read_puzzle(filename)

        #Defines the 9 3x3 cells in a sudoku puzzle.
        #Ex: self.cells[0][0] would return (0, 0), the top left entry in the top left cell
        #TODO: Find way to reference peers from the 3x3 cell given a box's coordinates
        self.cells = {
            0 : { 0 : (0, 0) , 1 : (0, 1), 2 : (0, 2),  3 : (1, 0) , 4 : (1, 1), 5 : (1, 2),  6 : (2, 0) , 7 : (2, 1), 8 : (2, 2)},
            1 : { 0 : (0, 3) , 1 : (0, 4), 2 : (0, 5),  3 : (1, 3) , 4 : (1, 4), 5 : (1, 5),  6 : (2, 3) , 7 : (2, 4), 8 : (2, 5)},
            2 : { 0 : (0, 6) , 1 : (0, 7), 2 : (0, 8),  3 : (1, 6) , 4 : (1, 7), 5 : (1, 8),  6 : (2, 6) , 7 : (2, 7), 8 : (2, 8)},
            
            3 : { 0 : (3, 0) , 1 : (3, 1), 2 : (3, 2),  3 : (4, 0) , 4 : (4, 1), 5 : (4, 2),  6 : (5, 0) , 7 : (5, 1), 8 : (5, 2)},
            4 : { 0 : (3, 3) , 1 : (3, 4), 2 : (3, 5),  3 : (4, 3) , 4 : (4, 4), 5 : (4, 5),  6 : (5, 3) , 7 : (5, 4), 8 : (5, 5)},
            5 : { 0 : (3, 6) , 1 : (3, 7), 2 : (3, 8),  3 : (4, 6) , 4 : (4, 7), 5 : (4, 8),  6 : (5, 6) , 7 : (5, 7), 8 : (5, 8)},

            6 : { 0 : (6, 0) , 1 : (6, 1), 2 : (6, 2),  3 : (7, 0) , 4 : (7, 1), 5 : (7, 2),  6 : (8, 0) , 7 : (8, 1), 8 : (8, 2)},
            7 : { 0 : (6, 3) , 1 : (6, 4), 2 : (6, 5),  3 : (7, 3) , 4 : (7, 4), 5 : (7, 5),  6 : (8, 3) , 7 : (8, 4), 8 : (8, 5)},
            8 : { 0 : (6, 6) , 1 : (6, 7), 2 : (6, 8),  3 : (7, 6) , 4 : (7, 7), 5 : (7, 8),  6 : (8, 6) , 7 : (8, 7), 8 : (8, 8)},
        }

        self.possible = []  #array to store all possible values for a given cell with strings

        templist = []
        for _ in range(0, 9):
             templist.append('123456789')

        for i in range(0, 9):
            self.possible.append(list(templist))  #Populating possible list with values

        for i in range(0,9):
            for j in range(0,9):
                if(self.puzzle[i][j] != '0'):
                    self.possible[i][j] = ''.join([c for c in self.possible[i][j] if c in self.puzzle[i][j]])   #Removing all values from possible array that are given in the puzzle

        del templist

        #TODO: process initial numbers and remove them from their peer's possibility list



    #Parses comma separated .csv file and returns array with its contents
    def read_puzzle(self, filename):
        puzzle = []

        for line in open(filename):
            line = line.replace('\n', '')
            puzzle.append(line.split(','))
        
        #Adding 0's as placeholders, easier to work with than blank strings
        for i in range(0,9):
            for j in range(0,9):
                if(not puzzle[i][j]):
                    puzzle[i][j] = '0'

        return puzzle


    #Function to print formatted puzzle
    def print_puzzle(self, puzzle):
        print('-------------------')    
        for i in range(0, 9):
            print("|", end='')

            for j in range(0,9):
                print(puzzle[i][j] + '|', end='')
            print('')
            print('-------------------')

    #Verifies the given row for correctness
    def verify_row(self, puzzle, row):
        row_numbers = '123456789'
        for i in puzzle[row]:
            if(i != '0'):
                if(row_numbers.find(i) >= 0):
                    row_numbers = row_numbers.replace(i, '')
                else:
                    return False
        return True

    #Verifies the given column for correctness
    def verify_col(self, puzzle, col):
        col_numbers = '123456789'
        for i in range(0,9):
            if(puzzle[i][col] != '0'):
                if(col_numbers.find(puzzle[i][col]) >= 0):
                    col_numbers = col_numbers.replace(puzzle[i][col], '')
                else:
                    return False
        return True

    #Verifies the given 3x3 cell for correctness
    def verify_cell(self, puzzle, cell_index):
        cell_numbers = '123456789'
        for box in self.cells[cell_index]:
            #This looks complicated but it's just stepping through individual boxes like the rest of the "verify_*" methods
            if(puzzle[self.cells[cell_index][box][0]][self.cells[cell_index][box][1]] != '0'):
                if(cell_numbers.find(puzzle[self.cells[cell_index][box][0]][self.cells[cell_index][box][1]]) >= 0):
                    cell_numbers = cell_numbers.replace(puzzle[self.cells[cell_index][box][0]][self.cells[cell_index][box][1]], '')
                else:
                    return False
        return True


    #Return True if entire puzzle is valid, return false if it's not
    #NOTE: Valid != correct/solved
    def verify_puzzle(self, puzzle):
        for i in range(0,9):
            if(not (self.verify_row(puzzle, i) and self.verify_col(puzzle, i) and self.verify_cell(puzzle, i))):
                return False
        return True
            
