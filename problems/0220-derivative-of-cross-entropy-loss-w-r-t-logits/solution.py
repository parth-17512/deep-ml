import math

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
    """
    Compute the derivative of cross-entropy loss with respect to logits.

    Args:
        logits: Raw model outputs (before softmax)
        target: Index of the true class (0-indexed)

    Returns:
        Gradient vector where gradient[i] = dL/d(logits[i])
    """
    # 1. Compute softmax stably
    max_logit = max(logits)
    exp_logits = [math.exp(x - max_logit) for x in logits]
    total = sum(exp_logits)
    probabilities = [x / total for x in exp_logits]

    # 2. Compute gradient: softmax probabilities - one-hot target
    probabilities[target] -= 1.0

    return probabilities