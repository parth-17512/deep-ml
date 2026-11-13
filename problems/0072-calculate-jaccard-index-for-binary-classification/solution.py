
import numpy as np

def jaccard_index(y_true, y_pred):
    y_true = np.array(y_true,dtype=float)
    y_pred = np.array(y_pred,dtype=float)
    union,intersection=0,0
    for actual,predicted in zip(y_true,y_pred):
        if actual == 1 or predicted == 1:
            union+=1
        if actual == 1 and predicted ==1:
            intersection+=1
    if union == 0:
        return 0.0
    jaccard = intersection/union
    
    return round(jaccard, 3)
