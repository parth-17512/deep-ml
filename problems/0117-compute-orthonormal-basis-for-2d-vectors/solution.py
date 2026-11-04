
import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:

    basis = []

    for a in vectors:
        v = np.array(a, dtype=float)

        # Remove projections onto previous basis vectors
        for q in basis:
            projection = np.dot(q, v) * q
            v = v - projection

        # Calculate magnitude
        norm = np.linalg.norm(v)

        # Skip dependent or nearly dependent vectors
        if norm > tol:
            q = v / norm
            basis.append(q)

    return basis
