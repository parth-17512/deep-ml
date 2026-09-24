import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n = data.shape[0]

    # Generate a reproducible random ordering of row indices
    indices = np.random.default_rng(seed).permutation(n)

    # Calculate split points
    train_end = int(n * train_frac)
    validation_end = train_end + int(n * validation_frac)

    # Shuffle the data and split it
    shuffled_data = data[indices]

    train = shuffled_data[:train_end]
    validation = shuffled_data[train_end:validation_end]
    test = shuffled_data[validation_end:]

    return [train, validation, test]
    pass