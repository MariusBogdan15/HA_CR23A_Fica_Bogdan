def dfs_tsp(matrix):
    n = len(matrix)  # Number of cities (nodes)
    all_visited = (1 << n) - 1  # Bitmask representing all cities visited
    memo = {}  # Memoization dictionary to store the minimum cost for each state

    # Recursive helper function to perform DFS with memoization
    def dfs(current, visited):
        # If all cities have been visited, return the cost to return to the start
        if visited == all_visited:
            return matrix[current][0] or float('inf')
        # If the current state has been computed before, return the stored cost
        if (current, visited) in memo:
            return memo[(current, visited)]
        min_cost = float('inf')  # Initialize the minimum cost to infinity
        # Explore all possible next cities
        for next in range(n):
            # Check if the next city has not been visited
            if not (visited & (1 << next)):
                # Calculate the cost to the next city, or infinity if no path
                cost = matrix[current][next] or float('inf')
                # Recursively find the minimum cost from the next city
                min_cost = min(min_cost, cost + dfs(next, visited | (1 << next)))
        # Store the computed minimum cost for the current state
        memo[(current, visited)] = min_cost
        return min_cost

    # Start the DFS from the first city with only the first city visited
    return dfs(0, 1)
