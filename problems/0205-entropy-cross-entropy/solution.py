import math

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
    entropy = 0.0
    cross_entropy = 0.0

    for p, q in zip(P, Q):
        if p == 0:
            continue

        entropy -= p * math.log(p)

        if q == 0:
            cross_entropy = float('inf')
        elif cross_entropy != float('inf'):
            cross_entropy -= p * math.log(q)

    return float(entropy), float(cross_entropy)