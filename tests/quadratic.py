
import numpy as np
import taylor as ta


def quad_vec(x,A,b):
    # computes the n dimensional quadratic of the form:
    #    (1/2) x^T A x - b^T x
    return 0.5*(x.T@A@x) - b.T@x



if (__name__ == "__main__"):
    print()
    print(f'--------------------- QUADRATIC TEST ---------------------')
    print(f'    f(A,b,x) = 0.5 x^T A x - x^T b\n')

    # set matrix and vector
    A = np.array([[1.0,2.0,3.0],
                  [2.0,4.0,5.0],
                  [3.0,5.0,6.0]])
    x = np.array([1.0,2.0,3.0])
    b = np.array([4.0,5.0,6.0])

    # print relevant quantities
    print(f'A :\n{A}\n')
    print(f'x :\n{x}\n')
    print(f'b :\n{b}\n')
    print(f'A x - b :\n{A@x-b}\n')

    # compute first derivative of quadratic with respect to x
    deriv_quad_vec_1 = ta.diff(quad_vec,x,1,args=(A,b))
    print(f'df / dx :\n{deriv_quad_vec_1}\n')

    # compute second derivative of quadratic with respect to x
    deriv_quad_vec_2 = ta.diff(quad_vec,x,2,args=(A,b))
    print(f'd^2 f / dx^2 :\n{deriv_quad_vec_2}\n')
