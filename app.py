from curso import *
from estudiante import *
from profesor import *
import msvcrt
import os
import getpass
import re

menucito = '''
\n *** Menu Principal ***
1 - Ingresar como alumno
2 - Ingresar como profesor
3 - Informes
4 - Salir
'''
def menu_principal():
    os.system ("cls")
    while True:
        print(menucito)
        
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            email = input("Ingrese su email: ")  
            if email and validar_email(email):
                ingresar_como_alumno(email)
            else:
                print("Correo inválido. Por favor, ingrese un correo válido.")
        elif opcion == "2":
            email = input("Ingrese su email: ") 
            if email and validar_email(email):           
                ingresar_como_profesor(email)
            else:
                print("Correo inválido. Por favor, ingrese un correo válido.")
        elif opcion == "3":
            informes()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            pause()
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            pause()


def menu_alumno(estudiante):
    os.system ("cls")
    while True:
        print(f"\n*** Menú Alumno - Bienvenido {estudiante.nombre} {estudiante.apellido} ***")
        print("1 - Matricularse a un curso")
        print("2 - Ver cursos matriculados")
        print("3 - Desmatricularse de un curso")
        print("4 - Perfil del alumno")
        print("5 - Editar mis datos")
        print("6 - Volver al menú principal")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            matricularse_a_curso(estudiante)
        elif opcion == "2":
            ver_cursos_matriculados(estudiante)
        elif opcion == "3":
            desmatricularse_a_curso(estudiante)
        elif opcion == "4":
            resumen = estudiante.resumen_alumno()
            print(resumen)
        elif opcion == "5":
            editar_usuario(estudiante)
        elif opcion == "6":
            print("Volviendo al menú principal.")
            pause()
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            pause()

def menu_profesor(profesor):
    os.system ("cls")
    while True:
        print(f"\n*** Menú Profesor - Bienvenido {profesor.nombre} {profesor.apellido} ***")
        print("1 - Dictar curso")
        print("2 - Ver cursos dictados")
        print("3 - Ver perfil profesor")
        print("4 - Editar mis datos")
        print("5 - Volver al menú principal")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            dictar_curso(profesor)
        elif opcion == "2":
            ver_cursos_dictados(profesor)
        elif opcion == "3":
            resumen = profesor.resumen_profesor()
            print(resumen)
        elif opcion == "4":
            editar_usuario(profesor)
        elif opcion == "5":
            print("Volviendo al menú principal.")
            pause()
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            pause()



def informes():
    os.system ("cls")
    while True:
        print("\n*** Informes ***")
        print("1 - Listado de cursos")
        print("2 - Listado de alumnos")
        print("3 - Listado de profesores")
        print("4 - Volver")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            ver_cursos(lista_cursos)
        elif opcion == "2":
            ver_alumnos()
        elif opcion == "3":
            ver_profesores()
        elif opcion == "4":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

#funcion para ingresar como alumno, pide mail, si no existe permite dar de alta un nuevo alumno
def ingresar_como_alumno(email): 
    os.system ("cls")
    for estudiante in lista_estudiantes:
        if estudiante.mail == email:
            password = getpass.getpass("Ingrese su contraseña: ")
            if Usuario.validar_credenciales(email, password):
                menu_alumno(estudiante)
                return
            else:
                print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
                return
    confirmacion = input("No se encontró un estudiante con ese email. ¿Desea darlo de alta? (si/no): ").lower()
    if confirmacion == "si":
        alta_alumno(email)
    else:
        print("Operacion cancelada.")

def ver_cursos_matriculados(estudiante):
    os.system ("cls")
    if not estudiante.mi_cursos:
        print("No estás matriculado en ningún curso aún.")
        pause()
        menu_alumno(estudiante)
        
    else:
        print("\n*** Cursos Matriculados ***")
        for i, curso in enumerate(estudiante.mi_cursos, start=1):
            print(f"{i}. {curso.nombre}")
        pause()
        return

def matricularse_a_curso(estudiante):
    os.system ("cls")
    lista_cursos_ordenados = sorted(lista_cursos, key=lambda cursos: cursos.nombre)
    ver_cursos(lista_cursos)
    #ver_cursos()
    opcion = input("Seleccione el número del curso al que desea matricularse: ")
    if opcion.isdigit():
        curso_index = int(opcion) - 1
        if 0 <= curso_index < len(lista_cursos_ordenados):
            curso = lista_cursos_ordenados[curso_index]
            contrasenia = input(f"Ingrese la contraseña de matriculación para el curso {curso.nombre}: ")
            mensaje = estudiante.matricularse_al_curso(curso, contrasenia)  #          
            print(mensaje)       
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

def desmatricularse_a_curso(estudiante):
    os.system("cls")
    lista_cursos_ordenados = sorted(lista_cursos, key=lambda cursos: cursos.nombre)
    ver_cursos(lista_cursos)
    opcion = input("Seleccione el número del curso al que desea matricularse: ")
    if opcion.isdigit():
        curso_index = int(opcion) - 1
        if 0 <= curso_index < len(lista_cursos_ordenados):
            curso = lista_cursos_ordenados[curso_index]
            mensaje = estudiante.desmatricularse_al_curso(curso)
            print(mensaje)
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")


def alta_alumno(mail:str):
    os.system ("cls")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    legajo = input("Ingrese el numero de legajo: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    if not nombre or not apellido or not legajo or not password:
        print("Todos los campos deben estar completos. Operación cancelada.")
        return
    fecha_actual = datetime.datetime.now()
    fecha_inscripcion = fecha_actual.year
    confirmacion = input("¿Confirma el alta de usuario? (si/no): ").lower()
    if confirmacion == "si":
        nuevo_estudiante = Estudiante(nombre, apellido, mail, password, legajo, fecha_inscripcion)
        lista_estudiantes.append(nuevo_estudiante)
        resumen = nuevo_estudiante.resumen_alumno()
        print(resumen)
    else:
        print("Operación cancelada.")

def editar_usuario(user):
    nuevos_datos = {"nombre": user.nombre, "apellido": user.apellido}

    while True:
        print(f"\n*** Editar Datos del Usuario - {user.nombre} {user.apellido} ***")
        print("1 - Editar Nombre")
        print("2 - Editar Apellido")
        print("3 - Editar Contraseña")
        print("4 - Confirmar y Guardar Cambios")
        print("5 - Volver al menú anterior")

        opcion = input("Seleccione el número de la opción que desea realizar: ")

        if opcion == "1":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nuevos_datos["nombre"] = nuevo_nombre
        elif opcion == "2":
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            nuevos_datos["apellido"] = nuevo_apellido
        elif opcion == "3":
            cambiar_contraseña(user)
        elif opcion == "4":
            if not nuevos_datos["nombre"] or not nuevos_datos["apellido"]:
                print("Todos los campos deben estar completos. No se realizaron cambios.")
            else:
                if nuevos_datos != {"nombre": user.nombre, "apellido": user.apellido}:
                    user.nombre = nuevos_datos["nombre"]
                    user.apellido = nuevos_datos["apellido"]
                    for usuario in Usuario.usuarios_registrados:
                        if usuario["mail"] == user.mail:
                            usuario["nombre"] = nuevos_datos["nombre"]
                            usuario["apellido"] = nuevos_datos["apellido"]
                    print("Cambios guardados con éxito.")
                else:
                    print("No se realizaron cambios.")
        elif opcion == "5":
            print("Volviendo al menú anterior.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")



def cambiar_contraseña(user):
    #os.system("cls")
    
    contraseña_actual = getpass.getpass("Ingrese su contraseña actual: ")
    if contraseña_actual == user.password:
        nueva_contraseña = getpass.getpass("Ingrese la nueva contraseña: ")
        if nueva_contraseña == user.password:
            print("Debe ingresar una constraseña diferente. Operación cancelada.")
        elif nueva_contraseña:
            user.password = nueva_contraseña
            for usuario in Usuario.usuarios_registrados:
                if usuario["mail"] == user.mail:
                    usuario["password"] = nueva_contraseña
            print("Contraseña actualizada con éxito.")        
        else:
            print("La contraseña no puede ser vacía. Operación cancelada.")
    else:
        print("Contraseña incorrecta. No se realizaron cambios.")

def ingresar_como_profesor(email):
    os.system ("cls")
    for profesor in lista_profesores:
        if profesor.mail == email:
            password = getpass.getpass("Ingrese su contraseña: ")
            if Usuario.validar_credenciales(email, password):
                menu_profesor(profesor)
                return
            else:
                print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
                return
    confirmacion = input("No se encontró un profesor con ese email. ¿Desea darlo de alta en alumnado? (si/no): ").lower()
    if confirmacion == "si":
        alta_profesor(email)
    else:
        print("Operacion cancelada.")
        pause()
        return

def dictar_curso(profesor):
    os.system ("cls")
    nombre_curso = input("Ingrese el nombre del curso a dictar: ")
    contrasenia_matriculacion = Curso.generar_password(nombre_curso)
    confirmacion = input(f"Confirma el curso {nombre_curso.title()} ? (si/no): ").lower()
    if confirmacion == "si":
        curso = Curso(nombre_curso, contrasenia_matriculacion)
        lista_cursos.append(curso)
        profesor.mi_cursos.append(curso)
        print(f"¡Curso dado de alta con éxito!\nNombre: {nombre_curso.title()}\nContraseña: {contrasenia_matriculacion}")
        pause()
    else:
        print("Se canceló la operación.")

def ver_cursos_dictados(profesor):
    os.system ("cls")
    if not profesor.mi_cursos:
        print("No dictas ningún curso aún.")
        pause()
    else:
        print("\n*** Cursos Dictados ***")
        for i, curso in enumerate(profesor.mi_cursos, start=1):
            print(f"{i}. {curso.nombre}\nContraseña de Matriculación: {curso.contrasenia_matriculacion}")
        pause()


def alta_profesor(mail:str):
    os.system ("cls")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    titulo = input("Ingrese el titulo: ")
    anio_egreso = int(input("Ingrese el año de egreso: "))
    password = getpass.getpass("Ingrese la contraseña: ")
    if not nombre or not apellido or not titulo or not anio_egreso or not password:
        print("Todos los campos deben estar completos. Operación cancelada.")
        return
    confirmacion = input("¿Confirma el alta de usuario? (si/no): ").lower()
    if confirmacion == "si":
        nuevo_profe = Profesor(nombre, apellido, mail, password, titulo, anio_egreso)
        lista_profesores.append(nuevo_profe)
        resumen = nuevo_profe.resumen_profesor()
        print(resumen)
    else:
        print("Operación cancelada.")
    
 

def ver_cursos(lista_cursos):
    os.system ("cls")
    print("\n*** Cursos Disponibles ***")

    lista_cursos_ordenados = sorted(lista_cursos, key=lambda cursos: cursos.nombre)
    for i, curso in enumerate(lista_cursos_ordenados, start=1):
        print(f"{i} -", curso)
    pause()
    #return lista_cursos_ordenados

def ver_alumnos():
    os.system ("cls")
    # Ordenar la lista de estudiantes por apellido
    lista_estudiantes_ordenados = sorted(lista_estudiantes, key=lambda estudiante: estudiante.apellido)
    print("\n*** Todos los Alumnos ***")
    # Imprimir la lista ordenada
    for estudiante in lista_estudiantes_ordenados:
        print(estudiante)
    pause()

def ver_profesores():
    os.system ("cls")
    # Ordenar la lista de profesores por apellido
    lista_profesores_ordenados = sorted(lista_profesores, key=lambda profesor: profesor.apellido)
    print("\n*** Todos los Profesor ***")
    # Imprimir la lista ordenada
    for profesor in lista_profesores_ordenados:
        print(profesor)
    pause()    
        
def pause():
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch().strip()    

def validar_email(email):
    # Patrón de expresión regular para validar un correo electrónico
    patron_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(patron_email, email):
        return True
    else:
        return False

menu_principal()
