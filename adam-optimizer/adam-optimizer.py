import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here

    # converting list to np array 
    param=np.array(param,dtype=float)
    grad=np.array(grad,dtype=float)
    m=np.array(m,dtype=float)
    v=np.array(v,dtype=float)
    
    #  Update biased first moment estimate (moving average of gradients) 
    m_new=beta1*m+(1-beta1)*grad

    # Update biased second moment estimate (moving average of squared gradients)
    v_new=beta2*v+(1-beta2)*(grad*grad)

    # Compute bias-corrected first moment (to fix initialization bias)
    m_hat=m_new/(1-beta1**t)
    
    # Compute bias-corrected second moment
    v_hat=v_new/(1-beta2**t)

    # Update parameters using Adam update rule
    param_new=param-lr*(m_hat/((np.sqrt(v_hat)+eps)))

    return param_new,m_new,v_new
    
    pass