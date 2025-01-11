import tdarecuperatorio as tda
import random as r
import copy

class Cola_aux(tda.Cola):
    def desencolar(self):
        ''' Elimina el primer elemento de la cola y devuelve su
        valor.'''

        if not self.es_vacia():
            return self.lista_cola.pop(0)

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

        self.contenedor_apilamiento = tda.Pila()
        self.__apilar_numeros(self.contenedor_apilamiento)

        self.numeros_ordenados = tda.ListaOrdenada()
        self.__ordenar_numeros(self.numeros_ordenados)

    def __cargar_contenedor(self,contenedor: list) -> None:
        for n in range(10):
            contenedor.append(r.randint(self.min,self.max))
    
    def mostrar_contenedores(self):
        contenedores = [self.contenedor1,self.contenedor2,self.contenedor3]
        for i,c in enumerate(contenedores): 
            print("contenedor nro "+str(i+1))
            print(c)
    
    def __apilar_numeros(self,contenedor_pila: tda.Pila) -> None:
        for x in range(10):
            contenedor_pila.apilar(self.contenedor1[x])
            contenedor_pila.apilar(self.contenedor2[x])
            contenedor_pila.apilar(self.contenedor3[x])
    
    def mostrar_pila(self):
        print("contenedor apilados")
        self.contenedor_apilamiento.mostrar()

    def __desapilar_numeros(self,contenedor_pila: tda.Pila) -> list:
        contenedor_copia = copy.deepcopy(contenedor_pila)
        numeros_desapilados = []

        while not contenedor_copia.vacia():
            numeros_desapilados.append(contenedor_copia.desapilar())

        return numeros_desapilados
    
    def __numeros_encolados(self) -> Cola_aux:
        cola = Cola_aux()
        for i in self.__desapilar_numeros(self.contenedor_apilamiento):
            cola.encolar(i)
        return cola
    
    def __ordenar_numeros(self,listaOrdenada: tda.ListaOrdenada) -> None:
        cola = self.__numeros_encolados()
        while not cola.es_vacia():
            listaOrdenada.agregar(cola.desencolar())

    def ver_numeros_ordenadas(self):
        print("ordenando numeros generados por la fabrica: ")
        self.numeros_ordenados.ver()

fabrica = Fabrica_de_numeros(0,9)
fabrica.mostrar_pila()
fabrica.ver_numeros_ordenadas()