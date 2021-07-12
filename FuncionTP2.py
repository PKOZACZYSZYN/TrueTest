#Guia funcionamiento TP2: 

def listar_carpeta_actual():
    print(''' \n3.2. Listado de archivos
Se debera permitirle al usuario ver por pantalla un listado de todos los archivos que se encuentren disponibles.
3.2.1. En local
Debera mostrar los archivos que se encuentren en la carpeta principal del usuario ası como las
subcarpetas permitiendo navegar entre ellas.
3.2.2. En remoto
Debera mostrar los archivos ası como las subcarpetas que se encuentren en el Drive del usuario
permitiendo navegar entre ellas.
Documentacion sobre busqueda de archivos disponible en este link.
Documentacion sobre busqueda por campos especificaos de archivos disponible en este link. ''')

def crear_archivo():
    print(''' \n3.3. Creacion de archivos
Se debera crear una funcionalidad que permita crear un nuevo archivo entre una lista de posibles
extensiones. La creacion del archivo debe reflejarse tanto en local como en remoto.''')

def subir_archivo():
    print(''' \n3.4. Subir archivos
Debera permitir al usuario subir un archivo desde su equipo local a su Drive.
Documentacion sobre subir archivos disponible en este link. ''')

def descargar_archivo():
    print(''' \n3.5. Descargar archivos
Debera permitir al usuario descargar un archivo o carpeta desde su Drive a su equipo local.
Documentacion sobre descargar archivos disponible en este link.''')

def sincronizar():
    print(''' \n3.6. Sincronizacion
Debera permitir al usuario actualizar los archivos tanto locales como remotos a las versiones
que sufrieron la ultima modificacion. Es decir, si un archivo esta presente en local y en remoto y
tiene fechas de modificacion diferentes, el mas antiguo debe modificarse por el mas actual.''')

def generar_carpetas():
    print(''' \n3.7. Sistema de carpetas
Esta funcionalidad debera permitir crear un sistema de carpetas con 3 niveles de anidacion. El
primero sera de la evaluacion, el segundo de los docentes y el tercero de los alumnos. Con lo cual
cada evaluacion sera una carpeta que contenga diferentes carpetas de cada docente que a su vez
contendran carpetas con el nombre de los alumnos que deben corregir. El nombre de la carpeta de
evaluacion vendra dado en un asunto del mail que se recibira. Luego, los nombres de los docentes,
alumnos y relacion alumnos - docente vendran dadas en un archivo comprimido el cual contendra
3 archivos de ’.csv’, uno para cada especificacion. Si existieran docentes sin alumnos asignados o
alumnos sin docentes asignados estos igual deberan tener su carpeta correspondiente.
2
3.7.1. docentes.csv
El archivo de docentes contendra el siguiente formato de informacion:
Formato: nombre del docente, mail del docente.
3.7.2. alumnos.csv
El archivo de alumnos contendra el siguiente formato de informacion:
Formato: nombre del alumno, padron, mail
3.7.3. docente-alumnos.csv
El archivo de docente-alumnos contendra el siguiente formato de informacion:
Formato: nombre del docente, nombre del alumno
Documentacion sobre crear carpetas disponible en este link. ''')

def actualizar_entregas():
    print(''' \n3.8. Asignacion de archivos
Esta funcionalidad permitira cargar en la carpeta de cada alumno el/los archivos que este envıe
en un mail con el siguiente formato: Asunto del mail: padron Archivo adjunto: archivo comprimido
Documentacion sobre crear archivos disponible en este link.
3.9. Recepcion de entregas
Esta funcionalidad permitira enviar un mail al alumno que realizo una entrega informando
si la misma fue exitosa o si presento algun tipo de inconveniente (padron incorrecto, nombre no
coincidente con padron, etc).''')

def main():
    menu = True
    while menu == True:
        print(''' \n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
La catedra de Diego Acosta de la asignatura de Algoritmos y Programacion I ha solicitado la
creacion de un nuevo sistema para organizar la correccion de evaluaciones de la asignatura frente
a la gran cantidad de quejas presentadas por sus estudiantes con respecto a la poca organizacion
de la misma. En esta primera presentacion se ha pedido la elaboracion de un prototipo de sistema
al estilo GitHub con ciertas funcionalidades y criterios que deberemos respetar. FuncionTP2.py
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n''')
        print('''Opciones:  
\n1. Listar archivos de la carpeta actual: Debera listar todos los archivos que se encuentren en la carpeta actual y en las subcarpetas de la misma tanto a nivel local como remoto.
2. Crear un archivo: Debera permitir crear un archivo o carpeta en la carpeta actual tanto a nivel local como
remoto.
3. Subir un archivo: Debera subir un archivo que se encuentren en la carpeta local a la misma carpeta en remoto
o a otra ubicacion especificada por el usuario.
4. Descargar un archivo: Debera descargar un archivo que se encuentren en la carpeta remota a la misma carpeta en
local o a otra ubicacion especificada por el usuario.
5. Sincronizar: Debera sincronizar las carpetas y archivos conservando los ultimos que hayan sufrido modificados.
6. Generar carpetas de una evaluacion: Debera recibir vıa mail la informacion necesaria para crear las carpetas tanto en local como
en remoto.
7. Actualizar entregas de alumnos vıa mail: Debera subir los archivos que haya recibido via mail a la carpeta correspondiente del alumno.
8. Salir: Debera salir del programa.''')
        eleccion = int(input('Haga su eleccion: '))
        if eleccion == 1:
            listar_carpeta_actual()
        elif eleccion == 2:
            crear_archivo()
        elif eleccion == 3:
            subir_archivo()
        elif eleccion == 4:
            descargar_archivo()
        elif eleccion == 5:
            sincronizar()
        elif eleccion == 6:
            generar_carpetas()
        elif eleccion == 7:
            actualizar_entregas()
        else:
            menu = False

main()