from usuario import *
from curso import *

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, mail: str, password: str, titulo: str, anio_egreso: int) -> None:
        super().__init__(nombre, apellido, mail, password)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        Usuario.usuarios_registrados.append({"mail": self.mail, "password": self.password, "tipo": "profesor"})
        self.__mi_cursos = []

    @property
    def mi_cursos(self):
        return self.__mi_cursos

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        self.__titulo = nuevo_titulo

    @property
    def anio_egreso(self) -> int:
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, nuevo_anio_egreso: int):
        self.__anio_egreso = nuevo_anio_egreso

    def __str__(self) -> str:
        return f"Profesor: {self.nombre} {self.apellido}, Título: {self.titulo}, Año de egreso: {self.anio_egreso}"

    def dictar_curso(self, curso: Curso) -> None:
        print(f"El profesor {self.nombre} está dictando el curso: {curso.nombre}")
   
    
# Crear instancias de profesores
profesor1 = Profesor("Pedro", "Lopez", "pedro@g.com", "pedro123", "Doctor", 2008)
profesor2 = Profesor("Mercedez", "Viloni", "mercedes@g.com", "mer123", "Ingeniera", 2012)
profesor3 = Profesor("Tomas", "Sánchez", "tomas@g.com", "tomas123", "Licenciado", 2015)

# Crear la lista de profesores
lista_profesores = [profesor1, profesor2, profesor3]