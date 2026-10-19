def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    count_x =0
    count_both =0
    
    for x_values,y_values in data:
      if x_values == x and y_values == y:
        count_both += 1
      if x_values == x:
        count_x += 1
    if count_x == 0:
      return 0.0
    return round(count_both/count_x, 4)
    