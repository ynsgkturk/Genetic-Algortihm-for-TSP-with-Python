

def problem(candidate, distance_matrix):
    """
    Takes candidate and returns fitness value using distance matrix
    """

    fitness = 0

    for idx in range(len(candidate)-1):
        i, j = candidate[idx]-1, candidate[idx+1]-1
        fitness += distance_matrix[i][j]

    return fitness
