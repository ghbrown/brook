
import numpy as np
import taylor as ta


def f(x):
    # vector function depending nonlinearly on input vector x
    if (x.shape[0] != 3):
        print(f'ERROR: Jacobian example requires vector of length 3')
    f    = np.empty(4)
    f[0] = x[0]*np.power(x[2],2)
    f[1] = np.sin(x[1]*x[2])
    f[2] = np.exp(np.pi*x[0]) + 10
    f[3] = np.sum(x)
    return f

def J_f_exact(x):
    # computes the exact Jacobian of 
    J = np.empty((4,3))
    # set Jacobian row by row
    J[0,:] = np.array([np.power(x[2],2), 0.0, 2*x[0]*x[2]])
    J[1,:] = np.array([0.0, np.cos(x[1]*x[2])*x[2],
                       np.cos(x[1]*x[2])*x[1]])
    J[2,:] = np.array([np.exp(np.pi*x[0])*np.pi,0.0,0.0])
    J[3,:] = np.array([1.0,1.0,1.0])
    return J



if (__name__ == "__main__"):
    print()
    print(f'--------------------- JACOBIAN TEST ---------------------')
    print(f'    f(x) = [ x_0*(x_2)^2,')
    print(f'             sin(x_1*x_2),')
    print(f'             exp(pi*x_0) + 10,')
    print(f'             x_1 + x_2 + x_3 ]')

    # set current point x and compute exact Jacobian there
    x       = np.array([1.5,20,2.718])
    J_exact = J_f_exact(x)

    # print point and exact Jacobian there
    print(f'x :\n{x}\n')
    print(f'J_f(x) (exact) :\n{J_exact}\n')

    # TODO: need transpose for Jacobian to be exactly right in the
    #       "natural sense", figure out default versus natural
    #       orderings

    # compute Jacobian of nonlinear f with respect to x numerically
    deriv_nonlinear_vec = ta.diff(f,x,1)
    print(f'df / dx :\n{deriv_nonlinear_vec}\n')
