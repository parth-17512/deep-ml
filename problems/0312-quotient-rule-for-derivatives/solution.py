import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g= np.poly1d(g_coeffs)
    h= np.poly1d(h_coeffs)

    g_x = g(x) 
    h_x = h(x)

    g_prime_x = np.polyder(g)(x) #g'(x)
    h_prime_x = np.polyder(h)(x) #h'(x)

    derivative = (g_prime_x*h_x -g_x*h_prime_x)/(h_x**2) 
    return  derivative