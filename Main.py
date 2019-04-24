from Sudoku import Sudoku
import csv
import time
import os.path

#Kyle Hardison & Sarah Evans Final Project
#Sudoku Solver
#Assuming that the puzzle is 9x9, in .csv format, and has at least one valid solution

file_string = ""

#Allowing the user to select which file they want to solve
while True:
    file_string = input("Enter the file name of the puzzle you want to solve (Ex: puzzle_1.csv): ")
    if(os.path.isfile(file_string)):
        print("")
        print("")
        break
    else:
        print("Please enter a valid file name. ")


start = time.time()
s = Sudoku(file_string)


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