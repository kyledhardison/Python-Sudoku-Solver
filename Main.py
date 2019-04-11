from Sudoku import Sudoku
import csv

#assuming that the puzzle is 9x9 and has at least one valid solution

s = Sudoku('test_puzzle.csv')

#s.print_puzzle(s.puzzle)

#print(s.puzzle)
#print(s.possible)

#print(s.verify_puzzle(s.puzzle))
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(s.possible)