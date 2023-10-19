from curso import *
from estudiante import *
from profesor import *

menucito = '''
\n *** Menu Principal ***
1 - Ingresar como alumno
2 - Ingresar como profesor
3 - Informes
4 - Salir
'''
def menu_principal():
    while True:
        print(menucito)
        
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            email = input("Ingrese su email: ")            
            ingresar_como_alumno(email)
        elif opcion == "2":
            email = input("Ingrese su email: ")            
            ingresar_como_profesor(email)
        elif opcion == "3":
            informes()
        elif opcion == "4":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def menu_alumno(estudiante):
    while True:
        print(f"\n*** Menú Alumno - Bienvenido {estudiante.nombre} {estudiante.apellido} ***")
        print("1 - Matricularse a un curso")
        print("2 - Ver cursos matriculados")
        print("3 - Volver al menú principal")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            matricularse_a_curso(estudiante)
        elif opcion == "2":
            ver_cursos_matriculados(estudiante)
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def menu_profesor(profesor):
    while True:
        print(f"\n*** Menú Profesor - Bienvenido {profesor.nombre} {profesor.apellido} ***")
        print("1 - Dictar curso")
        print("2 - Ver cursos dictados")
        print("3 - Volver al menú principal")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            dictar_curso(profesor)
        elif opcion == "2":
            ver_cursos_dictados(profesor)
        elif opcion == "3":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")



def informes():
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
    for estudiante in lista_estudiantes:
        if estudiante.mail == email:
            password = input("Ingrese su contraseña: ")
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
    if not estudiante.mi_cursos:
        print("No estás matriculado en ningún curso aún.")
    else:
        print("\n*** Cursos Matriculados ***")
        for i, curso in enumerate(estudiante.mi_cursos, start=1):
            print(f"{i}. {curso.nombre}")


def matricularse_a_curso(estudiante):
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
            #estudiante.matricularse_al_curso(curso,contrasenia)            
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

def alta_alumno(mail:str):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    legajo = input("Ingrese el numero de legajo: ")
    password = input("Ingrese la contraseña: ")
    fecha_actual = datetime.datetime.now()
    fecha_inscripcion = fecha_actual.year
    nuevo_estudiante = Estudiante(nombre, apellido, mail, password, legajo, fecha_inscripcion)
    lista_estudiantes.append(nuevo_estudiante)

def ingresar_como_profesor(email):
    for profesor in lista_profesores:
        if profesor.mail == email:
            password = input("Ingrese su contraseña: ")
            if Usuario.validar_credenciales(email, password):
                menu_profesor(profesor)
                return
            else:
                print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
                return
    confirmacion = input("No se encontró un profesor con ese email. ¿Desea darlo de alta en alumnado? (si/no): ").lower()
    if confirmacion == "si":
        profesor.alta_profesor(email)
    else:
        print("Operacion cancelada.")

def dictar_curso(profesor):
    nombre_curso = input("Ingrese el nombre del curso a dictar: ")
    contrasenia_matriculacion = Curso.generar_password(nombre_curso)
    curso = Curso(nombre_curso, contrasenia_matriculacion)
    lista_cursos.append(curso)
    profesor.mi_cursos.append(curso)
    print(f"¡Curso dado de alta con éxito!\nNombre: {nombre_curso}\nContraseña: {contrasenia_matriculacion}")

def ver_cursos_dictados(profesor):
    if not profesor.mi_cursos:
        print("No dictas ningún curso aún.")
    else:
        print("\n*** Cursos Dictados ***")
        for i, curso in enumerate(profesor.mi_cursos, start=1):
            print(f"{i}. {curso.nombre}\nContraseña de Matriculación: {curso.contrasenia_matriculacion}")

def alta_profesor(mail:str):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    titulo = input("Ingrese el titulo: ")
    password = input("Ingrese la contraseña: ")
    anio_egreso = int(input("Ingrese el año de egreso: "))
    nuevo_profe = Profesor(nombre, apellido, mail, password, titulo, anio_egreso)
    lista_profesores.append(nuevo_profe)
 

def ver_cursos(lista_cursos):
    print("\n*** Cursos Disponibles ***")

    lista_cursos_ordenados = sorted(lista_cursos, key=lambda cursos: cursos.nombre)
    for i, curso in enumerate(lista_cursos_ordenados, start=1):
        print(f"{i} -", curso)
    #return lista_cursos_ordenados

def ver_alumnos():
    # Ordenar la lista de estudiantes por apellido
    lista_estudiantes_ordenados = sorted(lista_estudiantes, key=lambda estudiante: estudiante.apellido)
    print("\n*** Todos los Alumnos ***")
    # Imprimir la lista ordenada
    for estudiante in lista_estudiantes_ordenados:
        print(estudiante)

def ver_profesores():
    # Ordenar la lista de profesores por apellido
    lista_profesores_ordenados = sorted(lista_profesores, key=lambda profesor: profesor.apellido)
    print("\n*** Todos los Profesor ***")
    # Imprimir la lista ordenada
    for profesor in lista_profesores_ordenados:
        print(profesor)

menu_principal()
