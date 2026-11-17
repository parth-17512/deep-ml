import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    # Your code here
    #a = np.asarray(a,dtype=float)
    ans=[]
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == col:
                ans.append(A[row][col])
    return ans
