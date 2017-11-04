from tests.towersofhanoi.hanoi_perf_harness import *

orig_stdout = sys.stdout
f = open('hanoi_perf.out', 'w')
sys.stdout = f

##################
# Disc Scale tests
##################

test_dfs_tree(3, 3, 3, 30, 'classic')
test_dfs_graph(3, 3, 3, 30, 'classic')
test_dfs_forward(3, 3, 3, 30, 'classic')
test_bfs_tree(3, 3, 3, 30, 'classic')
test_bfs_graph(3, 3, 3, 30, 'classic')
test_id_tree(3, 3, 3, 30, 'classic')
test_id_graph(3, 3, 3, 30, 'classic')
test_id_forward(3, 3, 3, 30, 'classic')
test_bdbfs(3, 3, 3, 30, 'classic')

#################
# Peg Scale tests
#################

test_dfs_tree(3, 30, 3, 3, 'classic')
test_dfs_graph(3, 30, 3, 3, 'classic')
test_dfs_forward(3, 30, 3, 3, 'classic')
test_bfs_tree(3, 30, 3, 3, 'classic')
test_bfs_graph(3, 30, 3, 3, 'classic')
test_id_tree(3, 30, 3, 3, 'classic')
test_id_graph(3, 30, 3, 3, 'classic')
test_id_forward(3, 30, 3, 3, 'classic')
test_bdbfs(3, 30, 3, 3, 'classic')

############################
# Peg/Disc Interaction tests
############################

test_dfs_tree(3, 5, 3, 5, 'classic')
test_dfs_graph(3, 5, 3, 5, 'classic')
test_dfs_forward(3, 5, 3, 5, 'classic')
test_bfs_tree(3, 5, 3, 5, 'classic')
test_bfs_graph(3, 5, 3, 5, 'classic')
test_id_tree(3, 5, 3, 5, 'classic')
test_id_graph(3, 5, 3, 5, 'classic')
test_id_forward(3, 5, 3, 5, 'classic')
test_bdbfs(3, 5, 3, 5, 'classic')

#########################
# Cyclic Disc Scale tests
#########################

test_dfs_tree(3, 3, 3, 30, 'classic')
test_dfs_graph(3, 3, 3, 30, 'classic')
test_dfs_forward(3, 3, 3, 30, 'classic')
test_bfs_tree(3, 3, 3, 30, 'classic')
test_bfs_graph(3, 3, 3, 30, 'classic')
test_id_tree(3, 3, 3, 30, 'classic')
test_id_graph(3, 3, 3, 30, 'classic')
test_id_forward(3, 3, 3, 30, 'classic')
test_bdbfs(3, 3, 3, 30, 'classic')

########################
# Cyclic Peg Scale tests
########################

test_dfs_tree(3, 30, 3, 3, 'classic')
test_dfs_graph(3, 30, 3, 3, 'classic')
test_dfs_forward(3, 30, 3, 3, 'classic')
test_bfs_tree(3, 30, 3, 3, 'classic')
test_bfs_graph(3, 30, 3, 3, 'classic')
test_id_tree(3, 30, 3, 3, 'classic')
test_id_graph(3, 30, 3, 3, 'classic')
test_id_forward(3, 30, 3, 3, 'classic')
test_bdbfs(3, 30, 3, 3, 'classic')

print()
print("done!")
sys.stdout = orig_stdout
f.close()
