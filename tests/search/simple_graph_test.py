from tests.search.simple_graph import Problem
from search.searching import *

problem = Problem()

bfs_solution = bfs(problem)

while True:
    try:
        n = bfs_solution.popleft()
        print(n.state, end=' ')
    except IndexError:
        print()
        break

dfs_solution = dls(problem, 10)

while True:
    try:
        n = dfs_solution.popleft()
        print(n.state, end=' ')
    except IndexError:
        print()
        break

iterative_deepening_solution = iterative_deepening(problem)

while True:
    try:
        n = iterative_deepening_solution.popleft()
        print(n.state, end=' ')
    except IndexError:
        print()
        break

bi_bfs_solution = bidirectional_bfs(problem)

while True:
    try:
        n = bi_bfs_solution.popleft()
        print(n.state, end=' ')
    except:
        print()
        break
