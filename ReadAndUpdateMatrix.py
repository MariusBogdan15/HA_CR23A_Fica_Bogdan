def read_and_update_matrix(filename, default_value=1):
    with open(filename) as f:
        # Read the matrix from the file and convert all entries to integers
        matrix = [list(map(int, line.strip().split())) for line in f]

    n = len(matrix)  # Number of cities (nodes)
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 0:
                # Replace zero with the default value for all non-diagonal elements
                matrix[i][j] = default_value
    return matrix  # Return the updated matrix
