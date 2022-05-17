import numpy as np
from scipy import signal
from scipy import interpolate
from PIL import Image

def getGaussians() :
    n=21
    sigma=0.3
    [X,Y]=np.meshgrid(np.linspace(-1,1,n),np.linspace(-1,1,n), indexing='xy')
    Z = np.sqrt(X*X+Y*Y)  # Cercle en (0, 0)
    im1=np.zeros((n,n))
    im1[Z<=.7]=1.
    im1[Z<=.3]=.5
    im1[Z<=.1]=.7
    im2=np.zeros((n,n));
    Z=np.sqrt((X-.3)**2+(Y+.2)**2) # Cercle en (-0.3, 0.2)
    im2[Z<=.7]=1
    im2[Z<=.3]=.5
    im2[Z<=.1]=.7
    G=np.fft.fftshift(np.exp(-(X**2+Y**2)/sigma**2))
    # Transformer de fourrier d'une gausienne
    f=np.real(np.fft.ifft2(np.fft.fft2(G)*np.fft.fft2(im1))) #Convolution de im1 avec une gausienne
    g=np.real(np.fft.ifft2(np.fft.fft2(G)*np.fft.fft2(im2))) #Convolution de im2 avec une gausienne
    f=f/np.max(f)
    g=g/np.max(g)
    return f,g,(X,Y)

def interpol(f,u) :
    # function that computes f \circ Id+u and interpolates it on a mesh
    (ux,uy)=u
    nx,ny=f.shape
    ip=interpolate.RectBivariateSpline(np.arange(nx),np.arange(ny),f)
    [X,Y]=np.meshgrid(np.arange(nx),np.arange(ny), indexing='ij')
    X=X+ux
    Y=Y+uy
    return np.reshape(ip.ev(X.ravel(),Y.ravel()),(nx,ny))

def upscale(f,factor) :
    nx,ny=f.shape
    ip=interpolate.RectBivariateSpline(np.arange(nx),np.arange(ny),f)
    [X,Y]=np.meshgrid(np.arange(factor*nx),np.arange(factor*ny), indexing='ij')
    X=X/factor
    Y=Y/factor
    return np.reshape(ip.ev(X.ravel(),Y.ravel()),(factor*nx,factor*ny))

############################## CORRECTIONS
def dx(im):
    nx, ny = im.shape[0], im.shape[1]
    d = np.zeros(im.shape)
    d[:-1, :] = im[1:, :] - im[:-1, :]
    return d

def dy(im):
    d = np.zeros(im.shape)
    d[:, :-1] = im[:, 1:] - im[:, :-1]
    return d

def dyT(d):
    im = np.zeros(d.shape)
    # im[:, 0] = -d[:, -0]
    # im[:, 1:-2] = d[:, 0:-3] - d[:, 1:-2]
    # im[:, -1] = d[:, -2]
    im[:, 1:] = d[:, :-1]
    im[:, :-1] -= d[:, :-1]
    return im

def dxT(d):
    im = np.zeros(d.shape)
    # im[0, :] = -d[0, :]
    # im[1:-2, :] = d[0:-3, :] - d[1:-2, :]
    # im[-1, :] = d[-2, :]
    im[1:, :] = d[:-1, :]
    im[:-1, :] -= d[:-1, :]
    return im

class R() :
    def __init__(self,lam=10,mu=5) :
        self.lam=lam
        self.mu=mu
        self.nb_eval=0
        self.nb_grad=0
        self.nb_Hess=0
    def eval(self,u) :
        self.nb_eval+=1
        lam, mu = self.lam, self.mu
        ux, uy = u
        vec1 = (dx(uy)+dy(ux)).ravel()
        vec2 = (dx(ux)+dy(uy)).ravel()
        Ru = 0.5*( mu*np.dot(vec1, vec1) + (lam+mu)*np.dot(vec2, vec2) )
        # Il faut voir pour le ux et uy !
        # dyu = dy(u)
        # dxu = dx(u)
        # dyTdyu = dyT(dy(u))
        # dyTdxu = dyT(dx(u))
        # dxTdxu = dxT(dx(u))
        # dxTdyu = dxT(dy(u))
        # ru_11 = 0.5*( lam*dyTdyu + (lam+mu)*dxTdxu )
        # ru_12 = 0.5*( lam*dyTdxu + (lam+mu)*dxTdyu )
        # ru_21 = 0.5*( lam*dxTdyu + (lam+mu)*dyTdxu )
        # ru_22 = 0.5*( lam*dxTdxu + (lam+mu)*dyTdyu )
        # Ru = np.block(
        #     [ru_11, ru_12],
        #     [ru_21, ru_22]
        # )
        return Ru
    def grad(self,u) :
        self.nb_grad+=1
        lam, mu = self.lam, self.mu
        ux, uy = u
        vec1 = (dx(uy)+dy(ux))
        vec2 = (dx(ux)+dy(uy))
        gradRu_1 = mu*dyT(vec1) + (lam+mu)*dxT(vec2)
        gradRu_2 = mu*dxT(vec1) + (lam+mu)*dyT(vec2)
        return (gradRu_1, gradRu_2)
    def Hess(self,x) :
        assert False
        return 

class E() :
    def __init__(self,f,g) :
        self.f=f
        self.g=g
        self.nb_eval=0
        self.nb_grad=0
        self.nb_Hess=0
    def eval(self,u) :
        f, g = self.f, self.g
        Eu = 0.5*np.linalg.norm(interpol(f, u) - g)**2
        self.nb_eval+=1
        return Eu
    def grad(self,u) :
        self.nb_grad+=1
        f, g = self.f, self.g
        gradfu = [interpol(dx(f), u), interpol(dy(f), u)]
        interpf = interpol(f, u)
        # interpdx = interpol(dx(f), u)
        # interpdy = interpol(dy(f), u)
        gradfu = [dx(interp), dy(interp)]
        gradEu = (interp - g)*gradfu
        return gradEu
    def Hess(self,x) :
        assert False
        return 

class objectif() :
    def __init__(self,r,e) :
        self.r=r
        self.e=e
    def eval(self,u) :
        return self.e.eval(u)+self.r.eval(u)
    def grad(self,u) :
        return self.e.grad(u)+self.r.grad(u)

class MoindreCarres() :
    def __init__(self,e,r) :
        self.e=e
        self.r=r
        self.lam = r.lam
        self.mu = r.mu
        self.f = e.f
        self.g = e.g
        self.obj=objectif(e,r)
    def compute(self,u) :
        ux, uy = u
        psi_u1 = interpol(self.f, u)
        vec1 = (dx(uy)+dy(ux))
        vec2 = (dx(ux)+dy(uy))
        psi_u2 = np.sqrt(self.mu)*vec1
        psi_u3 = np.sqrt(self.mu+self.lam)*vec2
        psi = np.vstack([psi_u1, psi_u2, psi_u3])
        return psi
    def JPsi(self,u,h) :
        ux, uy = u
        psi_u1 = interpol(self.f, u)
        vec1 = (dx(uy)+dy(ux))
        vec2 = (dx(ux)+dy(uy))
        psi_u2 = np.sqrt(self.mu)*vec1
        psi_u3 = np.sqrt(self.mu+self.lam)*vec2
        psi = np.vstack([psi_u1, psi_u2, psi_u3])
        return 
    def JPsiT(self,u,Psi) :
        return 
    def LM(self,u,h,epsilon=0.) :
        return 
        
