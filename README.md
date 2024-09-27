# Problema N reinas

 >Se resolvera el problema de las n reinas mediante un algoritmo metahuristico, a medida que pasen las clases
>

 >[!important]
 >Recuerda instalar la biblioteca **Numpy** con pip3 install Numpy.
>

## Funcionamiento basico del codigo
### Metodología

> 1. Se utiliza un algoritmo genetico el cual se crea a partir de una población inicial, de manera aleatoria, evitando los choques verticales y horizontales en el tablero.
>
> 2. Se calcula un Fitness la cual es una función que calcula cuantas veces chocan las reinas de manera diagonal a mayor cantidad de choques
>menor es el Fitnees.
>
> 3. Luego se crea una Ruleta donde el tablero que tenga menos choques tenga mayor probabilidad de ser escogido como padre de la siguiente generación.
>
> 4. Una vez elegidos los dos Padres se cruzan ambos para generar dos hijos y asi sucecivamente hasta obetener una nueva población.
>
> 5. se procede a hacer un nuevo calculo de fitness esperando que esta vez no hayan choques y si los hay se procede a hacer lo mismo explicado anteriormente
>hasta encontrar un tablero donde no haya choques o hasta que lleguemos a la ultima generación propuesta.
>
### Que colocar en la terminal

>[!TIP]
>En la terminal se coloca python Nreinas.py [semilla] [Tamaño del tablero] [Poblacion] [generaciones] [probabilidad de cruza] [probabilidad de mutacion]
>
### Integrantes:
* Débora Huerta
* Christopher Moyano
* Matias Olave
