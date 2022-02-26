
import numpy as np
from numpy import ma
import taylor as ta


if (__name__ == "__main__"):
    print()
    print(f'--------------------- ERROR TEST ---------------------')
    print()

    measured = np.array([40,1e-15,20,20e9])
    exact    = np.array([-1e-15,1e-16,20,50e8])
    rel_error_analytical = np.ma.array([np.nan,np.nan,0.0,3.0],
                                       mask=[1,1,0,0])

    print(f'measured : {measured}\n')
    print(f'exact : {exact}\n')
    print(f'exact relative error : {rel_error_analytical}\n')


    # compute relative error
    rel_error = ta.rel_error(measured,exact)
    print(f'relative error : {rel_error}\n')

    rel_error_correct = (np.max(np.abs(rel_error_analytical -
                                        rel_error)) == 0.0)

    if (rel_error_correct):
        print('  PASSED')
    else:
        print('  *******FAILED*******')
