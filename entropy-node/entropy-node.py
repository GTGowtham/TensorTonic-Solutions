import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
        # Convert to numpy array
    y = np.array(y)
    
    # Handle empty input
    if y.size == 0:
        return 0.0
    
    # Get class counts
    _, counts = np.unique(y, return_counts=True)
    
    # Compute probabilities
    p = counts / counts.sum()
    
    # Remove zero probabilities (numerical stability)
    p = p[p > 0]
    
    # Compute entropy
    entropy = -np.sum(p * np.log2(p))
    
    return float(entropy)
    
    pass