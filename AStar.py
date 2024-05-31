import heapq

# Heuristic function to estimate the cost from the current node to the unvisited nodes
def heuristic(current, unvisited, matrix):
    # Return the minimum distance from the current node to any unvisited node
    return min(matrix[current][city] for city in unvisited)

# A* algorithm for solving the TSP (Traveling Salesman Problem)
def a_star_tsp(matrix):
    n = len(matrix)  # Number of cities (nodes)
    # Priority queue to store (f, g, current_node, visited_state) tuples
    pq = [(0, 0, 0, 1)]
    visited = {}  # Dictionary to store the minimum cost to reach each state

    while pq:
        # Pop the node with the lowest f value (priority)
        f, g, current, state = heapq.heappop(pq)
        # If all nodes have been visited, return the total cost including return to the start
        if state == (1 << n) - 1:
            return g + (matrix[current][0] or float('inf'))
        # Skip if this state has already been visited with a lower or equal cost
        if (current, state) in visited and visited[(current, state)] <= g:
            continue
        # Mark this state as visited with the current cost
        visited[(current, state)] = g
        # List of unvisited nodes
        unvisited = [i for i in range(n) if not (state & (1 << i))]
        # Explore all unvisited neighbors
        for next in unvisited:
            # Calculate the cost to reach the next node
            next_g = g + (matrix[current][next] or float('inf'))
            # Calculate the estimated total cost using the heuristic
            next_f = next_g + heuristic(next, unvisited, matrix)
            # Push the new state to the priority queue
            heapq.heappush(pq, (next_f, next_g, next, state | (1 << next)))

    return float('inf')# Return infinity if no valid TSP cycle is found