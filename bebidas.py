from abc import ABC, abstractmethod

class Bebidas(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def descripcion(self):
        pass

class Cerveza(Bebidas):
    def __init__(self, nombre, precio, tipo_cerveza):
        super().__init__(nombre, precio)
        self.tipo_cerveza = tipo_cerveza

    def descripcion(self):
        return f"La cerveza {self.nombre} es del tipo {self.tipo_cerveza}. Su precio es {self.precio}."

class Refresco(Bebidas):
    def __init__(self, nombre, precio, sabor):
        super().__init__(nombre, precio)
        self.sabor = sabor

    def descripcion(self):
        return f"El refresco {self.nombre} es de sabor {self.sabor}. Su precio es {self.precio}."

class Te(Bebidas):
    def __init__(self, nombre, precio, variedad):
        super().__init__(nombre, precio)
        self.variedad = variedad

    def descripcion(self):
        return f"El té {self.nombre} es de la variedad {self.variedad}. Su precio es {self.precio}."