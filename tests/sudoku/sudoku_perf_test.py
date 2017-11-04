import sys
from sudoku import sudoku as sudokusolver
from tests.sudoku.samples.sample_input import *

sys.stdout = open('sudoku_perf.out', 'w')


########################
# Pretty Print of Matrix
########################

def sudoku_printer(matrix):
    n = len(matrix)
    for i in range(0, n):
        if n == 9 and (i == 3 or i == 6):
            for b in range(0, (n + 1) * 3):
                print('-', end='')
            print()
        if n == 6 and (i == 2 or i == 4):
            for b in range(0, (n + 1) * 3):
                print('-', end='')
            print()
        if n == 4 and (i == 2):
            for b in range(0, (n + 1) * 3):
                print('-', end='')
            print()
        for j in range(0, n):
            if n == 9 and (j == 3 or j == 6):
                print('|', end='  ')
            if n == 6 and (j == 3):
                print('|', end='  ')
            if n == 4 and (j == 2):
                print('|', end='  ')
            print(matrix[i][j], end='  ')
        print()


######################################################
# Integration Tests on 4x4 Created by Alex Schillinger
######################################################

p1 = sudokusolver.Problem(sudoku1)
print()
print('testing functions...')
sudoku_printer(p1.initial.board)
print('n = ', p1.n)
print('with subsquare dimmensions: ', p1.subsquare_dimensions)
print('prefilled tiles: ', p1.completed)
state = sudokusolver.SudokuState(p1.initial.board, p1.completed, (0, 0, 0))
actions = p1.actions(state)
print('possible actions: ', actions)
for a in actions:
    new = p1.result(state, a)
    sudoku_printer(new.board)

#################################
# 4x4 Created by Alex Schillinger
#################################

p2 = sudokusolver.Problem(sudoku1)
a2 = sudokusolver.breadth_first_search(p2)
print()
print()
print('#############')
print('# 4x4 example')
print('#############')
print()
print('initial state:')
sudoku_printer(p2.initial.board)
print()
print('final state:')
sudoku_printer(a2)

##############
# Sample A 6x6
##############

p3 = sudokusolver.Problem(sudoku2)
a3 = sudokusolver.breadth_first_search(p3)
print()
print()
print('############################')
print('# 6x6 1st Assignment example')
print('############################')
print()
print('initial state:')
sudoku_printer(p3.initial.board)
print()
print('final state:')
sudoku_printer(a3)

##############
# Sample B 6x6
##############

p4 = sudokusolver.Problem(sudoku3)
a4 = sudokusolver.breadth_first_search(p4)
print()
print()
print('############################')
print('# 6x6 2nd Assignment example')
print('############################')
print()
print('initial state:')
sudoku_printer(p4.initial.board)
print()
print('final state:')
sudoku_printer(a4)

############
# Sample 9x9
############

p5 = sudokusolver.Problem(sudoku4)
p5.metrics.start()
a5 = sudokusolver.breadth_first_search(p5)
p5.metrics.stop()
print()
print()
print('########################')
print('# 9x9 Assignment example')
print('########################')
print()
print('initial state:')
sudoku_printer(p5.initial.board)
print()
print('final state:')
sudoku_printer(a5)
print('solution found in ', p5.metrics.delta())
print('search generated ', p5.metrics.totalnodes(), ' nodes')
p5.metrics.nodesize(sudokusolver.Node(
    sudokusolver.SudokuState(sudoku4, 81, (0, 0, 0))))
print('search required ', p5.metrics.totalmemory(), ' bytes')
print('search peak memory usage: ', p5.metrics.maxnodes(), ' nodes at ', p5.metrics.maxmemory(), ' bytes')

##########################
# "Evil" Difficulty Sudoku
##########################

p6 = sudokusolver.Problem(sudoku5)
p6.metrics.start()
a6 = sudokusolver.breadth_first_search(p6)
p6.metrics.stop()
print()
print()
print('##################')
print('# 9x9 Evil example')
print('##################')
print()
print('initial state:')
sudoku_printer(p6.initial.board)
print()
print('final state:')
sudoku_printer(a6)
print('solution found in ', p6.metrics.delta())
print('search generated ', p6.metrics.totalnodes(), ' nodes')
p6.metrics.nodesize(sudokusolver.Node(
    sudokusolver.SudokuState(sudoku5, 81, (0, 0, 0))))
print('search required ', p6.metrics.totalmemory(), ' bytes')
