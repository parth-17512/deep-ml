import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.

    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation

    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Work on a float copy so we never mutate the caller's array,
    # and so integer inputs don't truncate the +/- epsilon perturbation.
    x = np.array(x, dtype=float)
    analytical_grad = np.asarray(analytical_grad, dtype=float)

    # Output container: same shape as x, one partial derivative per element.
    numerical_grad = np.zeros_like(x)

    # np.nditer with multi_index lets us visit every element of x,
    # whether x is 1-D, 2-D, or higher-dimensional.
    it = np.nditer(x, flags=['multi_index'])
    while not it.finished:
        idx = it.multi_index          # index of the coordinate being perturbed
        original = x[idx]             # remember the true value so we can restore it

        # f(x + epsilon * e_i): nudge this single coordinate up
        x[idx] = original + epsilon
        f_plus = f(x)

        # f(x - epsilon * e_i): nudge this single coordinate down
        x[idx] = original - epsilon
        f_minus = f(x)

        # Restore the coordinate before moving on, otherwise the
        # perturbation would leak into the next coordinate's evaluation.
        x[idx] = original

        # Centered finite difference: (f(x+e) - f(x-e)) / (2e)
        # Error is O(epsilon^2), better than the one-sided O(epsilon).
        numerical_grad[idx] = (f_plus - f_minus) / (2 * epsilon)

        it.iternext()

    # Relative error = ||num - ana|| / (||num|| + ||ana||)
    numerator = np.linalg.norm(numerical_grad - analytical_grad)
    denominator = np.linalg.norm(numerical_grad) + np.linalg.norm(analytical_grad)

    # Edge case: both gradients are zero vectors -> denominator is 0.
    # They agree perfectly, so the error is defined as 0 (avoids 0/0 = NaN).
    if denominator == 0:
        relative_error = 0.0
    else:
        relative_error = numerator / denominator

    return numerical_grad, float(relative_error)