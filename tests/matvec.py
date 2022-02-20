
import numpy as np
import taylor as ta


def matvec_vec(x,A):
    # computes the matrix vector product
    #    A x
    return A @ x


def matvec_mat(A,x):
    # computes the matrix vector product
    #    A x
    return A @ x



if (__name__ == "__main__"):
    print()
    print(f'--------------------- MATVEC TEST ---------------------')
    print(f'    f(A,x) = A x\n')

    # set matrix and vector
    A = np.array([[1.0,2.0,3.0],
                  [2.0,4.0,5.0],
                  [3.0,5.0,6.0]])
    x = np.array([1.0,2.0,3.0])

    # print matrix and vector
    print(f'A :\n{A}\n')
    print(f'x : {x}\n')

    # derivative of matrix vector product with respect to vector
    deriv_matvec_vec = ta.diff(matvec_vec,x,1,args=(A,))
    print(f'df / dx :\n{deriv_matvec_vec}\n')

    # derivative of matrix vector product with respect to matrix
    deriv_matvec_mat = ta.diff(matvec_mat,A,1,args=(x,))
    print(f'df / dA :\n{deriv_matvec_mat}')
