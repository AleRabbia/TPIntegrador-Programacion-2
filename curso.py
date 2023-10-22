from usuario import *
class Curso:
    def __init__(self, nombre:str, contrasenia_matriculacion:str) -> None:
        self.__nombre = nombre
        self.__contrasenia_matriculacion = contrasenia_matriculacion

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
    
# Crear instancias de cursos
curso1 = Curso("Programacion 2", "P22023")
curso2 = Curso("Laboratorio de Computacion 2", "LC22023")
curso3 = Curso("Metodologia de la Investigacion", "MI2023")

# Crear la lista de cursos
lista_cursos = [curso1, curso2, curso3]