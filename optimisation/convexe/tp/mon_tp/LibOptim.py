import numpy as np
import scipy.linalg as ln

def direction_gradient(F, x):
    gradF = F.grad(x)
    direction = gradF
    return -direction

def direction_newton(F, x):
    gradF = F.grad(x)
    hessF = F.Hess(x)
    direction = ln.solve(hessF, gradF)
    return -direction

def fixed_step(F, xk, Fk, gradFk, direction, previous_step):
    return 0.001

def wolf_step(F, xk, Fk, gradFk, direction, previous_step):
    e1 = 1.e-4
    e2 = 0.99
    itermax_W = 100

    s = previous_step
    s_sup = np.inf
    s_inf = 0.0
    do_Wolfe = True

    k = 0
    while (k < itermax_W) and do_Wolfe:
        k += 1
        Fk_new = F.eval(xk + s*direction)
        gradFk_new = F.grad(xk + s*direction)

        if Fk_new > Fk + e1*s*np.dot(gradFk, direction):
            s_sup = s
            s = 0.5*(s_sup+s_inf)
        else :
            if np.dot(gradFk_new, direction) < e2*np.dot(gradFk, direction):
                s_inf = s
                s = min(0.5*(s_inf+s_sup), 2*s_inf)
            else :
                do_Wolfe=False
                
    return s
