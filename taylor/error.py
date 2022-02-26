
import numpy as np
from numpy import ma


def rel_error(measured,exact):
    """
    computes the relative error between two scalars or arrays
    in a way robust to division by zero

    ---Inputs---
    measured : {scalar, array}
        measured or approximate value(s)
    exact: {scalar, array}
        exact value(s)

   ---Outputs---
    error_rel : {scalar, array}
        elementwise relative error (signed)
    """
    zero_threshold = 1e-14
    exact_masked = np.ma.masked_where(np.abs(exact) < zero_threshold,
                                      exact)
    error_rel = (measured - exact_masked)/exact_masked
    return error_rel
