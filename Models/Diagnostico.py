class Diagnostico:
    def __init__(self, nro: int, tipo: str, descripcion: str, estado: int = 0):
        self.nro = nro
        self.tipo = tipo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"{self.nro},{self.tipo},{self.descripcion},{self.estado}"

    def __repr__(self):
        return f"{self.__str__()}"

    def dar_alta(self):
        self.estado = 1

    def dar_baja(self):
        self.estado = 0

    def modificar_datos(self, posicion, dato):
        if posicion == "1":
            self.nro = dato
        elif posicion == "2":
            self.tipo = dato
        elif posicion == "3":
            self.descripcion = dato
