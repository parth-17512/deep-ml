import math

def poisson_probability(k, lam):
    """
    Calculate the probability of observing exactly k events in a fixed interval,
    given the mean rate of events lam, using the Poisson distribution formula.
    :param k: Number of events (non-negative integer)
    :param lam: The average rate (mean) of occurrences in a fixed interval
    """
    # Your code here
    P = (lam**k)*(math.exp(-lam))/(math.factorial(k))
    return round(P,5)