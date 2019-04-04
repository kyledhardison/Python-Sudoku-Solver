class Sudoku:
    def __init__(self, filename):
        #TODO: May change puzzle from a list to a Dict, may be better for keeping track of possible numbers left
        self.puzzle = []
        self.puzzle = self._read_puzzle(filename)


    #Parses comma separated .csv file and returns array with its contents
    def _read_puzzle(self, filename):
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