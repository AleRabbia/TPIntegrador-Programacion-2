from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nombre: str, apellido: str, mail: str,password: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__password = password

    @property
    def nombre(self) -> str:
        return self.__nombre.title()

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre.title()

    @property
    def apellido(self) -> str:
        return self.__apellido.title()

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self.__apellido = nuevo_apellido.title()

    @property
    def mail(self) -> str:
        return self.__mail


    @mail.setter
    def mail(self, nuevo_mail: str):
        self.__mail = nuevo_mail

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, nuevo_password: str):
        self.__password = nuevo_password

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
    
    usuarios_registrados = []
    
    @staticmethod
    def validar_credenciales(mail: str, password: str) -> bool:
        for usuario in Usuario.usuarios_registrados:
            #print(Usuario.usuarios_registrados)
            if usuario["mail"] == mail and usuario["password"] == password:
                return True
        return False