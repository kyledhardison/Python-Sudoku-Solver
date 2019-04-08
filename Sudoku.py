#TODO: Write code to verify rows/cols/cells

class Sudoku:
    def __init__(self, filename):
        self.puzzle = []    #array to store original puzzle
        
        self.puzzle = self.read_puzzle(filename)

        self.possible = []  #array to store all possible values for a given cell

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

    #TODO: Finish this guy, might need to be broken into different functions. Maybe add in writing abilities to edit the possible puzzle?
    #Return True if cell value is valid, return false if it's not
    def verify_puzzle(self, puzzle):
        valid = True

        #row verification
        #for i in range(0:9):
            
                
        return(valid)