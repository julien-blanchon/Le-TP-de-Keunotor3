import numpy as np

class square() :
	def __init__(self) :
		#print("Fonction (x,y) --> x^2/2+7/2*y^2")
		self.size=2
		self.fcounter = 0
		self.gcounter = 0
		self.hcounter = 0
	def eval(self,x) :
		if not len(x)==self.size :
			print ("Erreur de taille de x, on a ", len(x), " au lieu de ", self.size)
		self.fcounter += 1
		return 0.5*x[0]**2+7/2.*x[1]**2
	def grad(self,x) :
		self.gcounter += 1
		return np.array([x[0],7*x[1]])
	def Hess(self,x) :
		to_return=np.zeros((2,2))
		to_return[0,0]=1
		to_return[1,1]=7
		self.hcounter += 1
		return to_return

class Rosen() :
	def __init__(self) :
		#print("Fonction (x,y) --> 100*(y-x^2)^2 + (1-x)^2")
		self.size=2
		self.fcounter = 0
		self.gcounter = 0
		self.hcounter = 0
	def eval(self,x) :
		if not len(x)==self.size :
			print ("Erreur de taille de x, on a ",len(x)," au lieu de ",self.size)
		self.fcounter += 1
		return 100*(x[1]-x[0]**2)**2 + (1-x[0])**2
	def grad(self,x) :
		self.gcounter += 1
		return np.array([-400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0]), 200*(x[1]-x[0]**2)])
	def Hess(self,x) :
		to_return=np.zeros((2,2))
		to_return[0,0]= 1200*x[0]**2 - 400*x[1] + 2
		to_return[0,1]= -400*x[0]
		to_return[1,0]= to_return[0,1]
		to_return[1,1]= 200
		self.hcounter += 1
		return to_return
	
class oscill() :
	def __init__(self) :
		#print("Fonction (x,y) --> (1/2)x^2 + xcos(y)")
		self.size=2
		self.fcounter = 0
		self.gcounter = 0
		self.hcounter = 0
	def eval(self,x) :
		if not len(x)==self.size :
			print ("Erreur de taille de x, on a ",len(x)," au lieu de ",self.size)
		self.fcounter += 1
		return (1/2)*x**2 + x*np.cos(x[1])
	def grad(self,x) :
		self.gcounter += 1
		return np.array([x[0]+np.cos(x[1]), -x[0]*np.sin(x[1])])
	def Hess(self,x) :
		to_return=np.zeros((2,2))
		to_return[0,0]= 1
		to_return[0,1]= -np.sin(x[1])
		to_return[1,0]= to_return[0,1]
		to_return[1,1]= -x[0]*np.cos(x[1])
		self.hcounter += 1
		return to_return