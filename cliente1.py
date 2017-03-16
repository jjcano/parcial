#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import funciones
import json
ruta_s= socket.socket()
#coneccion con el servidor
ruta_s.connect(("localhost",35000))

men=0
datos_usuario=[]
datos_oper=[]

login=''

while True:
    cadena_oper = ''
    datos_oper=[]

    if login=='':
        datos=''
        cadena_envio=''
        cadena_oper=''
        usuario = raw_input("ingrese usuario ")
        datos_usuario.append(usuario)
        password = raw_input("ingrese Contraseña ")
        datos_usuario.append(password)
        cadena_envio = json.dumps(datos_usuario)
        ruta_s.send(cadena_envio)
        datos_usuario=[]
        datos = ruta_s.recv(1000)

        if datos == 'true' and usuario == 'admin':
            print "Bienvenido al Sistema Administrador\n"
            login = 'true'
            datosok=funciones.menu()
            listamenu=funciones.menu_lista(datosok)

            opt = raw_input("Seleccione una opción ")
            datos_oper.append(opt)

            if opt == 'a':
                nombre = raw_input("ingrese nombre de la pelicula ")
                datos_oper.append(nombre)
                costo = raw_input("ingrese costo ")
                datos_oper.append(costo)
                sillas = raw_input("Numero de sillas ")
                datos_oper.append(sillas)
                hora = raw_input("ingrese hora ")
                datos_oper.append(hora)
                id = raw_input("ingrese id ")
                datos_oper.append(id)
                #cadena_oper = json.dumps(datos_oper)
                #ruta_s.send(cadena_oper)
            if opt == 'c':
                nombre = raw_input("De Clic Para Listar ")
                datos_oper.append(nombre)

            cadena_oper=json.dumps(datos_oper)
            ruta_s.send(cadena_oper)

        elif datos == 'true' and usuario == 'cliente':
            login='true'
            datosok = funciones.cliente()
            listamenu = funciones.menu_cliente(datosok)
            opt = raw_input("Seleccione una opción ")
            datos_oper.append(opt)
        else:
            login=''
            print "Datos Incorrecto"
            break
    else:
        datosok = funciones.menu()
        listamenu = funciones.menu_lista(datosok)

        opt = raw_input("Seleccione una opción ")
        datos_oper.append(opt)

        cadena_oper = json.dumps(datos_oper)
        ruta_s.send(cadena_oper)


    #verificar mensaje para salir
    #if usuario == 'salir':
     #   break
#print "Vuelva cuando quiera"
#cerrar conexion con el servidor
ruta_s.close()