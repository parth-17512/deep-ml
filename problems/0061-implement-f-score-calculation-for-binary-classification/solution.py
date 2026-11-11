import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: Weight of recall relative to precision (beta > 1 favours recall)
    :return: F-Score rounded to three decimal places
    """
    y_true =np.array(y_true,dtype=float)
    y_pred =np.array(y_pred,dtype=float)

    tp,fp,fn=0,0,0

    for actual,predicted in zip(y_true,y_pred):
        if actual ==1 and predicted == 1:
            tp+=1
        if actual== 0 and predicted == 1:
            fp+=1
        if actual == 1 and predicted == 0:
            fn+=1

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)

    if (beta**2*precision+recall) ==0:
        return 0.0

    fscore = (1+beta**2)*(precision*recall)/((beta**2*precision)+recall)
    
    return round(fscore,3)
