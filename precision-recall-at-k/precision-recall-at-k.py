def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    # 1. Take only the top-k recommendations
    top_k = recommended[:k]
    
    # 2. Convert relevant items to a set for faster lookup
    relevant_set = set(relevant)
    
    # 3. Count the "Hits" (items in top-k that are relevant)
    hits = len([item for item in top_k if item in relevant_set])
    
    # 4. Calculate Precision@k
    # Precision = How many of our 5 suggestions were actually good?
    precision_k = hits / k
    
    # 5. Calculate Recall@k
    # Recall = How many of the user's total favorites did we manage to find?
    recall_k = hits / len(relevant)
    
    return [float(precision_k), float(recall_k)]