#Funcion que imprima lista
#Función que valide datos
#función que reordene el favorito
#función de error con mensaje personalizado

import os
import time
import random 

#Las regiones nos permiten colapsar ciertas partes del código

#region VARIABLES GLOBALES
opc1="Cambiar contraseña"
opc2="Ingresar restaurantes del sector"
opc3="Ubicar restaurantes más cercanos"
opc4="Actualizar restaurantes cercanos"
opc5="Guardar archivo con restaurantes cercanos"
opc6="Elegir opción favorita"
opc7="Cerrar sesión"
listamenu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]
contadorerrores=0
UsuarioGuardado="usuario"
ClaveGuardada=123
captcha1=123
captcha2=int((2*2)+(2**2)/(2+2)-1)
captcha=captcha1-captcha2 
#endregion

def ImprimirLista(): #Nos permite imprimir la lista
    for x in range(len(listamenu)):
        print(f"{x+1} - {listamenu[x]}")

def ValidacionDatos(dato1,dato2):#Toma como entrada dos parámetros a comparar, ej: UsuarioGuardado,UsuarioIngresado
    if dato1 == dato2:
        return True #Verdadero si son iguales
    else:
        return False #falso si son diferentes

def ReordenarFav(posicion): #Toma como entrada un parámetro que se usa para crear la variable mover
    mover=listamenu[posicion-1]
    listamenu.remove(mover)
    listamenu.insert(0,mover)

def ErrorConMensaje(mensaje):#Toma como entrada un mensaje personalizado que se imprimirá en pantalla
    os.system("cls")
    print(mensaje)
    time.sleep(2)

print("Bienvenido a la práctica de Python")
UsuarioIngresado=input("Ingrese su usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): #Se llama la función desde un condicinal por eso los dos puntos 
    if ValidacionDatos(int(input("Ingrese su contraseña: ")), ClaveGuardada): #El primer parámetro para la función, se toma desde un input
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} - {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<5:
                os.system("cls")
                ImprimirLista() #Llamamos a la función que nos imprime la lista
                opcionelegida=int(input("Por favor selecciona una opción: ")) 
                #Recordar que ésta condición evita un error que corregí en el video
                #Debe revisarse si el número elegido está dentro del rango
                #Para evitar que sea buscado en la lista una posición que no existe.
                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegidalista=listamenu[opcionelegida-1] 
                    
                    if opcionelegidalista==opc1:
                        print(opc1) 
                        time.sleep(2)
                    elif opcionelegidalista==opc2:
                        print(opc2)
                        time.sleep(2)
                    elif opcionelegidalista==opc3:
                        print(opc3)
                        time.sleep(2)
                    elif opcionelegidalista==opc4:
                        print(opc4)
                        time.sleep(2)
                    elif opcionelegidalista==opc5:
                        print(opc5)
                        time.sleep(2)
                    elif opcionelegidalista==opc6:
                        print(opc6)
                        nuevofavorito=int(input("Ingrese el número de la opción que desea mover: ")) 
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5: 
                            numerorndm=random.randint(0,10000)
                            if int(input(f"Por favor escriba el siguiente número: {numerorndm}:")) == numerorndm:
                                if int(input("Por favor resuelva la siguiente suma 9 + 9:"))==18:
                                    ReordenarFav(nuevofavorito)#Se llama la función reordenar fav, el parámetro es en número ingresado por el usuario
                                
                                else:
                                    ErrorConMensaje("Error comprobación 2") #Se llama la función de error con mensaje, y se manda el error a mostrar.
                            else:
                                ErrorConMensaje("Error comprobación 1")
                        else:
                            ErrorConMensaje("Opción Inválida")
                            continue #Recordar que continues, breaks y exit no están dentro de la función.
                    elif opcionelegidalista==opc7:
                        ErrorConMensaje("Sesión cerrada")
                        exit()
                else:
                    contadorerrores+=1 
                    ErrorConMensaje("Opción no válida")
                    continue    
    
        else:
            ErrorConMensaje("Error captcha incorrecto")
    else:
        ErrorConMensaje("Error contraseña incorrecta")
else:
    ErrorConMensaje("Error usuario incorrecto")
