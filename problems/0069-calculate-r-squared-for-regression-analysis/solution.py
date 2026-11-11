
import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    y_true = np.array(y_true,dtype=float)
    y_pred = np.array(y_pred,dtype=float)

    ssr,sst=0,0
    mean = np.mean(y_true)
    for actual , predicted in zip(y_true,y_pred):
        ssr+= (actual-predicted)**2
        sst+= (actual-mean)**2
    if sst == 0 :
        return 0.0
    return round(1-(ssr/sst),3)
