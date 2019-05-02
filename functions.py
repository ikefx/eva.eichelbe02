import math
import numpy as np

def penaltyNonlinear(k:float, capacity:int, weight, i:int ):
    """ DERIVE A NON-LINEAR PENALTY VALUE : RAISE PENALTY WITH TIME """
    violation:float = weight - capacity
    violation = abs(violation)
    penalty:float = k * math.log((violation**i)+1)
    return penalty

def knapSackBinaryNonlinear(binary:list, W:int, w:list, v:list):
    """ READ BINARY STREAM FIND TOTAL VALUE INVOKE PENALTY (LINEAR) IF NECESSARY """
    k       : int   = 3
    totalV  : int   = 0
    totalW  : int   = 0
    capacity: int   = W
    exceeds : bool  = False
    penalty : float = 0
    fitness : float = 0
    for i, bit in enumerate(binary):
        if bit == '1':
            if totalW + w[i] > capacity:
                exceeds = not exceeds
                totalW += w[i]
                """ INVOKE PENALTY TO VALUE WHEN INFEASIBLE | PICK K """
                penalty = penaltyNonlinear(k, capacity, totalW, i)
                totalV += (v[i] - penalty)
            else:
                totalW += w[i]
                totalV += v[i]
    print(f'\t{binary}\tCapacity: {totalW}/{W}\t totalV: {totalV:.1f}\tk: {k}\tPenalty: {penalty:.1f}')
    return totalV

def penaltyStatic(k:float, capacity:int, weight ):
    """ DERIVE A STATIC PENALTY VALUE """
    violation:float = weight - capacity
    violation = abs(violation)
    penalty:float = k * math.log(violation+1)
    return penalty

def knapSackBinarySublinear(binary:list, W:int, w:list, v:list):
    """ READ BINARY STREAM FIND TOTAL VALUE INVOKE PENALTY (LINEAR) IF NECESSARY """
    k       : int   = 3
    totalV  : int   = 0
    totalW  : int   = 0
    capacity: int   = W
    exceeds : bool  = False
    penalty : float = 0
    fitness : float = 0
    for i, bit in enumerate(binary):
        if bit == '1':
            if totalW + w[i] > capacity:
                exceeds = not exceeds
                totalW += w[i]
                """ INVOKE PENALTY TO VALUE WHEN INFEASIBLE | PICK K """
                penalty = penaltyStatic(k, capacity, totalW)
                totalV += (v[i] - penalty)
            else:
                totalW += w[i]
                totalV += v[i]
    print(f'\t{binary}\tCapacity: {totalW}/{W}\t totalV: {totalV:.1f}\tk: {k}\tPenalty: {penalty:.1f}')
    return totalV

def knapSack(W:int, w:list, v:list):
    """ RATIO DRIVEN KNAPSACK FUNCTION NO PENALTY RETURNS BEST FIT BIT STREAM """
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
    nRatio = ratio.copy()
    tempW = 0
    """ Place best ratio items in knapsack while they fit """
    while(tempW <= W and count < n):
        idx = nRatio.index(max(nRatio))
        if(tempW + w[idx] > W): 
            penaltyStatic(1, W, tempW)
            nRatio[idx] = -1 
        else:
            tempW += w[idx]
            nRatio[idx] = -1
            outIdx.append(idx)
        count += 1
    """ Pretty-print variables """
    wp = ["%03d" %i for i in w]
    vp = ["%03d" %i for i in v]
    rp = ["%.1f" %i for i in ratio]
    outIdxp = ["%03d" %i for i in outIdx]
    print(f'\tv:{vp}\n\tw:{wp}\n\ti:{outIdxp}\n\tr:{rp}')
    for i in range (0, n):
        if i in outIdx:
            binaryOut[i] = 1
        else: 
            binaryOut[i] = 0
    strBin = "".join(str(x) for x in binaryOut)
    print(f'\n Maximized Binary String: \'{strBin}\'')
    print(f' Sack Capacity: {tempW} / {W}')
    return binaryOut