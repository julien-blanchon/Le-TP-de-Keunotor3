#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:34:48 2021

@author: cantin
"""

import numpy as np
import numpy.linalg as npl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
#  Discrétisation en espace

# =============================================================================
### Parameters
xmin = 0.0; xmax = 2.0; nptx = 61; nx = nptx-2  
hx = (xmax-xmin)/(nptx -1)
xx = np.linspace(xmin,xmax,nptx) 
xx = xx.transpose()
xxint = xx[1:nx+1]
ymin = 0.0; ymax = 1.0; npty = 31; ny = npty-2 
hy = (ymax-ymin)/(npty -1)
yy = np.linspace(ymin,ymax,npty)
yy=yy.transpose() 
yyint = yy[1:ny+1]

mu = μ = 0.01  # Diffusion parameter
vx = 1 # Vitesse along x

cfl = 0.2  # cfl =mu*dt/hx^2 + mu*dt/hy^2 ou v*dt/h
# dt = (hx**2)*(hy**2)*cfl/(mu*(hx**2 + hy**2)) # dt = pas de temps
dt = cfl*hx/vx
Tfinal = 0.8   # Temps final souhaité

method_euler_explicite = True
method_euler_implicite = False
method_michelson = False
# =============================================================================


###### Matrice de Diffusion Dir/Neumann
#MATRICE C
def C(Nx):
  Cm = (-μ/hy**2)*np.eye((Nx+2))
  Cm[0, 0] = Cm[-1, -1] = 0
  return Cm

#MATRICE B
def B(Nx):
  Bm = μ*((2/hx**2)+(2/hy**2))*np.eye((Nx+2)) +\
      (-μ/hx**2)*np.roll(np.eye((Nx+2)), shift=1, axis=1) +\
      (-μ/hx**2)*np.roll(np.eye((Nx+2)), shift=-1, axis=1)
  Bm[0, 0] = 1
  Bm[0, 1] = Bm[0, -1] = 0
  Bm[-1, -2] = Bm[-1, 0] = 0
  # Ajout sur Gamma_1
  Bm[-1, -1] = -3/(2*hx)
  Bm[-1, -2] = 4/(2*hx)
  Bm[-1, -3] = -1/(2*hx)
  return Bm


#MATRICE A
def A(Nx, Ny):
  kronI = np.zeros((Ny+2, Ny+2))
  kronI[0, 0] = kronI[-1, -1] = 1
  Im = np.eye(Nx+2)

  kronC = np.roll(np.eye(Ny+2), shift=+1, axis=1) + \
      np.roll(np.eye(Ny+2), shift=-1, axis=1)
  kronC[0, -1] = kronC[-1, 0] = 0
  kronC[0, 1] = kronC[-1, -2] = 0
  Cm = C(Nx)

  kronB = np.eye(Ny+2)
  kronB[0, 0] = kronB[-1, -1] = 0
  Bm = B(Nx)
  Am = np.kron(kronI, Im) + np.kron(kronC, Cm) + np.kron(kronB, Bm)
  return Am

K2D = A(nx, ny)


#### Matrice de Convection  (Centré)
def D(Nx):
  Dm = vx*(np.diag([0] + [0.5/hx]*Nx, 1) - np.diag([0.5/hx]*Nx + [0], -1))
  return Dm

def Conv(Nx, Ny):
  kronD = np.eye(Ny+2)
  kronD[0, 0] = kronD[-1, -1] = 0
  Dm = D(Nx)
  Convm = np.kron(kronD, Dm)
  return Convm


V2Dx = Conv(nx, ny)
#### Global matrix : diffusion + convection
#A2D = -(K2D + V2Dx) #-mu*Delta + V.grad
A2D = K2D + V2Dx
#
#
##  Cas explicite
u = np.zeros((nx+2)*(ny+2))
u_ex = np.zeros((nx+2)*(ny+2))
err = np.zeros((nx+2)*(ny+2))
F = np.zeros((nx+2)*(ny+2))
#
#
# =============================================================================
# Time stepping
# =============================================================================
s0 = 0.1
x0 = 0.25
y0 = 0.5

def Sol_init(x):
  return np.exp( -((x[0]-x0)/s0)**2 -((x[1]-y0)/s0)**2   )

def Sol_init2(x):
  return np.maximum(0, s0**2 - (x[0] - x0)**2 - (x[1] - y0)**2)

u_init = np.zeros((nx+2)*(ny+2))
for i in range(nptx):
  for j in range(npty):
    coord = np.array([xmin+i*hx,ymin+j*hy])
    # u_init[j*(nx+2) + i] = Sol_init(coord)
    u_init[j*(nx+2) + i] = Sol_init(coord)
            
             
uu_init = np.reshape(u_init, (nx+2 ,ny+2), order = 'F');
fig = plt.figure(figsize=(10, 7))
X,Y = np.meshgrid(xx,yy)
ax = plt.axes(projection='3d')
surf = ax.plot_surface(X, Y, uu_init.T, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
ax.view_init(60, 35)
plt.pause(1.)
             
## Initialize u by the initial data u0
u = u_init.copy()

# Nombre de pas de temps effectues
nt = int(Tfinal/dt)
Tfinal = nt*dt # on corrige le temps final (si Tfinal/dt n'est pas entier)

# Time loop
for n in range(1,nt+1):

  # Schéma explicite en temps
  
  # Euler explicite u_{n+1} = x_n + dt*f(x_n)
  u = u - dt*np.dot(A2D, u)
  # #Euler implicite u_{n+1} = x_n + dt*f(x_{n+1}) <---> x_{n+1} = x_n + dt*A*x_{n+1} <---> (I - dt*A)*x_{n+1} = x_n
  # I = np.eye((nx+2)*(ny+2))
  # u = np.linalg.solve(I+dt*A2D, u)
  # Michelson u_{n+1} = x_n + 0.5*dt*f(x_n) + 0.5*dt*f(x_{n+1}) <---> (I - 0.5*dt*A)*u_{n+1} = x_n + 0.5*dt*A*x_n
  # I = np.eye((nx+2)*(ny+2))
  # u = np.linalg.solve(I+0.5*dt*A2D, u + 0.5*dt*np.dot(-A2D, u))


 # Print solution
  if n%5 == 0:
    plt.figure(1)
    plt.clf()
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection='3d')
    
    #ax.set_zlim(0, 1)
    uu = np.reshape(u, (nx+2, ny+2), order='F')
    surf = ax.plot_surface(X, Y, uu.T, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
    ax.view_init(60, 35)
    plt.title(['Schema explicite avec CFL=%s' %(cfl), '$t=$%s' %(n*dt)])
    plt.pause(0.1)

plt.show()
####################################################################
# comparaison solution exacte avec solution numerique au temps final
j0 = int((npty-1)/2)


plt.figure(2)
plt.clf()
x = np.linspace(xmin,xmax,nptx)
plt.plot(x, uu_init[:, j0], x, uu[:, j0], 'k')  # ,x,uexacte,'or')
# ,'solution exacte'],loc='best')
plt.legend(['Solution initiale', 'Schema explicite =%s' % (cfl)])
plt.show()

