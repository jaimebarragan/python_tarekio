import os
import time
import random 

#Tendremos la siguiente base de datos para trabajar.
# Lat1: 10,127
# Lon1: -74,950
# Numero de platos: 50
# Lat2: 10,196
# Lon2: -74,935
# Numero de platos: 15
# Lat3: 10,305
# Lon3: -75,040
# Numero de platos: 32
# Lat4: 10,196
# Lon4: -74,935
# Numero de platos: 17

#El usuario ingresará a la opción 3.
#en caso de que no existan restaurantes del sector (opción 2), mostrará un error y finalizará la ejecución.
#si ya están ingresadas el sistema nos mostrará sus 3 restaurantes favoritos (opción 2)
#y se le pedirá en qué restaurante se encuentra

#si se elige una opción inválida  mostrará error y volverá a la lista del menú.
#en caso de elegir una opción válida el programa calculará la distancia entre el restaurante actual
#y los de las bases de datos y mostrar los dos mas cercanos ordenados según la cantidad de platos.
#el usuario deberá elegir la opción 1 o la 2 para recibir indicaciones.

#el programa nos mostrará la dirección en la cual debe dirigirse (primero ir al sur, luego al occidente)
#y el tiempo aproximado que tardará en moto y en bicicleta

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
listadepuracion=[[10.103,-74.902],
                 [10.115,-75.085],
                 [10.108,-74.801]]
listacoordenadaspredet=[[50,20],
                        [50,20],
                        [50,20]]
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
        
def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)
    for x in range (0,3):
        listaduplicada.append([])
        lat=input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lat=float(lat)
        if lat >= 10.103 and lat <= 10.362:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
            lon=float(lon)
            if lon >= -75.088 and lon <= -74.319:
                listaduplicada[x].insert(0,lat)
                listaduplicada[x].insert(1,lon)
                
                
            else:
                ErrorConMensaje("Longitud fuera del rango")
                listaduplicada=[]
                return listaduplicada
        else:
            ErrorConMensaje("Latitud fuera del rango")
            listaduplicada=[]
            return listaduplicada
    print("Coordenadas Ingresadas correctamente")
    time.sleep(2)    
    return listaduplicada

def Ordenarlatitudes(listaoriginal):
    print(f"La coordenada que está mas al sur es: {min(listaoriginal, key=lambda posicion: posicion[0])}")

def OrdenarLongitudes(listaoriginal):
    print(f"La coordenada que está mas al oriente es: {max(listaoriginal, key=lambda posicion: posicion[1])}")
    
def PromedioCoordenadas(listaoriginal):
    print(f"EL promedio de las latitudes es: {(listaoriginal[0][0]+listaoriginal[1][0]+listaoriginal[2][0])/3}")

def ImprimirCoordenads(listaoriginal):
    
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
    Ordenarlatitudes(listaduplicada)
    OrdenarLongitudes(listaduplicada)
    PromedioCoordenadas(listaduplicada)
    choice=int(input("Por favor ingrese la opción que desea modificar:"))

    if choice !=1 and choice !=2 and choice !=3:
        ErrorConMensaje("Esa opción es inválida")
        return 
    else:
      
        ActualizarCoordenadas(choice,listaoriginal)

def ActualizarCoordenadas(choice,listaoriginal):

    listaduplicada=list(listaoriginal)
    choice=choice-1 
    lat=input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
    lat=float(lat)
    if lat >= 10.103 and lat <= 10.362:
        lon=input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lon=float(lon)
        if lon >= -75.088 and lon <= -74.319:

            listaduplicada[choice][0]=lat
            listaduplicada[choice][1]=lon
            
        else:
            ErrorConMensaje("Longitud fuera del rango")
            listaduplicada=[listaoriginal] 
            return listaduplicada
    else:
        ErrorConMensaje("Latitud fuera del rango")
        listaduplicada=[listaoriginal] 
        return listaduplicada
    
    return listaduplicada

#Creamos la función calcular distancias, tomará como parámetro la opción elegida por el usuario en la función 
#imprimir restaurantes, la lista original, y la lista de coordenadas fijas de la base de datos.
def calcularDistancias(IndRestauranteactual,listaoriginal,coordenadasfijas):
    listaduplicada=list(listaoriginal)#asignamos los métodos de listas a las copias
    listaduplicadafijas=list(coordenadasfijas)
    print(listaduplicada)
    print(listaduplicadafijas)
    time.sleep(2)
    pass

#Creamos la función imprimir restaurantes favoritos
def ImprimirRestaurantesFav(listaoriginal):
    #usamos la misma lógica de la función actualizar coordenadas, solo que sin las funciones que llaman a promedio y
    #coordenadas al norte/sur.
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
    #Pedimos al usuario el restaurante actual.    
    opcion=int(input("Por favor seleccione su restaurante actual: "))
    if opcion == 1 or opcion ==2 or opcion ==3: #comparamos si es una opcion válida y llamamos la funcion calc distancia.
        calcularDistancias(opcion,listaduplicada,listacoordenadaspredet)
    else:
        ErrorConMensaje("Restaurante inexistente.")#en caso de error mostramos el mensaje

#creamos la función mostrar restaurantes fav    
def MostrarRestaurantesFav(listaoriginal):
    if listaoriginal==[]: #si la lista está en blanco mostramos error y salimos del programa
        ErrorConMensaje("No hay restaurantes favoritos ingresados.")
        exit()
    else:
        ImprimirRestaurantesFav(listaoriginal) #en caso de tener datos ejecutamos la función que sigue la cadena.
        
MostrarRestaurantesFav(listadepuracion)

"""
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
                        if listacoordenadas==[]:
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            ImprimirCoordenads(listacoordenadas)
                        
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
"""
