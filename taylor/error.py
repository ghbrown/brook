
import numpy as np

# TODO: implement friendly error functin for user
#       something like below (make sure it makes sense)

# TODO: write rel_error test

def rel_error(measured,true):
    """
    computes the relative error between two scalars or arrays
    in a way robust to division by zero

    ---Inputs---
    measured : {scalar, array}
        measured or approximate value(s)
    true: {scalar, array}
        true value(s)

    ---Outputs---
    error_rel : {scalar, array}
        elementwise relative error
    """
    zero_threshold = 1e-14
    error_abs_val = np.abs(A_measured - A_true)

    # TODO: maybe just use a mask here too such that scary cases are
    #       just ignored

    #replaces all "zeroes" with ones to prevent divide by zero errors
    safe_denominator = np.where((np.abs(A_true) < zero_threshold),1.0,
                                np.abs(A_true))

    #compute relative error elementwise
    error_rel = error_abs_val/safe_denominator
    return error_rel
