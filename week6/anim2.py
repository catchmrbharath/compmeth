
from numpy import *
from scipy import *
from matplotlib.pyplot import *
from time import *

def func(x):
    x = array(x)
    sq = sqrt(x[0]**2 + x[1]**2)
    alpha = 5*(0.1*sq-0.5)
    tran_mat = array([[cos(alpha),sin(alpha)],
                        [-sin(alpha),cos(alpha)]])
    temp = dot(tran_mat,x.transpose())-array([5,5])

    return temp[0]**2 + temp[1]**2

p = [-1,5.5]
print func(p)
p = [1,5]
print func(p)
