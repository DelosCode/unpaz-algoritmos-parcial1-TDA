#Inicio de TDA Pila

class Pila:
    # Definimos el contructor   
    def __init__(self):
        # Inicializamos una 'pila vacía', el elemento contenedor es del
        # tipo de dato lista, donde se irán apilando los elementos.  
        self.lista = []
    
    # Método  que agrega un nuevo elemento a la pila (lista)    
    def apilar(self,item):
        self.lista.append(item)
        
    # Método  que quita el último elemento ingresado de la pila (lista)
    def desapilar(self):
        if self.vacia():
            #"No se puede desapilar la lista está vacía"
            return 
        else:
            #devuelve el elemento desapilado
            return self.lista.pop()
         
    # Método  que controla si la lista está vacía
    def vacia(self):
        if len(self.lista)==0:           
            return True
        else:           
            return False
    
    def mostrar(self):
        for i in self.lista[::-1]:
            print(f"[{str(i):^10}]")
        print()
#Fin de TDA Pila

#Inicio de TDA Cola
class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.lista_cola=[]
    
    def encolar(self, x):
        ''' Agrega el elemento x como último de la cola.  '''
        self.lista_cola.append(x)
    
    def desencolar(self) -> int:
        ''' Elimina el primer elemento de la cola y devuelve su
        valor.'''

        if not self.es_vacia():
            return self.lista_cola.pop(0)
           
    def es_vacia(self):
        ''' Devuelve True si la cola esta vacía, False si no. '''
        return self.lista_cola == []
    
    def mostrar(self):        
        print(self.lista_cola)
     
    def largo(self):
        return len(self.lista_cola) 


#Fin de TDA Cola

#Inicio de TDA Lista Ordenada

class NodoLo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaOrdenada:

    def __init__(self):
        self.cabeza = None
    
    def estaVacia(self):
        return self.cabeza == None

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()        
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()

        return encontrado

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()

        temp = NodoLo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)

    def ver(self):        
        print("[",end="")
        if self.estaVacia:            
            actual = self.cabeza
            while actual != None:
                 print(actual.dato,end="")
                 actual = actual.obtenerSiguiente()
                 if actual != None:
                    print(end=',')
            print("]")
        else:
            print('[]')
        return

#Modulo Nuevo
    def metodo_nuevo(self,x):
        actual = self.cabeza
        contador = 0
        while actual != None:
            if contador == x:
                return actual.dato
            contador += 1
            actual = actual.obtenerSiguiente()            
            
        return None
    
# Se quita para el parcial   lo tienen que hacer los alumnos
    def clear(self):
        self.cabeza = None

    def remover_x_indice(self,indice):
        actual = self.cabeza
        previo = None
        encontrado = False
        contador = 0
        while not encontrado and actual != None:            
            if contador == indice:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
            contador += 1
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:                
                previo.asignarSiguiente(actual.obtenerSiguiente())
                return actual.dato
                
#segunda solucion de remover x indice
    def remover_rapido(self,indice):
        eliminado = self.metodo_nuevo(indice)
        self.remover(eliminado)
        return eliminado

import random as r
class Fabrica_de_numeros:
    def __init__(self, min: int, max:int):
        self.min = min
        if min > max: raise Exception("che el minimo no puede ser mayor que el maximo")
        self.max = max

        self.contenedor1 = []
        self.__cargar_contenedor(self.contenedor1)

        self.contenedor2 = []
        self.__cargar_contenedor(self.contenedor2)

        self.contenedor3 = []
        self.__cargar_contenedor(self.contenedor3)

        self.mostrar_contenedores()

        self.contenedor_apilamiento = Pila()
        self.__apilar_numeros(self.contenedor_apilamiento)

        self.numeros_ordenados = ListaOrdenada()
        self.__ordenar_numeros(self.numeros_ordenados)

    def __cargar_contenedor(self,contenedor: list) -> None:
        for n in range(10):
            contenedor.append(r.randint(self.min,self.max))
    
    def mostrar_contenedores(self):
        contenedores = [self.contenedor1,self.contenedor2,self.contenedor3]
        for i,c in enumerate(contenedores): 
            print("contenedor nro "+str(i+1))
            print(c)
    
    def __apilar_numeros(self,contenedor_pila: Pila) -> None:
        for x in range(10):
            contenedor_pila.apilar(self.contenedor1[x])
            contenedor_pila.apilar(self.contenedor2[x])
            contenedor_pila.apilar(self.contenedor3[x])
    
    def mostrar_pila(self):
        print("contenedor apilados")
        self.contenedor_apilamiento.mostrar()

    def __desapilar_numeros(self,contenedor_pila: Pila) -> list:
        numeros_desapilados = []

        while not contenedor_pila.vacia():
            numeros_desapilados.append(contenedor_pila.desapilar())

        return numeros_desapilados
    
    def __numeros_encolados(self) -> Cola:
        cola = Cola()
        for i in self.__desapilar_numeros(self.contenedor_apilamiento):
            cola.encolar(i)
        return cola
    
    def __ordenar_numeros(self,listaOrdenada: ListaOrdenada) -> None:
        cola = self.__numeros_encolados()
        while not cola.es_vacia():
            listaOrdenada.agregar(cola.desencolar())

    def ver_numeros_ordenadas(self):
        print("ordenando numeros generados por la fabrica: ")
        self.numeros_ordenados.ver()

fabrica = Fabrica_de_numeros(0,9)
fabrica.mostrar_pila()
fabrica.ver_numeros_ordenadas()