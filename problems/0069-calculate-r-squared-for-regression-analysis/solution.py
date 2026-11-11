
import numpy as np

def r_squared(y_true, y_pred):
    # Write your code here
    y_true = np.array(y_true,dtype=float)
    y_pred = np.array(y_pred,dtype=float)

    ssr,sst=0,0
    for actual , predicted in zip(y_true,y_pred):
        ssr+= (actual-predicted)**2
        sst+= (actual-np.mean(y_true))**2
    return round(1-(ssr/sst),3)
