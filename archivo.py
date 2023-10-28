from datetime import *


class Archivo:
    def __init__(self, nombre: str, fecha: date, formato: str) -> None:
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato
    
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    @property
    def formato(self):
        return self.__fecha
    
    @formato.setter
    def formato(self, nuevo_formato):
        self.__formato = nuevo_formato
    
    def __str__(self) -> str:
        return f'Nombre de archivo: {self.nombre}, fecha de creacion: {self.fecha}, formato: {self.fecha}'