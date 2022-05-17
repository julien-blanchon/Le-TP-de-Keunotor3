import numpy as np

class BFGS(object):
    def __init__(self, nb_stock_max:int = 8) -> None:
        self.nb_stock_max = nb_stock_max
        self.stock = []
        self.last_iter = []
        super().__init__()

    def push(self, x, grad):
        if len(self.last_iter)>0:
            xk_m, gradk_m = self.last_iter[-1]
        else:
            xk_m, gradk_m = 0.0, 0.0
        sk = x - xk_m
        yk = grad - gradk_m #yk = gk ?
        rhok = 1.0/np.dot(sk, yk)
        if rhok>0:
            if len(self.stock) >= self.nb_stock_max:
                self.stock.pop(0)
                self.stock.append((sk, yk, rhok))
            else:
                self.stock.append((sk, yk, rhok))
        else:
            print("warning")
            self.stock = []
        self.last_iter.append((x, grad))
    
    def get(self, grad):
        if len(self.stock) == 0:
            return -grad
        r = -grad
        alpha = []
        for i, (si, yi, rhoi) in enumerate(reversed(self.stock)):
            alpha.append(rhoi*np.dot(si,r))
            r = r - alpha[i]*yi
        sk, yk, rhok = self.stock[-1]
        r = r*(np.dot(sk, yk)/np.dot(yk, yk))
        beta = []
        for i, (si, yi, rhoi) in enumerate(self.stock):
            beta.append(rhoi*np.dot(yi, r))
            r = r + (alpha[i]-beta[i])*si
        return r


def optim_bfgs(J, x_0, itermax=500, tol=1.e-5, e1=1.e-4, e2=0.99, itermax_W=100):
    k = 0
    xk = x_0
    norm_gradJk = np.inf
    bfgs = BFGS(nb_stock_max=8)

    s = 1  # Pas fixe

    x_list = [x_0]
    cost_list = []
    grad_list = []
    step_list = []
    angle_list = []
    while (k < itermax) and (norm_gradJk >= tol):
        k += 1
        gradJk = J.grad(xk)
        bfgs.push(xk, gradJk)
        norm_gradJk = np.linalg.norm(gradJk)
        #Calcul de dk par LBFGS
        dk = -bfgs.get(gradJk)
        angle = np.dot(dk, gradJk) / (np.linalg.norm(dk)
                                      * np.linalg.norm(gradJk))
        cos_angle = np.cos(angle)

        #Wolf
        s_sup = np.inf
        s_inf = 0.0
        def phi(s): return J.eval(xk+s*dk)
        def phi_prime(s): return np.dot(J.grad(xk+s*dk), dk)
        phi_prime_zero = phi_prime(0)
        phi_zero = phi(0)
        kw = 0
        while (kw < itermax_W) and ((phi(s) > phi_zero + e1*phi_prime_zero).all() or (phi_prime(s) < e2*phi_prime_zero).all()):
            kw += 1
            if (phi(s) > phi_zero + e1*phi_prime_zero).all():  # big
                s_sup = s
                s = (s_inf+s_sup)/2
            elif (phi_prime(s) < e2*phi_prime_zero).all():  # small
                s_inf = s
                s = min((s_inf+s_sup)/2, 2*s)
            big = phi(s) > phi(0) + e1*phi_prime(0)
        step = s
        # Fin de Wolf
        xk = xk + step*dk
        x_list.append(xk)
        cost_list.append(J.eval(xk))
        grad_list.append(norm_gradJk)
        step_list.append(step)
        angle_list.append(cos_angle)

    to_return = {}
    to_return["x_list"] = x_list
    to_return["cost_list"] = cost_list
    to_return["grad_list"] = grad_list
    to_return["step_list"] = step_list
    to_return["angle_list"] = angle_list

    return to_return

    
    
    

        

