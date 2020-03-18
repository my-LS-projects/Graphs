# Write a function that takes a 2D binary array
# and returns the number of "1" islands
# an island consists of 1s that are connected to
# the N, S, E, W
# For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0],
#            [1, 1, 0, 0, 0]
# ]
# island_counter(islands) # returns 4

# Translate problem into graph terminlogy
# Build graph
# Traverse graph


def island_counter(matrix):
    # created visited matrix
    visited = []
    for i in range(len(matrix)):  # len(matrix)gets = height of matrix
        visited.append([False] * len(matrix[0]))  # generates columns of False
    # for all nodes
    islands_count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # if node is not visited:
            if not visited[row][col]:
                # mark visited
                if matrix[row][col] == 1:
                    # traverse all connected nodes, marking as visited
                    visited = dft(row, col, matrix, visited)
                    # increment visited count
                    islands_count += 1

def dft(row, col, matrix, visited):
    # do a depth first traversal
    # return updated visited matrix
    # with all connected components marked as visited