import numpy as np

def true_distances(mask):
    """Distance to the previous and next True along the last axis, -1 where none exists."""
    arr = np.asarray(mask, dtype=bool)
    
    # Handle empty arrays cleanly
    if arr.size == 0:
        empty = [] if arr.ndim == 1 else [[] for _ in range(arr.shape[0])]
        return {"prev": empty, "next": empty}

    n = arr.shape[-1]
    idx = np.arange(n)

    # Helper to compute backward distance along the last axis
    def dist_from_prev(m):
        stamped = np.where(m, idx, -1)
        last_true_idx = np.maximum.accumulate(stamped, axis=-1)
        return np.where(last_true_idx == -1, -1, idx - last_true_idx)

    # --- These lines were missing ---
    prev_dist = dist_from_prev(arr)
    next_dist = dist_from_prev(arr[..., ::-1])[..., ::-1]

    return {
        "prev": prev_dist.tolist(),
        "next": next_dist.tolist(),
    }