from usuario import *
from archivo import Archivo

__prox_cod = 0
class Curso:
    def __init__(self, nombre:str, contrasenia_matriculacion:str, carrera: str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion
        self.__codigo = Curso.get_codigo()
        self.__cant_archivos = 0
        self.__archivos = []
        self.__carrera = carrera

    @property
    def nombre(self):
        return self.__nombre.title()
    
    @nombre.setter
    def nombre(self, nuevo_nombre:str):
        self.__nombre = nuevo_nombre.title()

    @property
    def contrasenia_matriculacion(self):
        return self.__contrasenia_matriculacion

    @contrasenia_matriculacion.setter
    def contrasenia_matriculacion(self, nueva_contrasenia_matriculacion:str):
        self.__contrasenia_matriculacion = nueva_contrasenia_matriculacion

    def __str__(self) -> str:
        return f"Curso: {self.nombre}"
    
    @staticmethod
    def generar_password(nombre) -> str:
        nombre = nombre.title().replace(" ", "")
        return nombre + "2023"
    
    @classmethod
    def get_codigo(cls):
        cls.__prox_cod += 1
        return cls.__prox_cod
    
    def nuevo_archivo(self, archivo: Archivo) -> None:
        self.__cant_archivos += 1
        self.__archivos.append(archivo)



# Crear instancias de cursos
curso1 = Curso("Programacion 2", "P22023", "Ingenieria civil")
curso2 = Curso("Laboratorio de Computacion 2", "LC22023", "Ingenieria mecánica")
curso3 = Curso("Metodologia de la Investigacion", "MI2023", "Tecnicatura Universitaria en programacion")

# Crear la lista de cursos
lista_cursos = [curso1, curso2, curso3]