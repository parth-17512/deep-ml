import numpy as np
from collections import Counter

def dummy_classifier(y_train, n_test, strategy, constant=None):
    """
    Produce baseline predictions of length n_test using the given strategy.
    Returns a Python list of predicted labels.
    """
    classes = sorted(set(y_train))

    if strategy == "most_frequent":
        # Count occurrences of each class.
        counts = {c: y_train.count(c) for c in classes}

        # max() uses the first encountered item when there is a tie.
        # Since classes is sorted, this gives the smallest class label.
        most_frequent = max(classes, key=lambda c: counts[c])

        return [most_frequent] * n_test

    elif strategy == "constant":
        return [constant] * n_test

    elif strategy == "uniform":
        k = len(classes)
        return [classes[i % k] for i in range(n_test)]

    elif strategy == "stratified":
        n_train = len(y_train)

        # Calculate exact expected counts and floor them.
        allocations = {}
        fractions = {}

        for c in classes:
            frequency = y_train.count(c) / n_train
            expected = n_test * frequency

            allocations[c] = int(expected)
            fractions[c] = expected - int(expected)

        # Number of predictions still left to distribute.
        remaining = n_test - sum(allocations.values())

        # Sort by:
        # 1. largest fractional part
        # 2. smallest class label for ties
        classes_by_fraction = sorted(
            classes,
            key=lambda c: (-fractions[c], c)
        )

        # Give one additional prediction to each selected class.
        for c in classes_by_fraction[:remaining]:
            allocations[c] += 1

        # Output grouped by sorted class order.
        predictions = []

        for c in classes:
            predictions.extend([c] * allocations[c])

        return predictions

    else:
        raise ValueError(
            "strategy must be one of: "
            "'most_frequent', 'constant', 'uniform', 'stratified'"
        )
