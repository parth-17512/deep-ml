import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    """
    dataset = np.array(data)

    mean = np.mean(dataset)
    median = np.median(dataset)

    values, counts = np.unique(dataset, return_counts=True)
    mode = values[np.argmax(counts)]

    var = np.var(dataset)
    std = np.std(dataset)

    percentiles = np.percentile(dataset, [25, 50, 75])

    q1 = percentiles[0]
    q2 = percentiles[1]
    q3 = percentiles[2]

    iqr = q3 - q1

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": var,
        "standard_deviation": std,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": iqr
    }