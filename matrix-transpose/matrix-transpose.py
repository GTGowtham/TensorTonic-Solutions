import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # rows = len(A)
    # cols = len(A[0])
    
    # result = []
    
    # for j in range(cols):
    #     new_row = []
    #     for i in range(rows):
    #         new_row.append(A[i][j])
    #     result.append(new_row)

    # np_arr=np.array(result)
    np_arr=np.transpose(A)
    return np_arr
    pass
