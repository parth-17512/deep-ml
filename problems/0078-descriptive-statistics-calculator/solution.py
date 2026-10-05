import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    dataset = np.array(data,dtype = float)

    mean = np.mean(dataset)
    median =np.median(dataset)
    
    values,counts = np.unique(dataset,return_counts=True)
    mode = values[np.argmax(counts)]

    variance = np.var(dataset)
    std_dev = np.std(dataset)

    percentiles = np.percentile(dataset,[25,50,75])
    iqr = percentiles[2]-percentiles[0]
    return {
    "mean": float(mean),
    "median": float(median),
    "mode": float(mode),
    "variance": float(variance),
    "standard_deviation": float(std_dev),
    "25th_percentile": float(percentiles[0]),
    "50th_percentile": float(percentiles[1]),
    "75th_percentile": float(percentiles[2]),
    "interquartile_range": float(iqr)
}
    pass