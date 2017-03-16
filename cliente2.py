#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones2
import os

import json
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))
inicio=''
datos_oper=[]
cadena_oper=''
optread=''
nfile=''
while True:
 datos_oper = []
 cadena_oper = ''
 datos=''
 if inicio=='':
   datos = ruta_s.recv(1000)
   datos_oper=[]
   cadena_oper=''
   listamenu=funciones2.menu_lista(datos)
   opt=raw_input('Selecciones una opción: ')
   datos_oper.append(opt)
   if opt=='a':
        cadena_oper = json.dumps(datos_oper)
        ruta_s.send(cadena_oper)
   if (opt == 'b'):
       namefile = raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       textofile = raw_input('Ingrese el contenido del archivo\n')
       datos_oper.append(textofile)
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
   if opt == 'c':
       namefile = raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       cadena_oper = json.dumps(datos_oper)
       optread = 'true'
       nfile = namefile
       ruta_s.send(cadena_oper)

   if opt == 'n':
       datos_oper.append(opt)
       datos_oper.append(nfile)
       ncont = raw_input('Digite contenido a agregar ')
       datos_oper.append(ncont)
       optread = ''
       nfile = ''
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
   if opt == 'd':
       namefile = raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       cadena_oper = json.dumps(datos_oper)
       optread = ''
       nfile = ''
       ruta_s.send(cadena_oper)
       # verificar mensaje para salir
   if opt == 'e':
       datos_oper.append(opt)
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
       print "Vuelva cuando quiera"
       break
   inicio='true'
 else:
   # Variable para la ruta al directorio
  # datafiles = funciones2.listarfiles()
   datos_oper=[]
   datos = ruta_s.recv(1000)
   if optread =='':
    listafil = funciones2.menu_lista(datos)
    print(listafil)
    opt = raw_input('Digite una opción: ')
    datos_oper.append(opt)
   else:
    print(datos)
    opt = 'n'
   if opt=='a':
        cadena_oper = json.dumps(datos_oper)
        ruta_s.send(cadena_oper)
   if(opt=='b'):
       namefile=raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       textofile=raw_input('Ingrese el contenido del archivo\n')
       datos_oper.append(textofile)
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
   if opt == 'c':
       namefile = raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       cadena_oper = json.dumps(datos_oper)
       optread = 'true'
       nfile = namefile
       ruta_s.send(cadena_oper)

   if  opt =='n':
       datos_oper.append(opt)
       datos_oper.append(nfile)
       ncont = raw_input('Digite contenido a agregar ')
       datos_oper.append(ncont)
       optread = ''
       nfile = ''
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
   if opt == 'd':
       namefile = raw_input('ingrese nombre del archivo')
       datos_oper.append(namefile)
       cadena_oper = json.dumps(datos_oper)
       optread = ''
       nfile = ''
       ruta_s.send(cadena_oper)
       #verificar mensaje para salir
   if opt == 'e':
       datos_oper.append(opt)
       cadena_oper = json.dumps(datos_oper)
       ruta_s.send(cadena_oper)
       print "Vuelva cuando quiera"
       break

#cerrar conexion con el servidor
ruta_s.close()