import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    y_true = np.array(y_true,dtype=float)
    y_pred = np.array(y_pred,dtype=float)

    TP,FN = 0,0
    for actual , predicted in zip(y_true,y_pred):
        if actual == 1 and predicted == 1:
            TP+=1
        if actual == 1 and predicted ==0:
            FN+=1

    if TP+FN == 0:
        return 0.0

    return float(TP/(TP+FN))
    
