from usuario import *
from curso import *
import datetime 

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, legajo: int, anio_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, mail, password)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        Usuario.usuarios_registrados.append({"mail": self.mail, "password": self.password, "tipo": "estudiante"})
        self.__mi_cursos = []


    @property
    def legajo(self) -> str:
        return self.__legajo

    @legajo.setter
    def legajo(self, nuevo_legajo: str):
        self.__legajo = nuevo_legajo

    @property
    def mi_cursos(self):
        return self.__mi_cursos

    @property
    def anio_inscripcion_carrera(self) -> int:
        return self.__anio_inscripcion_carrera

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion: int):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion

    def __str__(self) -> str:
        return f"Alumno: {self.nombre} {self.apellido}, Legajo: {self.legajo}, Año de inscripcion: {self.anio_inscripcion_carrera}"

    def matricularse_al_curso(self, curso: Curso, contrasenia: str) -> bool:

        if contrasenia == curso.contrasenia_matriculacion:
                if curso not in self.__mi_cursos:
                    self.__mi_cursos.append(curso)
                    mensaje = f"Matriculado con éxito en el curso {curso.nombre}!"                    
                else:
                    mensaje = f"Ya estás matriculado en el curso {curso.nombre}."                    
        else:
            mensaje ="Contraseña incorrecta. Matriculación fallida."
        return mensaje
    

        
# Crear instancias de estudiantes
estudiante1 = Estudiante("Ale", "Rabbia", "ale@g.com", "1234", 1001, 2020)
estudiante2 = Estudiante("Marcelo", "Cepeda", "marce@g.com", "abc123", 1002, 2019)
estudiante3 = Estudiante("Matias", "Volpe", "mvolpe@g.com", "qwerty", 1003, 2021)

# Crear la lista de estudiantes
lista_estudiantes = [estudiante1, estudiante2, estudiante3]