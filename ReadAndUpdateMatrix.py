def read_matrix(filename):
    with open(filename) as f:
        # Read the matrix from the file and convert all entries to integers
        matrix = [list(map(int, line.strip().split())) for line in f]

    return matrix  # Return the updated matrix
