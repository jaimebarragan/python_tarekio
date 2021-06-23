import os
import time
import random 

#El programa debe permitir cambiar la contraseña almacenada internamente con las siguientes reglas:
#Se debe verificar la contraseña anterior.
#en caso de error mostrar mensaje y salir del programa.
#La nueva contraseña no pede ser igual a la anterior.
#?Se debe pedir una confirmación de la nueva contraseña (debe escribirse dos veces
#En caso de fallar alguna de éstas verificaciones deberá mostrarse un error y volver al menú ppal (lista)
#En caso de éxito deberá volverse al menú  ppal (el que tiene la lista)

#En la opción 2 el programa hará lo siguiente:
#Si es la primera vez que se ingresa a la opción
#Deberá permitir ingresar 3 pares de coordenadas (latitud, longitud)
#Los datos ingresados deberán ser decimales separados con un . y tener 3 cifras.
#La latitud deberá estar entre los siguientes rangos 10.103 y 10.362
#La longitud deberá estar entre los siguientes rangos -75.088 y -74.918
#Se deberá verificar cada número ingresado y que éste esté dentro del rango permitido.
#En caso de no ser así, deberá mostrarse un error personalizado y regresar al menú de la lista
#Debe verificarse que la coordenada ingresada no esté en blanco, en caso de ser así; deberá repetirse la pregunta
#para esa pregunta en especific.
#Si todos los datos son correctos se guardarán en parejas en una matriz de 3 x 2.

#Si es la segunda vez que ingresa:
#Se mostrarán las coordenadas guardadas y se mostrará.
#La coordenada más al sur.
#La coordenada más al occidente
#El promedio de las latitudes.
#se le preguntará al usuario la opción que desea actualizar
#Si elige una opción inválida se mostrará un error y se regresará al menú de la lista.
#Los datos ingresados deberán cumplir las mismas reglas anteriores.
#Una vez ingresados los datos; deberá guardarse esa nueva información en la posición de la lista correspondiente.

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
ClaveGuardada="123"
captcha1=123
captcha2=int((2*2)+(2**2)/(2+2)-1)
captcha=captcha1-captcha2 
#endregion



def ImprimirLista(): 
    for x in range(len(listamenu)):
        print(f"{x+1} - {listamenu[x]}")

def ValidacionDatos(dato1,dato2):
    if dato1 == dato2:
        return True 
    else:
        return False 

def ReordenarFav(posicion): 
    mover=listamenu[posicion-1]
    listamenu.remove(mover)
    listamenu.insert(0,mover)

def ErrorConMensaje(mensaje):
    os.system("cls")
    print(mensaje)
    time.sleep(2)

#Declaramos la función para cambiar la clave
def CambiarClave(claveactual): #toma como parámetro la clave actual (desde donde se llama la función.)
    #A través de la función confirmamos que la clave ingrsada sea igual a la guardada
    if ValidacionDatos(input("Por favor ingrese su contraseña actual: "), claveactual):
        nuevaclave=input("Por favor ingrese su nueva contraseña: ") #solicitamos la clave nueva
        if ValidacionDatos(nuevaclave,claveactual):#verificamos que las contraseñas nueva y guardada sean diferentes
            ErrorConMensaje("La nueva contraseña no puede ser igual a la anterior.")
            return claveactual
        else:
         #solicitamos la confirmación de la nueva contraseña
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nuevaclave):
                return nuevaclave
                
            else: #mostramos los mensajes de error
                ErrorConMensaje("Las contraseñas no coinciden")
                return claveactual
    else:
        ErrorConMensaje("La contraseña es incorrecta")
        exit()
        

print("Bienvenido a la práctica de Python")
UsuarioIngresado=input("Ingrese su usuario: ")
if ValidacionDatos(UsuarioGuardado,UsuarioIngresado): 
    if ValidacionDatos(input("Ingrese su contraseña: "), ClaveGuardada): 
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} - {captcha2}: "))
        if ValidacionDatos(captcha,verificacion): 
            os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)
            while contadorerrores<5:
                os.system("cls")
                ImprimirLista()
                opcionelegida=int(input("Por favor selecciona una opción: ")) 

                if opcionelegida > 0 and opcionelegida < 8:
                    opcionelegidalista=listamenu[opcionelegida-1] 
                    
                    if opcionelegidalista==opc1:
                        print(opc1)
                        ClaveGuardada=CambiarClave(ClaveGuardada) #llamamos la función
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
                                    ReordenarFav(nuevofavorito)
                                
                                else:
                                    ErrorConMensaje("Error comprobación 2") 
                            else:
                                ErrorConMensaje("Error comprobación 1")
                        else:
                            ErrorConMensaje("Opción Inválida")
                            continue 
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
