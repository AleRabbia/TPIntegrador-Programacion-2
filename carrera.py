
class Carrera:
    def __init__(self, nombre: str, cant_anios: int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        #self.__cursos_carrera = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def cant_anios(self):
        return self.__cant_anios
    
    @cant_anios.setter
    def cant_anios(self, nueva_cantidad):
        self.__cant_anios = nueva_cantidad
    
    def __str__(self) -> str:
        return f'Nombre de carrera: {self.carrera}, cantidad de años: {self.cant_anios}'
    
    #def get_cantidad_materias(self):
    #    return len(self.__cursos_carrera)  NO SE SI SERÍA ASÍ LA FORMA DE HACERLO