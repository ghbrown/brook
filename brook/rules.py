
import itertools
import numpy as np

def forward(fun,x,order,i_m,args,delta_vec):
    # need both order and i_m to differentiate between cases like
    #     second derivative of scalar: order = 2, i_m = (i, j)
    #     first derivative of scalar with respect to matrix : order = 1, i_m = (i, j)
