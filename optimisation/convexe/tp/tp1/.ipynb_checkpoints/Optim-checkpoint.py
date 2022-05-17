import numpy as np

def deriv_num(J,a,d,compute_grad=True,compute_Hess=True) :
    eps_range=[0.1**(i+1) for i in range(12)]
    for eps in  eps_range:
        s = 'eps {:1.3e}'.format(eps)
        print("\t" + s)
        
        if compute_grad:
            b = (J.eval(a+eps*d) - J.eval(a))/eps
            c = np.dot(J.grad(a), d)
            err = abs(b/c - 1)
            print("\t Err Grad :" + str(err))
        if compute_Hess: 
            b = (J.grad(a+eps*d) - J.grad(a))/eps
            c = np.dot(J.Hess(a), d)
            ratio = abs(np.linalg.norm(b)/np.linalg.norm(c) - 1)
            angle = abs(np.dot(b,c)/(np.linalg.norm(b)*np.linalg.norm(c)) - 1)
            print("\t Err Hess :" + str(ratio))
            print("\t Angle Hess :" + str(angle))
            
def fixed_step(J, x_0, step=1., itermax=500, tol=1.e-5):
    k = 0
    xk = x_0
    norm_gradJk = tol

    liste_xk = [x_0]  
    liste_Jk = []
    liste_normgradJk = []
    while (k < itermax) and (norm_gradJk >= tol) :
        k += 1
        gradJk = J.grad(xk)
        norm_gradJk = np.linalg.norm(gradJk)
        alphak = step
        xk = xk - alphak*gradJk
        liste_xk.append(xk)
        liste_Jk.append(J.eval(xk))
        liste_normgradJk.append(norm_gradJk)
        
        
    return liste_xk, liste_Jk, liste_normgradJk


def wolfe(J, x_0, e1=1.e-4, e2=0.99, itermax=500, itermax_W=20, tol=1.e-5):
    k = 0
    xk = x_0
    norm_gradJk = tol
    
    step_list = []
    liste_xk = [x_0]  
    liste_Jk = []
    liste_normgradJk = []

    s = 1
    #Descente de gradient
    while (k < itermax) and (norm_gradJk >= tol) :
        k += 1
        gradJk = J.grad(xk)
        dk = -gradJk
        norm_gradJk = np.linalg.norm(dk)
        
        #Wolf
        s_sup = 0.0
        s_inf = 1000
        
        phi = lambda s: J.eval(xk+s*dk) - gradJk
        phi_prime = lambda s: np.dot(J.grad(xk+s*dk), dk)
        
        big = not(phi_prime(s) > e2*phi_prime(0)).any()
        small = not(phi(s) < e1*phi_prime(0)).any()
        
        kw = 0
        while (kw < itermax_W) and (big or small):
            kw += 1
            if big:
                s_sup = s
                s = (s_inf+s_sup)/2
            if small:
                s_inf = s
                s = min((s_inf+s_sup)/2, 2*s)
            big = not(phi_prime(s) > e2*phi_prime(0)).any()
            small = not(phi(s) < e1*phi_prime(0)).any()
            
        xk = xk + s*dk
        step_list.append(s)
        liste_xk.append(xk)
        liste_Jk.append(J.eval(xk))
        liste_normgradJk.append(norm_gradJk)
        
    return liste_xk, liste_Jk, liste_normgradJk, step_list