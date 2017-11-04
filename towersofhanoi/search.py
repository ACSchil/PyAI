from collections import deque
from threading import RLock, Thread
from queue import Queue

from search.node import Node
from towersofhanoi.hanoi import immutable_hanoi


def dls_graph(problem, limit):
    """Depth limited search for hanoi with an explored set."""
    problem.metrics.start()
    explored = set()
    explored.add(immutable_hanoi(problem.initial))
    return recursive_dls_graph(Node(problem.initial), problem, limit, explored)


def dls_forward(problem, limit):
    problem.metrics.start()
    problem.metrics.inc_node()
    return recursive_dls_forward(Node(problem.initial), problem, limit)


def bfs_graph(problem):
    """BFS for hanoi with explored set"""
    problem.metrics.start()
    node = Node(problem.initial)
    problem.metrics.inc_node()
    problem.metrics.node_size(node)
    if problem.goal_test(node.state):
        return solution(node, problem)
    frontier = deque()
    # explored set
    explored = set()
    frontier.append(node)
    explored.add(immutable_hanoi(node.state))
    # explore descendants in order of shallowest
    while frontier:
        problem.metrics.update_max_frontier(len(frontier))
        problem.metrics.update_max_explored(len(explored))
        node = frontier.popleft()
        for child in node.expand(problem):
            problem.metrics.inc_node()
            c = immutable_hanoi(child.state)
            if problem.goal_test(child.state):
                problem.metrics.stop()
                return solution(child, problem)
            if c not in explored:
                frontier.append(child)
                explored.add(c)
    problem.metrics.stop()
    return None


def bidirectional_bfs(problem):
    """BD-BFS for hanoi"""
    problem.metrics.start()
    start_node = Node(problem.initial)
    end_node = Node(problem.end)
    problem.metrics.node_size(start_node)
    problem.metrics.inc_node()
    problem.metrics.inc_node()
    if end_node.state == start_node.state:
        return [start_node]
    # locks for threads starting from the start and end (i.e. solution) of the problem
    explored_e_lock = RLock()
    explored_s_lock = RLock()
    # explored sets as dictionaries to recover the solution. Use locks as these are shared
    explored_e = {}
    explored_e[hash(immutable_hanoi(end_node.state))] = end_node
    explored_s = {}
    explored_s[hash(immutable_hanoi(start_node.state))] = start_node
    # queue for saving the solution from the threads
    solutions = Queue()
    # thread starts from initial state
    thread_s = Thread(target=directional_bfs,
                      args=(problem, start_node, explored_s, explored_s_lock,
                            explored_e, explored_e_lock, solutions, 's'),
                      daemon=True)
    # thread starts from goal state
    thread_e = Thread(target=directional_bfs,
                      args=(problem, end_node, explored_e, explored_e_lock,
                            explored_s, explored_s_lock, solutions, 'e'),
                      daemon=True)
    thread_s.start()
    thread_e.start()
    # s is of the form (intersecting_node (from start direction),
    # intersecting_node.parent (from soultion direction))
    s = solutions.get()
    problem.metrics.stop()
    return bidirectional_solution(s[0], s[1], problem)


def iterative_deepening_forward(problem):
    """Iterative deepening using a depth limited search with an explored list"""
    problem.metrics.start()
    problem.metrics.node_size(Node(problem.initial))
    depth = 0
    while True:
        # print()
        # print()
        # print('===============')
        # print(' Deepened to ', depth)
        # print('===============')
        result = dls_forward(problem, depth)
        if result != 'cutoff':
            problem.metrics.stop()
            return result
        else:
            depth += 1


def iterative_deepening_graph(problem):
    """Iterative deepening using a depth limited search with an explored list"""
    problem.metrics.start()
    problem.metrics.node_size(Node(problem.initial))
    depth = 0
    while True:
        # print()
        # print()
        # print('===============')
        # print(' Deepened to ', depth)
        # print('===============')
        result = dls_graph(problem, depth)
        if result != 'cutoff':
            problem.metrics.stop()
            return result
        else:
            depth += 1


##################
# Without explored
##################


def bfs_tree(problem):
    """BFS for hanoi without explored set"""
    problem.metrics.start()
    node = Node(problem.initial)
    problem.metrics.node_size(node)
    problem.metrics.inc_node()
    if problem.goal_test(node.state):
        return solution(node, problem)
    frontier = deque()
    frontier.append(node)
    # explore descendants in order of shallowest
    while frontier:
        problem.metrics.update_max_frontier(len(frontier))
        problem.metrics.update_max_explored(0)
        node = frontier.popleft()
        for child in node.expand(problem):
            problem.metrics.inc_node()
            if problem.goal_test(child.state):
                problem.metrics.stop()
                return solution(child, problem)
            else:
                frontier.append(child)
    problem.metrics.stop()
    return None


def dls_tree(problem, limit):
    """Depth limited search used for iterative deepening."""
    problem.metrics.start()
    return recursive_dls_tree(Node(problem.initial), problem, limit)


def iterative_deepening_tree(problem):
    """Iterative deepening using a depth limited search with an explored list"""
    problem.metrics.start()
    problem.metrics.node_size(Node(problem.initial))
    depth = 0
    while True:
        # print()
        # print()
        # print('===============')
        # print(' Deepened to ', depth)
        # print('===============')
        result = dls_tree(problem, depth)
        if result != 'cutoff':
            problem.metrics.stop()
            return result
        else:
            depth += 1


##################
# Helper Functions
##################


def directional_bfs(problem, node, my_explored, my_lock, their_explored, their_lock, solutions, direction):
    """Runs a bfs in a given direction. If the search finds an intersection, it pushes the node onto the
    shared solution queue. """
    frontier = deque()
    frontier.append(node)
    with my_lock:
        h = hash(immutable_hanoi(node.state))
        my_explored[h] = node
    # perform bfs
    while frontier:
        problem.metrics.update_max_frontier(len(frontier))
        node = frontier.popleft()
        for child in node.expand(problem):
            problem.metrics.inc_node()
            h = hash(immutable_hanoi(child.state))
            if h in my_explored.keys():
                continue
            # Acquire locks in same order to avoid deadlock
            if direction == 's':
                lock_one = my_lock
                lock_two = their_lock
            else:
                lock_one = their_lock
                lock_two = my_lock
            # if we haven't seen this state, check to see if the other direction has seen it
            with lock_one:
                with lock_two:
                    my_keys = my_explored.keys()
                    problem.metrics.update_max_explored(len(my_keys) +
                                                        len(their_explored.keys()))
                    for key in my_keys:
                        # if the other direction has seen the state the searches have intersected
                        if key in their_explored:
                            if direction == 's':
                                solutions.put((my_explored[key], their_explored[key].parent))
                            else:
                                solutions.put((their_explored[key], my_explored[key].parent))
                            return
            # if there wasn't an intersection, add the generated child to the FIFO queue
            frontier.append(child)
            with my_lock:
                h = hash(immutable_hanoi(child.state))
                my_explored[h] = child


def recursive_dls_graph(node, problem, limit, explored, depth=0):
    """Recursive depth limited search for hanoi; uses an explored set.
    Setting the limit to infinity runs a DFS"""
    problem.metrics.update_max_depth(depth)
    print()
    print('At depth ', depth, ' and limit', limit)
    problem.print_state(node.state)
    if problem.goal_test(node.state):
        problem.metrics.update_max_explored(len(explored))
        problem.metrics.stop()
        return solution(node, problem)
    elif limit == 0:
        problem.metrics.update_max_explored(len(explored))
        problem.metrics.stop()
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            problem.metrics.inc_node()
            c = immutable_hanoi(child.state)
            if c not in explored:
                explored.add(c)
            else:
                continue
            # search deeper
            result = recursive_dls_graph(child, problem, limit - 1, explored, depth + 1)
            # decide if we hit our depth limit, or if we found the solution
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                problem.metrics.update_max_explored(len(explored))
                problem.metrics.stop()
                return result
        # if we didn't hit the depth limit nor did we find a solution, we failed
        if cutoff_occurred:
            problem.metrics.update_max_explored(len(explored))
            problem.metrics.stop()
            return 'cutoff'
        else:
            problem.metrics.update_max_explored(len(explored))
            problem.metrics.stop()
            return 'failure'


def recursive_dls_forward(node, problem, limit, forward_set=set(), depth=0):
    """Recursive depth limited search for hanoi; uses an explored set.
    Setting the limit to infinity runs a DFS"""
    problem.metrics.update_max_depth(depth)
    # print()
    # print('At depth ', depth, ' and limit', limit)
    # problem.print_state(node.state)
    if problem.goal_test(node.state):
        problem.metrics.stop()
        return solution(node, problem)
    elif limit == 0:
        problem.metrics.stop()
        return 'cutoff'
    else:
        forward_set.add(immutable_hanoi(node.state))
        problem.metrics.update_max_explored(len(forward_set))
        cutoff_occurred = False
        for child in node.expand(problem):
            problem.metrics.inc_node()
            c = immutable_hanoi(child.state)
            if c not in forward_set:
                forward_set.add(c)
            else:
                continue
            # search deeper
            result = recursive_dls_forward(child, problem, limit - 1, forward_set, depth + 1)
            # decide if we hit our depth limit, or if we found the solution
            forward_set.remove(c)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                problem.metrics.stop()
                return result
        # if we didn't hit the depth limit nor did we find a solution, we failed
        if cutoff_occurred:
            problem.metrics.stop()
            return 'cutoff'
        else:
            problem.metrics.stop()
            return 'failure'


def recursive_dls_tree(node, problem, limit, depth=0):
    """Recursive depth limited search. Setting the limit to infinity runs a DFS"""
    # if depth == 3 or depth == 5 or depth == 7 or depth == 10 or depth == 15 or depth == 16 or depth == 17:
    #    print(depth)
    problem.metrics.update_max_depth(depth)
    if problem.goal_test(node.state):
        problem.metrics.stop()
        return solution(node, problem)
    elif limit == 0:
        problem.metrics.stop()
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            problem.metrics.inc_node()
            result = recursive_dls_tree(child, problem, limit - 1, depth + 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                problem.metrics.stop()
                return result
        if cutoff_occurred:
            problem.metrics.stop()
            return 'cutoff'
        else:
            problem.metrics.stop()
            return 'failure'


#############################
# Solution Recovery Functions
#############################


def solution(node, problem=None):
    """Returns a deque of the steps required to get from the initial
    state to the goal state, given a node with the goal state whose
    ancestors form a path to the initial state."""
    q = deque()
    n = node
    while True:
        q.appendleft(n)
        try:
            n = n.parent
            if n is None:
                problem.metrics.update_solution_steps(len(q))
                return q
        except AttributeError:
            problem.metrics.update_solution_steps(len(q))
            return q


def bidirectional_solution(start_node, end_node, problem=None):
    """Returns a deque of the steps required to get from the initial
    state to the goal state, given a node with with an intermediary state whose
    ancestors form a path to the initial state, and another node with that's the
    parent of the same intermediary state, but whose ancestors for a path to the
    goal state"""
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
                problem.metrics.update_solution_steps(len(q))
                return q
        except AttributeError:
            problem.metrics.update_solution_steps(len(q))
            return q
