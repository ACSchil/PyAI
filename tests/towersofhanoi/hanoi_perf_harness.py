import sys

from towersofhanoi.hanoi import TowersOfHanoi, CyclicHanoi
from towersofhanoi import search


def test_dfs_graph(p_min, p_max, d_min, d_max, type):
    print()
    print('=============')
    print(' DFS (GRAPH) ')
    print('=============')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.dls_graph(problem, sys.maxsize)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_dfs_tree(p_min, p_max, d_min, d_max, type):
    print()
    print('============')
    print(' DFS (TREE) ')
    print('============')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.dls_tree(problem, sys.maxsize)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_dfs_forward(p_min, p_max, d_min, d_max, type):
    print()
    print('===============')
    print(' DFS (FORWARD) ')
    print('===============')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.dls_forward(problem, sys.maxsize)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_bfs_tree(p_min, p_max, d_min, d_max, type):
    print()
    print('============')
    print(' BFS (TREE) ')
    print('============')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.bfs_tree(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_bfs_graph(p_min, p_max, d_min, d_max, type):
    print()
    print('=============')
    print(' BFS (GRAPH) ')
    print('=============')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p, ' for type ', type)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.bfs_graph(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_id_forward(p_min, p_max, d_min, d_max, type):
    print()
    print('===============================')
    print(' ITERATIVE DEEPENING (FORWARD) ')
    print('===============================')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p, ' for type ', type)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.iterative_deepening_forward(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_id_graph(p_min, p_max, d_min, d_max, type):
    print()
    print('=============================')
    print(' ITERATIVE DEEPENING (GRAPH) ')
    print('=============================')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p, ' for type ', type)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.iterative_deepening_graph(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_id_tree(p_min, p_max, d_min, d_max, type):
    print()
    print('============================')
    print(' ITERATIVE DEEPENING (TREE) ')
    print('============================')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p, ' for type ', type)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.iterative_deepening_tree(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()


def test_bdbfs(p_min, p_max, d_min, d_max, type):
    print()
    print('===================')
    print(' BIDIRECTIONAL BFS ')
    print('===================')
    for p in range(p_min, p_max + 1):
        for d in range(d_min, d_max + 1):
            print(type, ' problem d = ', d, ', p = ', p)
            if type == 'classic':
                problem = TowersOfHanoi(d, p)
            elif type == 'cyclic':
                problem = CyclicHanoi(d, p)
            else:
                continue
            try:
                search.bidirectional_bfs(problem)
            except Exception as e:
                print('An exception occurred: {}'.format(e))
                problem.metrics.get_metrics()
                return
            problem.metrics.get_metrics()
