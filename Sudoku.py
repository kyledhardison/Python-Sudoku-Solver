class Sudoku:
    def __init__(self, filename):
        #TODO: May change puzzle from a list to a Dict, may be better for keeping track of possible numbers left
        self.puzzle = []    #array to store original puzzle
        
        self.puzzle = self.read_puzzle(filename)

        self.possible = []  #array to store all possible values for a given cell

        templist = []
        for k in range(0, 9):
             templist.append('123456789')

        for i in range(0, 9):
            self.possible.append(list(templist))  #Populating possible list with values

        for i in range(0,9):
            for j in range(0,9):
                if(self.puzzle[i][j]):
                    self.possible[i][j] = ''.join([c for c in self.possible[i][j] if c in self.puzzle[i][j]])   #Removing all values from possible array that are given in the puzzle

        del templist


    #Parses comma separated .csv file and returns array with its contents
    def read_puzzle(self, filename):
        puzzle = []

        for line in open(filename):
            line = line.replace('\n', '')
            puzzle.append(line.split(','))
        return puzzle


    #Function to print formatted puzzle
    def print_puzzle(self):

        print('-------------------')    
        
        for i in range(0, 9):
            print("|", end='')

            for j in range(0,9):
                if(self.puzzle[i][j]):
                    print(self.puzzle[i][j] + '|', end='')
                else:
                    print(" |", end='')
            print('')
            print('-------------------')