import numpy as np
import math

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    res = [(y*math.log(p)+(1-y)*math.log(1-p)) for y,p in zip(Y, P) ]
    return round(-sum(res),2)
    #return -sum(res)

Y = [1,1,0]
P = [0.8,0.7,0.1]

print("\n\nThe Cross-Entropy: {} !!!\n\n".format(cross_entropy(Y,P)))
    