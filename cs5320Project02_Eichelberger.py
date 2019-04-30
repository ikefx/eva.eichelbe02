""" CS5320 : PROJECT03 
    NEIL EICHELBERGER """
import math
import random
from statistics import *
from functions import *
from prettytable import PrettyTable

def runSim(numberOfItems:int, W:int, wMax:int, vMax:int):
    """ INIT RANDOM WEIGHT AND VALUE LISTS """
    v = list()
    w = list()
    n = numberOfItems
    for i in range(0, n): 
        v.append(int(random.uniform(1,int(vMax))))
        w.append(int(random.uniform(1,int(wMax))))

    """ INIT FIXED VARIABLES (DEVELOPMENT) """
    #w = [ 10, 20, 30, 40, 50 ]
    #v = [ 25, 10, 100, 60, 40 ]
    #W = 75
    return knapSack(W, w, v)

def main():

    runSim(10, random.uniform(50,100), random.uniform(5,50), random.uniform(50,100))


if __name__ == "__main__":
    main() 