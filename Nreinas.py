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
        if (contador != 0):
            fitness[i] = (1/contador)
        else:
            fitness[i] = 1
    return fitness

def CrearRuleta(Fitness,p):
    Ruleta = np.zeros(p,float)
    proporcion = Fitness/Fitness.sum()
    Ruleta[0]=proporcion[0]
    for i in range (1,p):
        Ruleta[i] = Ruleta[i-1]+proporcion[i]
    return Ruleta

def eleccionPadres(Ruleta):
    random = np.random.rand()
    i=0
    contador=0
    padre1 = 0
    padre2 = 0
    while(random > Ruleta[i] or contador <2):
        if(random < Ruleta[i] and contador == 0):
            padre1 = i
            contador +=1
            random = np.random.rand()
            i=0
        elif(random < Ruleta[i] and contador ==1 and padre1!=i):
            padre2 = i
            contador +=1
        elif(random < Ruleta[i] and contador ==1 and padre1 == i):
            random = np.random.rand()
            i=0
        else:
            i+=1
    return padre1,padre2

def cruza(padre1,padre2):
    pto_corte=np.random.randint(1,n)
    hijo11=padre1[:pto_corte]
    hijo12=padre2[pto_corte:]
    hijo1=np.concatenate([hijo11,hijo12])
    hijo21=padre1[pto_corte:]
    hijo22=padre2[:pto_corte]
    hijo2=np.concatenate([hijo21,hijo22])

    #mejoramiento de los hijos valores repetidos
    m1 = np.zeros_like(hijo1, dtype=bool)
    m2 = np.zeros_like(hijo2, dtype=bool)
    m1[np.unique(hijo1, return_index = True)[1]] = True
    m2[np.unique(hijo2, return_index = True)[1]] = True
    for i in range(hijo1[~m1].size):
        repe1_idx = np.where(hijo1 == hijo1[~m1][i])
        repe2_idx = np.where(hijo2 == hijo2[~m1][i])
        idx = np.random.randint(2)
        aux = hijo1[repe1_idx[idx]]
        hijo1[repe1_idx[idx]] = hijo2[repe2_idx[np.absolute(idx-1)]]
        hijo2[repe2_idx[np.absolute(idx-1)]]=aux

    return hijo1,hijo2

def mutacion(hijo,n):
    intercambiar = np.random.choice(n,size=2,replace=False)
    aux = hijo[intercambiar[0]]
    hijo[intercambiar[0]] = hijo[intercambiar[1]]
    hijo[intercambiar[1]] = aux
    return hijo

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
Fitness = ContarFitness(Poblacion,n,p)
Ruleta=CrearRuleta(Fitness,p)

generacion = 0
#condiciones de termino mientras que no se terminen las generaciones o si se encuentra un tablero donde no choquen las reinas (fitness 1)
while (generacion < ite) and ~np.any(Fitness == 1):
    nuevaPoblacion = np.zeros((p,n),int)
    i=0
    while i < p:
        seCruza = np.random.rand()
        if(seCruza < pc):
            Padres = eleccionPadres(Ruleta)
            Hijos = cruza(Poblacion[Padres[0]],Poblacion[Padres[1]])
            nuevaPoblacion[i],nuevaPoblacion[i+1] = Hijos[0],Hijos[1]
            seMuta1= np.random.rand()
            seMuta2= np.random.rand()
            if(seMuta1< pm):
                nuevaPoblacion[i] = mutacion(nuevaPoblacion[i],n)
            if(seMuta2 < pm):
                nuevaPoblacion[i+1] = mutacion(nuevaPoblacion[i+1],n)
            i=i+2
    Poblacion = nuevaPoblacion
    Fitness = ContarFitness(Poblacion,n,p)
    Ruleta = CrearRuleta(Fitness,p)
                 
if (np.any(Fitness==1)):
    indices = np.where(Fitness == 1)[0]
    print("La mejor solucion encontrada es:")
    for i in indices:
        print(Poblacion[i])
else:
    indices = np.where(Fitness == np.max(Fitness))[0]
    print("no se encontro una solucion precisa, la más cercana es: ")
    for i in indices:
        print(Poblacion[i])
    