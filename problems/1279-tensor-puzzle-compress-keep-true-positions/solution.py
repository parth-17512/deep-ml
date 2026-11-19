import numpy as np

def compress(g: np.ndarray, v: np.ndarray) -> np.ndarray:
    idx = np.arange(v.shape[0])
    dest = (idx[:, None] > idx) @ g.astype(int)
    routing = ((idx[:, None] == dest) & g).astype(v.dtype)
    return routing @ v