import numpy as np
import math

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    sig = 1 / (1 + np.exp(-x))
    return sig
    
    pass