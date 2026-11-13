import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    scores = np.array(scores,dtype=float)
    softmax = scores - np.max(scores)-np.log(np.sum(np.exp(scores-np.max(scores))))
    return np.round(softmax,4)
