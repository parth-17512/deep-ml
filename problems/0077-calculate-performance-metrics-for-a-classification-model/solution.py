import numpy as np
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
    actual = np.array(actual)
    predicted = np.array(predicted)
    tp,fp,fn,tn =0,0,0,0
    for actual,predicted in zip(actual,predicted):
        if actual == 1 and predicted == 1 :
            tp+=1
        if actual == 0 and predicted == 1:
            fp+=1
        if actual == 1 and predicted == 0:
            fn+=1
        if actual == 0 and predicted == 0:
            tn+=1
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    confusion_matrix=[[tp,fn],[fp,tn]]
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    f1 = (2*precision*recall)/(precision+recall)
    specificity = tn/(tn+fp)
    negativePredictive=tn/(tn+fn)
    return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
