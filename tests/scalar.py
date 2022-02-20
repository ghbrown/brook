
import numpy as np
import taylor as ta


def f(x):
    # scalar depending nonlinearly on scalar input
    val = 20*x - 14*np.power(x,2) - 2*np.sin(1.8*x)*np.exp(-5*x)
    return val

def df_dx_exact(x):
    # computes the exact first derivative of f(x)
    df_dx = 20 - 28*x - 2*(1.8*np.cos(1.8*x)*np.exp(-5*x) +
                           -5*np.sin(1.8*x)*np.exp(-5*x))
    return df_dx

def d2f_dx2_exact(x):
    # computes the exacts second derivative of f(x)
    d2f_dx2 = -28 - 2*(1.8*(-1.8*np.sin(1.8*x)*np.exp(-5*x) +
                            -5*np.cos(1.8*x)*np.exp(-5*x)) -
                    5*(-1.8*np.sin(1.8*x)*np.exp(-5*x) -
                       5*np.sin(1.8*x)*np.exp(-5*x)))
    return d2f_dx2



if (__name__ == "__main__"):
    print()
    print(f'--------------------- SCALAR TEST ---------------------')
    print(f'    f(x) = 20*x - 14*np.power(x,2) -')
    print(f'              2*np.sin(1.8*x)*np.exp(-5*x)\n')

    # set current point x and compute exact derivative there
    x = 1.2
    first_deriv_exact = df_dx_exact(x)
    second_deriv_exact = d2f_dx2_exact(x)

    # print point and exact Jacobian there
    print(f'x : {x}\n')
    print(f'df(x)_dx (exact) : {first_deriv_exact}\n')
    print(f'd^2 f(x) / dx^2 (exact) : {second_deriv_exact}\n')

    # compute first derivative of f with respect to x numerically
    deriv_scalar_1 = ta.diff(f,x,1)
    print(f'df(x) / dx : {deriv_scalar_1}\n')

    # compute second derivative of f with respect to x numerically
    deriv_scalar_2 = ta.diff(f,x,2)
    print(f'd^2 f(x) / dx^2 : {deriv_scalar_2}\n')
