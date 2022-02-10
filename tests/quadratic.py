
import numpy as np
import brook as bk

def quad(x,n):
    # computes the n dimensional quadratic of the form:
    #    (1/2) x^T A x

    # fix and set random seed
    seed = 4 
    np.random.seed(seed)

    # symmetrize matrix
    A_unsymm = np.random.rand(n,n) 
    A = A_unsymm + A_unsymm.T

    return 0.5*(x.T@A@x)


# set dimension of problem
n = 10

# set point at which to compute derivatives
x = np.random.rand(n)

grad_quad_x = bk.diff(quad,x,2,args=(n,))
