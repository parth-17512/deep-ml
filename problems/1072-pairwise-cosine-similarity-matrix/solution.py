import numpy as np

def pairwise_cosine_similarity(X):
    a = np.array(X,dtype=float)
    dot_product =  a @ a.T
    l2_norm = np.linalg.norm(a,axis=1)

    n = l2_norm.size
    reshape_norm = l2_norm.reshape(n,1)
    norm = l2_norm*reshape_norm
    
    cosine_similarity = np.zeros_like(dot_product)
    np.divide(dot_product, norm, out=cosine_similarity, where=(norm != 0))
    return np.round(cosine_similarity, 4).tolist()