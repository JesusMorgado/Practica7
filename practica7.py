'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
'''
import json
import random

import bcrypt

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes. (5) 10 min.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }

4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]
'''
'''
def M():
    archivo = open("Kardex.txt", "r")       # Abrir el archivo de kardes para sacar las materias
    mate = set()
    for linea in archivo:
        d = linea.split("|")
        datos = int(str(d[2]))
        mate.add((linea[0:8], d[1], datos))    # Agregamos a conjunto la linea del caracter 0 al 8
    archivo.close()
    return mate

def regresa_materia_por_estudiantes(ctr):
    promedios = M()
    lista_materias = []
    for mat in promedios:
       c,m,p = mat
       if ctr == c:
           lista_materias.append({"Nombre":m})
    return json.dumps(lista_materias)

print(regresa_materia_por_estudiantes("18420469"))
'''

'''
5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4
    
   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada
'''
'''

def generar_letra_mayuscula():
    return chr(random.randint(65,98))

def generar_letra_minuscula():
    return chr(random.randint(97,122))

def generar_numeros():
    return chr(random.randint(48,57))

def generr_caracter_especial():
    lista_caracteres = ["@","#","$","%","&","_","?","!"]
    return lista_caracteres[random.randint(0,7)]

def generar_contraseña():
    clave = ""
    for i in range(0,10):
        numero = random.randint(1, 5)

        if numero == 1:
            clave = clave + generar_letra_mayuscula()
        elif numero == 2:
            clave = clave + generar_letra_minuscula()
        elif numero == 3:
            clave = clave + generr_caracter_especial()
        elif numero >= 4 and numero <= 5:
            clave = clave + generar_numeros()

    # Regresar contraseña

    return clave

#print(generar_contraseña())

# Cifrar las contraseñas con bcrypt

def cifrar_contra(contrasena):
    sal = bcrypt.gensalt()
    contra_cifra = bcrypt.hashpw(contrasena.encode(),sal)
    return contra_cifra

#clave = generar_contraseña()
#print(clave,cifrar_contra(clave))


# Generar el archivo de usuario
def E():
    archivo = open("Estudiantes.prn", "r")  # Abrir el archivo de estudiantes
    c = set()                        # Creacion de conjunto
    for linea in archivo:                   # Recorrer el archivo
        c.add((linea[0:8], linea[8:-1]))   # Agregamos al conjunto las lineas del caracter 0 al 8

    return c



def generar_archivo_estudiantes():

    #Obtener la lista de los estudiantes

    estudiantes = list(E())
    archivo = open("usuarios.txt", "w")
    contador = 1
    for est in estudiantes:
        c,n = est
        clave = generar_contraseña()
        clave_cifrada = cifrar_contra(clave)
        registro = c + " " + clave + " " + str(clave_cifrada,"utf-8") + " \n"
        archivo.write(registro)
        contador += 1
        print(contador)
        print("Arcivo Generado")

generar_archivo_estudiantes()


'''


'''
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''

# Jesus Morgado Marquez
# 08/09/2022
# Practica 7
def E():
    archivo = open("Estudiantes.prn", "r")  # Abrir el archivo de estudiantes
    c = set()                        # Creacion de conjunto
    for linea in archivo:                   # Recorrer el archivo
        c.add((linea[0:8], linea[8:-1]))   # Agregamos al conjunto las lineas del caracter 0 al 8

    return c

def validar():
    archivo = open("usuarios.txt","r")
    lista = []
    clave = ""
    usuario = ""
    b = False
    msj = ""
    dicc = {}
    usuario = input("Usuario: ")
    clave = input("Contraseña:  ")
    estudiantes = list(E())
    aux = ""
    for est in estudiantes:
        c, n = est
        if c == usuario:
            aux = n
            break
    for linea in archivo:
        lista = linea.split(" ")
        lista.append(linea[:-1])


        if usuario == lista[0]:

            msj = "Ingresado Correctamente"

            if bcrypt.checkpw(clave.encode("utf-8"), lista[2].encode("utf-8")):
                b = True
                msj = "Bienvenido al Sistema de Autenticación de usuarios"
            else:
                b = False
                msj = "Contraseña incorrecta"

            break
        else:

            msj = "El Ususrio no Exsiste"






    dicc["Bandera"] = b
    dicc["Usuario"] = aux
    dicc["Mensaje"] = msj


    return json.dumps(dicc,indent=3)



print(validar())




