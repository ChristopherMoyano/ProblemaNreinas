import sys
import numpy as np # type: ignore

def CrearPoblacion(n, p):
    Poblacion = np.zeros((p,n),int)
    for i in range(p):
        Poblacion[i]=np.arange(n)
        np.random.shuffle(Poblacion[i])
    return Poblacion

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




