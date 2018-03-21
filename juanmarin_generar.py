import numpy as np 
import matplotlib.pyplot as plt 

# la funcion 1 que retorna N valores N numeros aleatorios siguiendo la distribuci ́on discreta de probabilidad

def sample_1(N): 
	a = [-10,-5,3,9]
	sample_1 = np.random.choice(a,N,p = [0.1,0.4,0.2,0.3])
	return sample_1 
# La funcion 2 que retorna la distribucion de probabilidad exponencial
def sample_2(N): 
	beta = 0.5 
	sample_2 = np.random.exponential(beta, N)
	return sample_2 

#tercera funcion que genera y retorna un arreglo con M promedios para un sampling que le entra como parametro

def get_mean(sampling_fun,N,M):
	promedios=[] 
	for i in range(len(M)):
		promedios.append(np.mean(sampling_fun(N)))
		return promedios 

#ejecutar las funciones para crear archivos de texto conlos promedios de M(10000) asociados a los valores de la lista N
aso= [10,100,1000]
M = 10000
for i in range(len(aso)):
	
	array1= get_mean(sample_1(N),aso,M)
	if(aso == 10):
		np.savetxt("sample_1_10.txt", array1)
	elif (aso == 100):
		np.savetxt("sample_1_100.txt", array1)
	elif (aso == 1000):
		np.savetxt("sample_1_1000.txt", array1)

for j in range (len(aso)):
	array2 = get_mean(sample_2(N),asp,M)
	if(aso == 10):
		np.savetxt("sample_2_10.txt", array2)
	elif (aso == 100):
		np.savetxt("sample_2_100.txt", array2)
	elif (aso == 1000):
		np.savetxt("sample_2_1000.txt", array2)



get_mean(sample_1, N , 10000 )

