
import itertools
import numpy as np


def diff(fun,x,order,args=(),mask=None,rule='forward',delta=None):
    """
    fun : {function}
        function whose derivative is sought
        has function definition
            def fun(x,*args):
    x : {scalar, array}
        independent variable the derivative will be computed with respect to
    order : {integer}
        number of derivatives to take
    args : {tuple}
        additional arguments to fun
    mask : {integer or array}
        array of same shape as the returned derivative
        element 1 signifies this entry should be computed, element 0
            signifies entry should not be computed
        TODO: change over to using sparse masks or masked arrays, etc.
    rule : {string}
        finite difference rule
        choose from : {'forward','backward','central'}
    delta_vec : {float or array}
        scalar/array of same shape as x that specifies the finite difference
            step size
    """

    if (not isinstance(args,tuple)):
        print(f'ERROR: optional args input must be at tuple')

    
    # run test evaluation to assess output shape
    fun_output = fun(x,*args)

    if (isinstance(fun_output,float)):
        fun_output_shape = ()
    elif (isinstance(fun_output_shape,np.ndarray)):
        fun_output_shape = fun_output.shape
    
    # get dimension of x
    if (isinstance(x,(float,int))):
        x = float(x)
        x_shape = (1,)
    elif (isinstance(x,np.ndarray)):
        x_shape = x.shape
            
    # partition modes of output into derivatives and output
    derivative_index_space = [dim for dim in list(x_shape)]*order
    output_index_space = list(fun_output_shape)
    derivative_shape =  derivative_index_space + output_index_space 

    derivative = np.zeros(derivative_shape)

    print(f'derivative shape : {derivative_shape}')

    # set finite differences step size(s)
    if (delta is None):
        step_size = 1e-6 # default step size
        delta = np.full(x_shape,step_size)
    elif (isinstance(delta,float)):
        step_size = delta
        delta = np.full(x_shape,step_size)
    elif (isinstance(delta,np.nd.array)):
        if (x.shape != delta.shape):
            print(f'ERROR: setting delta as array requires it be the same shape as x')
    else:
        print(f'ERROR: delta must be one of {None,float,array}')
        
        
    # store derivative indices at front of array so one can use the a[i] convention
    # will need to reverse this order before output?

    index_range_array = [np.arange(elem,dtype='i') for elem in derivative_index_space]
    multi_index_iterator = itertools.product(*index_range_array) #iterator of tensor 

    for i_m in multi_index_iterator:
        derivative[i_m] = 4 #TODO: call rule function here

        print(f'{i_m}')

    # TODO: try Jacobian next to rule out edgecases introduced in first pass
    #       try fun(x,A) = A @ x (derivative with respect to A)

