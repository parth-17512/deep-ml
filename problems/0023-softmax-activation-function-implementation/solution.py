import math

def softmax(scores: list[float]) -> list[float]:
    shifted = [v-max(scores) for v in scores]
    e = [math.exp(v) for v in shifted]
    return [v/sum(e) for v in e]
    