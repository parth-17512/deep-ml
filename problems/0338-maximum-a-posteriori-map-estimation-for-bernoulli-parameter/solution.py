def map_estimate_bernoulli(observations: list, alpha: float, beta: float) -> float:
    successes = sum(observations)
    failures = len(observations) - successes

    a = alpha + successes
    b = beta + failures

    if a == 1 and b == 1:
        estimate = 0.5
    elif a == 1:
        estimate = 0.0
    elif b == 1:
        estimate = 1.0
    else:
        estimate = (a - 1) / (a + b - 2)

    return round(estimate, 4)