def knapSack(W, w, v):
    """ RATIO DRIVEN KNAPSACK FUNCTION """
    count = 0
    n = len(w)
    assert len(w) == len(v), "ERROR: w list and v list must be equal length"
    ratio = list()
    outIdx = list()
    binaryOut = [0] * n
    """ Get a list of value/weight ratios """
    for i in range(0, n):
        ratio.append(v[i]/w[i])
    """ Duplicate ratio to preserve original for reference """
    nRatio = ratio
    tempW = w[nRatio.index(max(nRatio))]
    """ Place best ratio items in knapsack while they fit """
    while(tempW <= W and count < n):
        idx = ratio.index(max(nRatio))
        tempW += w[idx]
        nRatio[idx] = -1
        outIdx.append(idx)
        count += 1
    """ Pretty-print variables """
    wp = ["%03d" %i for i in w]
    vp = ["%03d" %i for i in v]
    outIdxp = ["%03d" %i for i in outIdx]
    print(f'w:{wp}\nv:{vp}\ni:{outIdxp}')
    for i in range (0, n):
        if i in outIdx:
            binaryOut[i] = 1
        else: 
            binaryOut[i] = 0
    print(f'\nBinary String: {binaryOut}')
    return binaryOut

# A Dynamic Programming based Python Program for 0-1 Knapsack problem 
# Returns the maximum value that can be put in a knapsack of capacity W 
def knapSackDynamic(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSackG2G(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
