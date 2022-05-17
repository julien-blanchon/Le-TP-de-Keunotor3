import numpy as np
import scipy.linalg as ln

class Optimizer(object):
    def __init__(self, direction_finder, step_finder) -> None:
        self.direction_finder = direction_finder
        self.step_finder = step_finder
        super().__init__()
    
    def fit(self, F, x0, itermax=500, tol=1.e-5):
        k = 0
        xk = x0
        Fk = F.eval(xk)
        gradFk = F.grad(xk)
        norm_gradFk = np.inf

        previous_step = 0.01

        list_xk = [x0]
        list_Fk = []
        list_norm_gradJk = []
        list_step = []
        while (k<itermax) and (norm_gradFk >= tol):
            k += 1
            direction = self.direction_finder(F, xk)
            step = self.step_finder(F, xk, Fk, gradFk, direction, previous_step)
            xk = xk + step*direction
            Fk = F.eval(xk)
            gradFk = F.grad(xk)

            list_xk.append(xk)
            list_Fk.append(Fk)
            list_norm_gradJk.append(np.linalg.norm(gradFk))
            list_step.append(step)
    
        return list_xk, list_Fk, list_norm_gradJk, list_step


def wolfe(J, x_0, d=None, cost=None, grad=None, s=1.0, e1=1.e-4, e2=0.99, itermax=500, itermax_W=100, tol=1.e-5):
    k = 0
    xk = x_0
    norm_gradJk = np.inf

    step_list = []
    liste_xk = [x_0]
    liste_Jk = []
    liste_normgradJk = []

    s = 1
    #Descente de gradient
    while (k < itermax) and (norm_gradJk >= tol):
        k += 1
        gradJk = J.grad(xk)
        dk = -gradJk
        norm_gradJk = np.linalg.norm(dk)

        #Wolf
        s_sup = np.inf
        s_inf = 0.0

        def phi(s): return J.eval(xk+s*dk)
        def phi_prime(s): return np.dot(J.grad(xk+s*dk), dk)

        phi_prime_zero = phi_prime(0)
        phi_zero = phi(0)

        kw = 0
        while (kw < itermax_W) and ((phi(s) > phi_zero + e1*phi_prime_zero) or (phi_prime(s) < e2*phi_prime_zero)):
            kw += 1
            if (phi(s) > phi_zero + e1*phi_prime_zero):  # big
                s_sup = s
                s = (s_inf+s_sup)/2
            elif (phi_prime(s) < e2*phi_prime_zero):  # small
                s_inf = s
                s = min((s_inf+s_sup)/2, 2*s)
            big = phi(s) > phi(0) + e1*phi_prime(0)

        xk = xk + s*dk
        step_list.append(s)
        liste_xk.append(xk)
        liste_Jk.append(J.eval(xk))
        liste_normgradJk.append(norm_gradJk)
    # return liste_xk, ...
    """"Ajout TP2"""
    to_return = {}
    to_return["x_list"] = liste_xk
    to_return["cost_list"] = liste_Jk
    to_return["grad_list"] = liste_normgradJk
    to_return["step_list"] = step_list

    return to_return


def Newton(J, x_0, itermax=500, tol=1.e-5):
    k = 0
    xk = x_0
    norm_gradJk = np.inf

    step = 1  # Pas fixe

    x_list = [x_0]
    cost_list = []
    grad_list = []
    step_list = []
    angle_list = []
    while (k < itermax) and (norm_gradJk >= tol):
        k += 1
        gradJk = J.grad(xk)
        norm_gradJk = np.linalg.norm(gradJk)
        hessJk = J.Hess(xk)
        dk = ln.solve(hessJk, gradJk)
        angle = np.dot(dk, gradJk) / (np.linalg.norm(dk)
                                      * np.linalg.norm(gradJk))
        cos_angle = np.cos(angle)
        xk = xk - step*dk
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


def Newton_Wolfe(J, x_0, itermax=500, tol=1.e-5, e1=1.e-4, e2=0.99, itermax_W=100):
    k = 0
    xk = x_0
    norm_gradJk = np.inf

    s = 1  # Pas fixe

    x_list = [x_0]
    cost_list = []
    grad_list = []
    step_list = []
    angle_list = []
    while (k < itermax) and (norm_gradJk >= tol):
        k += 1
        gradJk = J.grad(xk)
        norm_gradJk = np.linalg.norm(gradJk)
        hessJk = J.Hess(xk)
        dk = -ln.solve(hessJk, gradJk)
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
