
import numpy as np

def jaccard_index(y_true, y_pred):
    y_true =np.array(y_true,dtype=float)
    y_pred =np.array(y_pred,dtype=float)
    union = np.sum((y_true==1)|(y_pred==1))
    intersection = np.sum((y_true==1) &(y_pred==1))
    if union == 0:
        return 0.0
    jaccard = intersection/union
    return round(jaccard, 3)
