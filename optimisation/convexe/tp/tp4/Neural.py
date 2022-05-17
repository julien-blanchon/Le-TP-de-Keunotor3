import numpy as np

class MLP() :
	def __init__(self,inp,outp,p=2,q=20,r=1) :
		self.inp=inp
		self.outp=outp
		self.p=p # taille de la première couche
		self.q=q # taille de la deuxième couche
		self.r=1 # taille de la troisième couche
		self.ind_s=(0,p*q,p*q+q,p*q+q+q*r) # indice de debut de stockage des variables
		self.ind_e=(p*q,p*q+q,p*q+q+q*r,p*q+q+q*r+r) # indice de fin de stockage des variables
		self.shapes=((q,p),(q,1),(r,q),(r,1)) #taille des variables
		self.nb_params=self.ind_e[-1] #taille totale du vecteur de paramètres
	def eval(self,theta) :
		(inp1,inp2,inp3,inp4)=self.forward(theta)
		return inp4
	def grad(self,theta) :
		state=self.forward(theta)
		gstate,gtheta=self.backward(theta,state)
		return gtheta

	def get_matrices(self,theta) :
		#A, b, C, d = None  # TODO
		p = self.p
		q = self.q
		r = self.r
		A = theta[0:p*q]
		A = A.reshape((q, p))
		b = theta[(p*q): (p*q)+q]
		b = b.reshape(q, 1)
		C = theta[(p*q+q):(p*q+q)+q*r]
		C = C.reshape(1, q*r)
		d = theta[(p*q+q+q*r):(p*q+q+q*r)+r]
		d = d.reshape(r, 1)
		return (A,b,C,d)
	def get_theta(self,matrices) :
		theta=np.zeros(self.nb_params)
		for (i_s,i_e,m,s) in zip(self.ind_s,self.ind_e,matrices,self.shapes) :
			#print(f"{m.shape} <--> {s}")
			assert m.shape==s
			theta[i_s:i_e]=m.ravel()
		return theta
	def product(self,A,b,x) :
		return A.dot(x)+np.outer(b,np.ones(x.shape[1]))
	def forward(self,theta) :
		A, b, C, d = self.get_matrices(theta)
		inp = self.inp
		outp = self.outp
		inp1 = self.product(A, b, inp)
		inp2 = self.sigmoid(inp1)
		inp3 = self.product(C, d, inp2)
		inp4 = np.linalg.norm(inp3-outp, 2)**2/2
		state = (inp1, inp2, inp3, inp4)
		return state
	def sigmoid_prime(self, x):
		return np.exp(-x)/(1+np.exp(-x))**2
	def sigmoid(self, x):
		return 1/(1+np.exp(-x))
	def diff(self,theta,state,dtheta) :
		A, b, C, d = self.get_matrices(theta)
		dA, db, dC, dd = self.get_matrices(dtheta)
		inp = self.inp
		outp = self.outp
		inp1, inp2, inp3, inp4 = state
		dinp1 = dA.dot(inp) + db
		dinp2 = dinp1*self.sigmoid_prime(inp1)
		dinp3 = C.dot(dinp2) + dC.dot(inp2) + dd
		dinp4 = dinp3.dot(np.transpose(inp3-outp))
		dstate = (dinp1, dinp2, dinp3, dinp4)
		return dstate
	def backward(self,theta,state) :
		# On cherche un vecteur gtheta tq dinp4 = <gtheta|dtheta>
		A, b, C, d = self.get_matrices(theta)
		inp1, inp2, inp3, inp4 = state
		inp = self.inp
		outp = self.outp
		# On remplaceras dans les calculs les dinp par les ginp
		# dinp4 	= <p|dinp3> = <ginp3|dinp3>
		# 			= <ginp3|dC*inp2+dd> + <ginp3|C*dinp3>
		#			= <>
		ginp4 = np.array([1.0])
		ginp3 = ginp4*(inp3-outp)
		gC = ginp3.dot(inp2.T)
		gd = np.sum(ginp3, axis=1, keepdims=True)
		ginp2 = C.T*ginp3
		ginp1 = ginp2*self.sigmoid_prime(inp1)
		gA = ginp1.dot(inp.T)
		gb = np.sum(ginp1, axis=1, keepdims=True)
		
		gstate = (ginp1, ginp2, ginp3, ginp4)
		gtheta = (gA, gb, gC, gd)
		gtheta = self.get_theta(gtheta)
		return gstate, gtheta
	
