from Sudoku import Sudoku
import csv
import time

#assuming that the puzzle is 9x9 and has at least one valid solution

start = time.time()
s = Sudoku('test_puzzle_2.csv')

#This code can be used to print out the puzzle when it's solved:
"""
with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(s.possible)
"""
print("Original Puzzle with 0's as placeholders: ")
s.print_puzzle(s.puzzle)
print('\n')

if(s.solve()):
    print("Solved Puzzle: ")
    s.print_puzzle(s.puzzle_solve)
else:
    print("Invalid puzzle")

end = time.time()

print("Time Elapsed: " + str(end - start))

print("Cycles of solve routime: " + str(s.cycles))