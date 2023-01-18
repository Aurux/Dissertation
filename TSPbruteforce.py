import numpy as np
import itertools

def create_nodes(n):

    node_array = []
    for i in range(n):
        node_array.append(np.round(np.random.rand(2) * 100))

    print(node_array)
    return np.array(node_array)

def create_distance_matrix(node_array):

    totalNodes = len(node_array)
    
    distance_matrix = np.zeros((totalNodes, totalNodes))
    
    for i in range(totalNodes):
        for j in range(i, totalNodes):
            distance = np.sqrt((node_array[i][0] - node_array[j][0])**2 + (node_array[i][1] - node_array[j][1])**2)
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    print(distance_matrix)
    return distance_matrix




create_distance_matrix(create_nodes(5))
