import numpy as np

def multivariate_kl_divergence(mu_p: np.ndarray, Cov_p: np.ndarray,
                              mu_q: np.ndarray, Cov_q: np.ndarray) -> float:
    k = len(mu_p)

    term1 = np.trace(np.linalg.solve(Cov_q, Cov_p))

    diff = mu_q - mu_p
    term2 = diff.T @ np.linalg.solve(Cov_q, diff)

    term3 = np.linalg.slogdet(Cov_q)[1] - np.linalg.slogdet(Cov_p)[1]

    return float(0.5 * (term1 + term2 - k + term3))