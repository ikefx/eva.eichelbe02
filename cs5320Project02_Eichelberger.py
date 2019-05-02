""" CS5320 : PROJECT03 
    NEIL EICHELBERGER """
import math
import itertools 
import random
from statistics import *
from functions import *
from prettytable import PrettyTable

def runSim01(numberOfItems:int, W:int, wMax:int, vMax:int):
    """ FIND THE BEST SEQUENCE OF RANDOM WEIGHT | VALUE """
    v = list()
    w = list()
    n = numberOfItems
    for i in range(0, n): 
        v.append(int(random.uniform(1,int(vMax))))
        w.append(int(random.uniform(1,int(wMax))))

    """ INIT FIXED VARIABLES (DEVELOPMENT) """
    return knapSack(int(W), w, v)

def runSim02(n:int):
    """ GENERATE A LIST OF ALL PERMUTATIONS OF BIT SEQUENCE OF SIZE N AND PIPE TO SUBLINEAR KNAPSACK FUNC """
    seqList = ["".join(seq) for seq in itertools.product("01", repeat=n)]
    """ INIT VARIABLES """
    b = ()
    W = 40
    v = list()
    w = list()
    w = [ 10, 20, 30  ]
    v = [ 25, 10, 100 ]
    bestPair: tuple = (0,0)
    """ Pretty-print variables """
    wp = ["%03d" %i for i in w]
    vp = ["%03d" %i for i in v]
    print(f' Capacity: {W}\n v:{vp}\n w:{wp}\n')
    for i, sequence in enumerate(seqList):
        assert len(sequence) == len(w) == len(v), "ERROR: Sequence, w vector, and v vector must be equal length"
        b = knapSackBinarySublinear(sequence, W, w, v)
        if b > bestPair[0]:
            bestPair = (b, i)
    print(f'\n Best Value: {bestPair[0]:.1f} in Binary Sequence \'{seqList[bestPair[1]]}\'')
    return

def runSim03(n:int):
    """ GENERATE A LIST OF ALL PERMUTATIONS OF BIT SEQUENCE OF SIZE N AND PIPE TO NON-LINEAR KNAPSACK FUNC """
    seqList = ["".join(seq) for seq in itertools.product("01", repeat=n)]
    """ INIT VARIABLES """
    b = ()
    W = 40
    v = list()
    w = list()
    w = [ 10, 20, 30  ]
    v = [ 25, 10, 100 ]
    bestPair: tuple = (0,0)
    """ Pretty-print variables """
    wp = ["%03d" %i for i in w]
    vp = ["%03d" %i for i in v]
    print(f' Capacity: {W}\n v:{vp}\n w:{wp}\n')
    for i, sequence in enumerate(seqList):
        assert len(sequence) == len(w) == len(v), "ERROR: Sequence, w vector, and v vector must be equal length"
        b = knapSackBinaryNonlinear(sequence, W, w, v)
        if b > bestPair[0]:
            bestPair = (b, i)
    print(f'\n Best Value: {bestPair[0]:.1f} in Binary Sequence \'{seqList[bestPair[1]]}\'')
    return

def main():
    """ THIS FIRST SIMULATION FINDS THE BEST SEQUENCE OF A RANDOM SET OF { WEIGHTS | VALUES } """
    print("Legend:\n\t[ v = value vector, w = weight vector, r = ratio vector, i = index of selected items ]\n")
    print("-- SIMULATION 01: BEST BINARY SEQUENCE FROM RANDOM PROBLEM PARAMETERS ( NO PENALTY | DISCARD INFEASIBLE ) ---")
    runSim01(10, random.uniform(50,100), random.uniform(10,50), random.uniform(50,100))
    print("-- END SIMULATION 01 ---------------------------------------------\n")

    """ THIS SECOND SIMULATION ATTEMPTS ALL PERMUTATIONS OF A 3 BIT SEQUENCE (SUBLINEAR PENALTY): RETURNS BEST """
    print("\n-- SIMULATION 02: BEST SEQUENCE FROM BINARY STREAM PERMUTATIONS (SUBLINEAR PENALTY) ---")
    runSim02(3)
    print("-- END SIMULATION 02 ---------------------------------------------\n")

    """ THIS THIRD SIMULATION ATTEMPTS ALL PERMUTATIONS OF A 3 BIT SEQUENCE (NONLINEAR PENALTY): RETURNS BEST """
    print("\n-- SIMULATION 03: BEST SEQUENCE FROM BINARY STREAM PERMUTATIONS (NONLINEAR PENALTY) ---")
    runSim03(3)
    print("-- END SIMULATION 03 ---------------------------------------------\n")

if __name__ == "__main__":
    main() 