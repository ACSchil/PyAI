from collections import deque
from threading import Lock, Thread
from queue import Queue

from search.node import Node


def bfs(problem):
    """General BFS"""
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return solution(node)
    frontier = deque()
    explored = set()
    frontier.append(node)
    explored.add(node.state)
    while frontier:
        node = frontier.popleft()
        for child in node.expand(problem):
            if problem.goal_test(child.state):
                return solution(child)
            if child.state not in explored:
                frontier.append(child)
                explored.add(child.state)
    return None


def bidirectional_bfs(problem):
    start_node = Node(problem.initial)
    end_node = Node(problem.end)
    if end_node.state == start_node.state:
        return [start_node]
    explored_e_lock = Lock()
    explored_s_lock = Lock()
    explored_e = {}
    explored_e[hash(end_node.state)] = end_node
    explored_s = {}
    explored_s[hash(start_node.state)] = start_node
    solutions = Queue()
    thread_s = Thread(target=directional_bfs,
                      args=(problem, start_node, explored_s, explored_s_lock,
                            explored_e, explored_e_lock, solutions, 's'),
                      daemon=True)
    thread_e = Thread(target=directional_bfs,
                      args=(problem, end_node, explored_e, explored_e_lock,
                            explored_s, explored_s_lock, solutions, 'e'),
                      daemon=True)
    thread_s.start()
    thread_e.start()
    s = solutions.get()
    return bidirectional_solution(s[0], s[1])


def directional_bfs(problem, node, my_explored, my_lock, their_explored, their_lock, solutions, direction):
    frontier = deque()
    frontier.append(node)
    with my_lock:
        h = hash(node.state)
        my_explored[h] = node
    while frontier:
        # ssleep(1)
        node = frontier.popleft()
        # print(direction + ':' + node.state)
        for child in node.expand(problem):
            h = hash(child.state)
            if h in my_explored.keys():
                continue
            with their_lock:
                with my_lock:
                    my_keys = my_explored.keys()
                    for key in my_keys:
                        if key in their_explored:
                            if direction == 's':
                                solutions.put((my_explored[key], their_explored[key].parent))
                            else:
                                solutions.put((their_explored[key], my_explored[key].parent))
                            return
            frontier.append(child)
            with my_lock:
                h = hash(child.state)
                my_explored[h] = child


def bidirectional_iterative_deepening(problem):
    print('nyi')


def recursive_dls(node, problem, limit):
    # print(node.state)
    if problem.goal_test(node.state):
        return solution(node)
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            result = recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return 'failure'


# dfs when limit = infinity
def dls(problem, limit):
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening(problem):
    depth = 0
    while True:
        result = dls(problem, depth)
        if result != 'cutoff':
            return result
        else:
            depth += 1


def solution(node):
    q = deque()
    n = node
    while True:
        q.appendleft(n)
        try:
            n = n.parent
            if n is None:
                return q
        except AttributeError:
            return q


def bidirectional_solution(start_node, end_node):
    q = deque()
    n = start_node
    while True:
        q.appendleft(n)
        try:
            n = n.parent
            if n is None:
                break
        except AttributeError:
            break
    n = end_node
    while True:
        q.append(n)
        try:
            n = n.parent
            if n is None:
                return q
        except AttributeError:
            return q
