def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counts = {}
    for value in samples:
        counts[value] = counts.get(value,0)+1

    pmf = []
    for value in sorted(counts):
        probability = counts[value]/len(samples)
        pmf.append((value,probability))
    return pmf
    pass