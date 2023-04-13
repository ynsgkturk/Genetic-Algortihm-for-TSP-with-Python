from math import sqrt


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    total = ((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return sqrt(total)


def calculate_distance_matrix(areas):
    n = len(areas)
    distance_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if distance_matrix[j][i] == 0:
                    distance_matrix[i][j] = calculate_distance(areas[i], areas[j])
                else:
                    distance_matrix[i][j] = distance_matrix[j][i]

    return distance_matrix
