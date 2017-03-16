import json
import os

def usuarios():
    lista=['admin','cliente']
    cadena=json.dumps(lista)
    return cadena

def menu():
    lista=['a. Crear Peliculas','b. Eliminar Peliculas','c. Listar Peliculas','d. Ver Peliculas Vendidas','e. Sillas Disponibles']
    cadena=json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def cliente():
    lista = ['a. Listar Peliculas', 'b. Comprar Entrada', 'c. Ver Mi Pelicula']
    cadena = json.dumps(lista)
    return cadena

def menu_cliente(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def crear_pelicula(nombre,costo,silla,hora,id):

    creartxt()
    archivo = open("datos.txt",'a')
    archivo.write("Pelicula: " + nombre + '\n')
    archivo.write("Costo: " + costo + '\n')
    archivo.write("silla: " + silla + '\n')
    archivo.write("Hora: " + hora + '\n')
    archivo.write("ID: " + id + '\n')
    archivo.close()

def creartxt():
    archivo = open('datos.txt', 'w')
    archivo.close()

def listar_pelicula():
    path = "C:\Users\JJ\Desktop\parcial"
    mitexto = os.listdir(path)
    archivos = []
    for ruta in mitexto:
        (nombreFichero, extension) = os.path.splitext(ruta)
        if(extension == ".txt"):
            archivos.append(nombreFichero+extension)
    #archivos.append("Presione Enter para continuar")
    cadena = json.dumps(archivos)

    return cadena