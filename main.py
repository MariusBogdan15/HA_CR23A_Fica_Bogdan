import heapq
from DFS import dfs_tsp  # Import the DFS TSP function
from ReadMatrix import read_matrix  # Import the function to read and update matrices
from UCS import ucs_tsp  # Import the UCS TSP function
from AStar import a_star_tsp  # Import the A* TSP function

def main():
    # Sample matrix for 3 cities
    # This matrix represents a graph with 3 cities and the distances between them
    sample_matrix = [
        [0, 10, 15],  # Distances from city 0 to city 0, 1, 2
        [10, 0, 35],  # Distances from city 1 to city 0, 1, 2
        [15, 35, 0]   # Distances from city 2 to city 0, 1, 2
    ]

    # Print the results of DFS, UCS, and A* TSP algorithms for the sample matrix
    print("DFS TSP result for sample matrix:", dfs_tsp(sample_matrix))
    print("UCS TSP result for sample matrix:", ucs_tsp(sample_matrix))
    print("A* TSP result for sample matrix:", a_star_tsp(sample_matrix))

    # Read matrices from files and test the algorithms
    # Read and update the 5x5 matrix from the file 'matrix_5x5.txt'
    matrix_5x5 = read_and_update_matrix('matrix_5x5.txt')
    # Read and update the 10x10 matrix from the file 'matrix_10x10.txt'
    matrix_10x10 = read_and_update_matrix('matrix_10x10.txt')
    # Read and update the 15x15 matrix from the file 'matrix_15x15.txt'
    matrix_15x15 = read_and_update_matrix('matrix_15x15.txt')

    # Print the results of DFS, UCS, and A* TSP algorithms for the 5x5 matrix
    print("DFS TSP result for 5x5 matrix:", dfs_tsp(matrix_5x5))
    print("UCS TSP result for 5x5 matrix:", ucs_tsp(matrix_5x5))
    print("A* TSP result for 5x5 matrix:", a_star_tsp(matrix_5x5))

    # Print the results of DFS, UCS, and A* TSP algorithms for the 10x10 matrix
    print("DFS TSP result for 10x10 matrix:", dfs_tsp(matrix_10x10))
    print("UCS TSP result for 10x10 matrix:", ucs_tsp(matrix_10x10))
    print("A* TSP result for 10x10 matrix:", a_star_tsp(matrix_10x10))

    # Print the results of DFS, UCS, and A* TSP algorithms for the 15x15 matrix
    print("DFS TSP result for 15x15 matrix:", dfs_tsp(matrix_15x15))
    print("UCS TSP result for 15x15 matrix:", ucs_tsp(matrix_15x15))
    print("A* TSP result for 15x15 matrix:", a_star_tsp(matrix_15x15))

if __name__ == "__main__":
    main()  # Call the main function to execute the TSP algorithms on the provided matrices
