import sys
import numpy as np # type: ignore

def CrearPoblacion(n, p):
    Poblacion = np.zeros((p,n),int)
    for i in range(p):
        Poblacion[i]=np.arange(n)
        np.random.shuffle(Poblacion[i])
    return Poblacion

def ContarFitness(Poblacion,n,p):
    fitness= np.zeros(p,float)
    for i in range(p):
        contador = 0
        for j in range(n):
            for k in range(j+1,n,1):
                if((Poblacion[i][j]+j) == (Poblacion[i][k]+k)):
                    contador +=1
                if((Poblacion[i][j]-j) == Poblacion[i][k]-k):
                    contador+=1
        fitness[i] = (1/contador)
    return fitness

def CrearRuleta(Fitness,p):
    Ruleta = np.zeros(p,float)
    proporcion = Fitness/Fitness.sum()
    Ruleta[0]=proporcion[0]
    for i in range (1,p):
        Ruleta[i] = Ruleta[i-1]+proporcion[i]
    return Ruleta

def NuevaPoblacion(Poblacion,Ruleta,n,p):
    i = 0
    contador = 0
    random = np.random.rand()
    NuevaPoblacion = np.zeros((p,n),int)
    individuo1 = np.zeros(n,int)
    individuo2 = np.zeros(n,int)
    while random<Ruleta[i] and contador<2:
        if(random>Ruleta[i] and contador==0):
            individuo1 = Poblacion[i]
            contador+=1
            i=0
        elif(random>Ruleta[i] and contador==1)
            individuo2=Poblacion[i]
            contador+=1




if len(sys.argv)==7:
    semilla = int(sys.argv[1])
    n = int(sys.argv[2]) #tamaño del tablero y cantidad de reinas
    p = int(sys.argv[3]) #poblacion
    ite = int(sys.argv[4]) #iteracion (generaciones) 
    pc = float(sys.argv[5])/100 #probabilidad de cruza
    pm = float(sys.argv[6])/100 #probabilidad de mutación
    print(semilla, n, p, ite, pc, pm)
else:
    print("Error en la entrada de los parámetros")
    print("Los parámetros a ingresar son: Semilla TamañoTablero TamañoPoblacion Iteraciones ProbabilidadCruza ProbabilidadMutación")
    sys.exit(0)

np.random.seed(semilla)

Poblacion = CrearPoblacion(n,p)
print(Poblacion)
Fitness = ContarFitness(Poblacion,n,p)
print(Fitness)
Ruleta=CrearRuleta(Fitness,p)
print(Ruleta)
random = np.random.rand()
print(random)




