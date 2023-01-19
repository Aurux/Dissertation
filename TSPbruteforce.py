import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt




def create_nodes(n):

    node_array = []
    for i in range(n):
        node = np.round(np.random.rand(2) * 100)
        node_array.append(node)
        plt.plot(node[0], node[1], "ro")
        plt.text(node[0] * (1 + 0.01), node[1] * (1 + 0.01), i)


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

def brute_force(node_array):
    
    distance_matrix = create_distance_matrix(node_array)
    perms = [list(i) for i in permutations(range(0,len(node_array)))]
    bestLength = 1000000000000
    
    for perm in perms:
        permLen = calculateLength(distance_matrix, perm)
        if permLen < bestLength:
            bestLength = permLen
            bestPerm = perm

    print(perms)
    print(len(perms))

    
    print("Best permutation = ", bestPerm)

    return bestPerm

def calculateLength(distance_matrix, permutation):
    print("current perm: ",permutation)
    sum = 0

    for i in range(len(permutation)):
        x = i % len(permutation)
        y = (i+1) % len(permutation)

        print(permutation[x])
        sum += distance_matrix[permutation[x], permutation[y]]
    
    return sum


def main():
    fig = plt.figure()
    brute_force(create_distance_matrix(create_nodes(4)))

    plt.grid()
    plt.show()

main()