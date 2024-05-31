import heapq

def ucs_tsp(matrix):
    n = len(matrix)  # Number of cities (nodes)
    pq = [(0, 0, 1)]  # Priority queue initialized with (cost, current_node, visited_state)
    visited = {}  # Dictionary to store the minimum cost to reach each state

    while pq:
        # Pop the node with the lowest cost (UCS uses cost as the priority)
        cost, current, state = heapq.heappop(pq)
        # If all nodes have been visited, return the total cost including return to the start
        if state == (1 << n) - 1:
            return cost + (matrix[current][0] or float('inf'))
        # Skip if this state has already been visited with a lower or equal cost
        if (current, state) in visited and visited[(current, state)] <= cost:
            continue
        # Mark this state as visited with the current cost
        visited[(current, state)] = cost
        # Explore all possible next cities
        for next in range(n):
            # Check if the next city has not been visited
            if not (state & (1 << next)):
                # Calculate the cost to reach the next city
                next_cost = matrix[current][next] or float('inf')
                # Push the new state to the priority queue with the updated cost and state
                heapq.heappush(pq, (cost + next_cost, next, state | (1 << next)))

    return float('inf')  # Return infinity if no valid TSP cycle is found
