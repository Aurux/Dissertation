import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
import time


fig = plt.figure()

def create_nodes(n):

    node_array = []
    for i in range(n):
        node = np.round(np.random.rand(2) * 100)
        node_array.append(node)
        


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

    
    return distance_matrix

def brute_force(node_array):
    
    distance_matrix = create_distance_matrix(node_array)
    perms = [list(i) for i in permutations(range(0,len(node_array)))]
    bestLength = 1000000000000
    
    for perm in perms:
        permLen = calculateLength(distance_matrix, perm)
        draw_graph(node_array, perm, permLen, False)
        if permLen < bestLength:
            bestLength = permLen
            bestPerm = perm

    

    
    print("Best permutation = ", bestPerm)

    return bestPerm, bestLength

def calculateLength(distance_matrix, permutation):
    #print("current perm: ",permutation)
    sum = 0

    for i in range(len(permutation)):
        x = i % len(permutation)
        y = (i+1) % len(permutation)

        sum += distance_matrix[permutation[x], permutation[y]]
    
    return sum

def draw_graph(node_array, permutation, length, endFlag):
    
    plt.grid()
    
    if endFlag == True:
        plt.pause(0.0001)
        plt.clf()
        plt.grid()

    if endFlag == False:
        plt.ion()

    x_values = []
    y_values = []

    for i in range(len(node_array)):
        plt.plot(node_array[i][0], node_array[i][1], "ro")
        plt.text(node_array[i][0] * (1 + 0.03), node_array[i][1] * (1 + 0.03), i)

    for i in range(len(permutation)):
        x_values.append(node_array[permutation[i]][0])
        y_values.append(node_array[permutation[i]][1])
    
    plt.plot(x_values, y_values, "bo-")
    plt.title(str("Path: "+str(permutation)+"      Distance ≈ "+str(round(length, 2))))

    

    if endFlag == False:
        plt.draw()
        plt.pause(0.0001)
        plt.clf()
        plt.show()
    else:
        plt.show(block=True)
        
    



def main():
    
    nodes = int(input("How many nodes should be used? "))
    
    node_array = create_nodes(nodes)

    start = time.time()

    bestPerm, bestLength = brute_force(create_distance_matrix(node_array))

    end = time.time()

    print("Computation time for",nodes,"nodes was", (end-start),"seconds!")

    draw_graph(node_array, bestPerm, bestLength, True)
            
    
    
    

main()