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
from matplotlib import cm

#  Discrétisation en espace


xmin = 0.0; xmax = 1.8; nptx = 16; nx = nptx-2  
hx = (xmax-xmin)/(nptx -1)
xx = np.linspace(xmin,xmax,nptx) 
xx = xx.transpose()
xxint = xx[1:nx+1]
ymin = 0.0; ymax = 1.0; npty = 16; ny = npty-2 
hy = (ymax-ymin)/(npty -1)
yy = np.linspace(ymin,ymax,npty)
yy=yy.transpose() 
yyint = yy[1:ny+1]


mu = μ = 1;
#Matrix A implementation

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
    Bm[0, 0] = Bm[-1, -1] = 1
    Bm[0, 1] = Bm[0, -1] = 0
    Bm[-1, -2] = Bm[-1, 0] = 0
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




##  Solution and source terms
u = np.zeros((nx+2)*(ny+2)) #Numerical solution
u_ex = np.zeros((nx+2)*(ny+2)) #Exact solution
F = np.zeros((nx+2)*(ny+2)) #Source term
#
#
# Source term
def Source_int(x):
    return 2*np.pi**2*(np.sin(np.pi*x[0])*np.sin(np.pi*x[1]))
def Source_bnd(x):
    return np.sin(np.pi*x[0])*np.sin(np.pi*x[1])
def Sol_sin(x):
    return np.sin(np.pi*x[0])*np.sin(np.pi*x[1])
for i in range(nptx):
    for j in range(npty):
        coord = np.array([i*hx,j*hy])
        u_ex[j*(nx+2) + i] = Sol_sin(coord)
    if i==0 or i==nptx-1: # Boundary x=0 ou x=xmax
        for j in range(npty):
            coord = np.array([i*hx,j*hy])
            F[j*(nx+2) + i]=Source_bnd(coord)
    else:
        for j in range(npty):
            coord = np.array([i*hx,j*hy])  
            if j==0 or j==npty-1: # Boundary y=0 ou y=ymax
                F[j*(nx+2) + i]=Source_bnd(coord)
            else:
                F[j*(nx+2) + i]=Source_int(coord)

uu_num = np.linalg.solve(A(nx, ny), F)
uu_num = np.reshape(u_ex,(nx+2 ,ny+2),order = 'F');


#Post-traintement u_ex+Visualization of the exct solution
uu_ex = np.reshape(u_ex,(nx+2 ,ny+2),order = 'F');
X,Y = np.meshgrid(xx,yy)
fig = plt.figure(figsize=(20, 20))
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X,Y,uu_ex.T,rstride = 1, cstride = 1, cmap = cm.coolwarm)
ax1.plot_surface(X, Y, uu_num.T, rstride=1, cstride=1, alpha=0.5)
plt.title('Superposition des deux solutions')

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, uu_ex.T, rstride=1, cstride=1, cmap = cm.coolwarm)
plt.title("Solution Exacte")

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, uu_num.T, rstride=1, cstride=1, cmap = cm.coolwarm)
plt.title("Solution Numérique")
plt.show()