import os
import time
import random 

##########################################
#IMPORTANTE: LOS COMENTARIOS ÚNICAMENTE SON DE LO MOSTRADO EN ÉSTE VIDEO
#Para los comentarios de la parte anterior debes buscar el código correspondiente
#La razón es evitar la cantidad de lineas.
##########################################

#region ENUNCIADO
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
#para esa pregunta en especifico.
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
#endregion


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
listacoordenadas=[]
listadepuracion=[[None,None],
                 [None,None],
                 [None,None]]
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

def CambiarClave(claveactual):
    if ValidacionDatos(input("Por favor ingrese su contraseña actual: "), claveactual):
        nuevaclave=input("Por favor ingrese su nueva contraseña: ")
        if ValidacionDatos(nuevaclave,claveactual):
            ErrorConMensaje("La nueva contraseña no puede ser igual a la anterior.")
            return claveactual
        else:
            if ValidacionDatos(input("Por favor confirme su nueva contraseña: "), nuevaclave):
                return nuevaclave
                
            else:
                ErrorConMensaje("Las contraseñas no coinciden")
                return claveactual
    else:
        ErrorConMensaje("La contraseña es incorrecta")
        exit()
        
#Definimos la función para ingresar coordenadas, toma como parámetro la lista orignal (vacía)
def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)#creamos un duplicado de la lista para poder usar sus métodos
    for x in range (0,3): #creamos un for que se repetirá 3 veces
        listaduplicada.append([]) #en cada iteración agregaremos una sublista a la lista vacía.
        lat=input("Ingrese la latitud: ") #pediremos por la latitud EN TEXTO
        #Creamos un while que se ejecute mientras lat= espacio en blanco.
        while lat == "" or lat == " ": #"" = enter; " " = espacio
            lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lat=float(lat)#Una vez roto el ciclo while, convertimos la latitud a float
        if lat >= 10.103 and lat <= 10.362: #comparamos los rangos, si es válido pedimos la longitud
            lon=input("Ingrese la longitud: ") #se aplica la misma lógica que la latitud
            while lon == "" or lon == " ":
                lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
            lon=float(lon)
            if lon >= -75.088 and lon <= -74.319:
                #Si todas las verificaciones pasaron agregamos en la sublista [x]
                #en la posición 0 la latitud
                #y en la posición 1 la longitud
                listaduplicada[x].insert(0,lat) #Es importante el insert, es por que no existe ese elemento
                listaduplicada[x].insert(1,lon)
            #Mostramos la cadena de errores    
            else:
                ErrorConMensaje("Longitud fuera del rango")
                #debemos reiniciar la lista a su estado vacío para que no rompa
                #la condición que llama la función
                listaduplicada=[]
                return listaduplicada #retornamos la lista generada durante la funcion (vacía)
        else:
            ErrorConMensaje("Latitud fuera del rango")
            listaduplicada=[]
            return listaduplicada
    #Una vez terminado el for    
    return listaduplicada #retornamos la lista generada durante la funcion (llena con los 6 datos)

#creamos la función para actualizar los datos y la depuramos
def ActualizarCoordenadas(listaoriginal):
    input("segunda")
    pass





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
                        ClaveGuardada=CambiarClave(ClaveGuardada)
                    elif opcionelegidalista==opc2:
                        print(opc2)
                        #Revisamos si la lista está vacía
                        if listacoordenadas==[]:
                            #Llamamos a la función ingresar coordenadas.
                            #reemplazando la lista original con el return de la función.
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            #si la lista no está vacía
                            #Llamamos a la función actualizar coordenadas.
                            ActualizarCoordenadas(listacoordenadas)
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
