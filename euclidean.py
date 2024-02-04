import math

def euc_dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)

def bubble_sort(dist):
    n = len(dist)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if dist[j] > dist[j + 1]:
                dist[j], dist[j + 1] = dist[j + 1], dist[j]

X = [(3, 4), (5, 6),(1, 2),(7, 8)]
Y = [(2, 3), (5, 6), (8, 9), (11, 12)]

dist = [euc_dist(x, y) for x, y in zip(X, Y)]

print("Unsorted dist:", dist)

bubble_sort(dist)

print("Sorted dist:", dist)


