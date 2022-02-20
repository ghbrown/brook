
## `taylor`

Compute finite difference approximations to derivatives of multidimensional, multivariate functions with respect to multidimensional variables.

Unlike [`findiff`](https://github.com/maroba/findiff) and [`fastfd`](https://github.com/stefanmeili/FastFD) (which focus on the computation of finite differences over multidimensional grids likely representing physical systems), the focus of [`taylor`](https://github.com/ghbrown/taylor) is on computing higher order derivative objects (gradients, Jacobians, Hessians, etc.) for problems like optimization and the solution of nonlinear equations.
Of course, it may also be used to numerically verify handcoded implementations of said derivative objects.

## Interface

```python
def diff(fun,x,order,args=(),mask=None,rule='forward',delta=None,
         idx_order='default'):
    """
    fun : {function}
        function whose derivative is sought
        has function definition
            def fun(x,*args):
    x : {scalar, array}
        independent variable with respect to which the derivative
            will be computed
    order : {integer}
        order of desired derivative
        1: first derivative (gradient),
        2: second derivative (Hessian), ...
    args : {tuple}
        tuple of additional arguments to fun
    mask : {integer or array}
        array of same shape as the returned derivative where
            element = 1 -> this entry should be computed,
            element = 0 -> entry should not be computed
    rule : {string}
        finite difference rule
        choose from: {'forward','backward','central'}
    delta : {float or array}
        scalar/array of same shape as x that specifies the finite
            difference step size
    idx_order : {string}
        string indicating how indices of derivative object should be
            ordered when returned
        'default' : indices corresponding to derivatives are
                        ordered first
        'natural' : indices corresponding to elements of function
                        output are ordered first (like in Jacobians)
    """
```


## Examples

The first example computes the first derivative of the matrix vector product `f(A,x) = A x` with respect to both the matrix `A` and vector `x`.

```python
import numpy as np
import taylor as ta

# both functions compute matrix vector product,
# but have different first arguments
def matvec_vec(x,A):
    return A @ x

def matvec_mat(A,x):
    return A @ x

if (__name__ == "__main__"):
    # set matrix and vector
    A = np.array([[1.0,2.0,3.0],
                  [2.0,4.0,5.0],
                  [3.0,5.0,6.0]])
    x = np.array([1.0,2.0,3.0])

    # derivative of matrix vector product with respect to vector
    deriv_matvec_vec = ta.diff(matvec_vec,x,1,args=(A,))
    print(f'df / dx :\n{deriv_matvec_vec}\n')

    # derivative of matrix vector product with respect to matrix
    deriv_matvec_mat = ta.diff(matvec_mat,A,1,args=(x,))
    print(f'df / dA :\n{deriv_matvec_mat}')
```


## Namesake

The package is named after [Brook Taylor](https://en.wikipedia.org/wiki/Brook_Taylor), the namesake for Taylor series and the originator of finite differences.

