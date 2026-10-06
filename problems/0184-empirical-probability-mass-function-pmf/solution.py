def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    if len(samples) == 0 :
        return []
    counts = {}
    for value in samples:
        counts[value] = counts.get(value,0)+1
    pmf=[]
    total = len(samples)
    
    for value in sorted(counts):
        probability = counts[value]/total
        pmf.append((value,probability))
    return pmf
    