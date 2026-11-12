
import numpy as np

def rmse(y_true, y_pred):
    # Write your code here
    y_true = np.array(y_true,dtype=float)
    y_pred = np.array(y_pred,dtype=float)
    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")
    if y_true.size == 0 or y_pred.size ==0:
        raise ValueError("None of the array should be empty")
    rmse = np.sqrt(np.mean(np.square(y_true-y_pred)))
    return round(rmse,3)
