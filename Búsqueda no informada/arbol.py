# Esta clase es una sencilla implementación de la estructura de datos árbol
class Nodo:

    # El constructor acepta como primer parámetro un dato que será almacenado en el
    # nodo (en principio de cualquier tipo). Opcionalmente acepta un segundo
    # parámetro con una lista de hijos.
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.costo= None
        self.set_hijos(hijos)
    
    # Asigna al nodo la lista de hijos que son pasados como parámetro.
    def set_hijos(self, hijos):
        self.hijos=hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self
    # Retorna una lista con los hijos del nodo.
    def get_hijos(self):
        return self.hijos
    
    # Retorna el nodo padre.
    def get_padre(self):
        return self.padre

    # Asigna el nodo padre de este nodo.
    def set_padre(self, padre):
        self.padre = padre

    # Asigna un dato al nodo.
    def set_datos(self, datos):
        self.datos = datos

    # Devuelve el dato almacenado en el nodo.
    def get_datos(self):
       return self.datos
    
    # Asigna un costo al nodo dentro del árbol.
    def set_costo(self, costo):
        self.costo = costo

    # Devuelve el costo del nodo dentro del árbol.
    def get_costo(self):
        return self.costo

    # Devuelve True si el dato contenido en el nodo es igual al nodo 
    # pasado como parámetro.
    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    # Devuelve True si el dato contenido en el nodo es igual a alguno 
    # de los nodos contenidos en la lista de nodos pasada como parámetro.
    def en_lista(self, lista_nodos):
        en_la_lista=False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista=True
        return en_la_lista
    
    def __str__(self):
        return str(self.get_datos())