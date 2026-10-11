
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    if not vectors:
        return []

    n = len(vectors[0])

    if n < 2:
        raise ValueError("At least two observations are required.")

    if any(len(vector) != n for vector in vectors):
        raise ValueError("All vectors must have the same number of observations.")

    means = [sum(vector) / n for vector in vectors]

    centered = [
        [value - means[i] for value in vector]
        for i, vector in enumerate(vectors)
    ]

    num_features = len(vectors)
    covariance_matrix = []

    for i in range(num_features):
        row = []
        for j in range(num_features):
            covariance = sum(
                centered[i][k] * centered[j][k]
                for k in range(n)
            ) / (n - 1)

            row.append(float(covariance))

        covariance_matrix.append(row)

    return covariance_matrix
