import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.array(x,dtype=float)
    p=np.array(p,dtype=float)

    if len(x)!=len(p):
        raise ValueError("x and p must have same length")
    
    total=np.sum(p)
    if not np.allclose(total,1,atol=1e-6):
        raise ValueError("Probabilities must sum to 1")

    result = np.sum(x * p)
    return float(result)
        
    

    
    
    pass
