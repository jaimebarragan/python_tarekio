
#Importamos las librerias que usaremos
import os
import time
import random #No se necesita para el reto de la plataforma.

#Elaborar un programa parecido al del reto 2:
#Deben cumplirse todas las reglas del reto 1.
#Debe tener un menú con las siguientes opciones:
#cambiar contraseña; ingresar restaurantes del sector; 
# ubicar restaurante más cercano; guardar archivo con restaurante cercano, 
# actualizar restaurantes cercanos desde archivo, elegir favorito, cerrar sesión
#El menú debe ser recurrente; es decir no debe finalizar la ejecución al no ser que sea indicado.
#Si el usuario elije una opción inválida sacará error personalizado y finalizará la ejecución
#Si el usuario comete 5 errores en el menú principal, sacará error personalizado y finalizará la ejecución.
#Cada vez que el usuario ingrese a una opción del menú se mostrará un mensaje con el texto de la opción elegida
#Independientemente de su posición, el mensaje debe ser el de dicha opción.
#En la opción de mover el favorito, se le preguntará al usuario cuál es la opción que desea mover.
#Puede mover todas menos las dos últimas.
#En caso de opción equivocada se mostrará un error y se volverá al menú inicial.
#Si la opción es válida; se realizará una doble comprobación para confirmar la operación.
#La primera será escribir un número al azar (dado por el sistema)
#La segunda será resolver una simple suma.
#En caso de error en alguna comprobación sacará error y se regresará al menú principal.
#Si las dos comprobaciones son exitosas se volverá al menú inicial
# mostrándolo ordenado con la opción favorita de primera.
#Si se cierra sesión se deberá mostrar un mensaje de despedida y finalizar la ejecución.

#Creamos una variable con el contenido de cada opción de la lista; ésto nos permite modificar todo más adelante.
#De una forma más rápida y efectiva.

opc1="Cambiar contraseña"
opc2="Ingresar restaurantes del sector"
opc3="Ubicar restaurantes más cercanos"
opc4="Actualizar restaurantes cercanos"
opc5="Guardar archivo con restaurantes cercanos"
opc6="Elegir opción favorita"
opc7="Cerrar sesión"

#Creamos una lista con cada opción del menú.
listamenu=[opc1,opc2,opc3,opc4,opc5,opc6,opc7]

#Variable que contará los errores en caso de opción equivocada.
contadorerrores=0
    
UsuarioGuardado="usuario"
ClaveGuardada=123
captcha1=123
captcha2=int((2*2)+(2**2)/(2+2)-1)
captcha=captcha1-captcha2 

print("Bienvenido a la práctica de Python")
UsuarioIngresado=input("Ingrese su usuario: ") 
if UsuarioIngresado==UsuarioGuardado: 
    if int(input("Ingrese su contraseña: ")) == ClaveGuardada: 
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} - {captcha2}: "))
        if verificacion == captcha:
            os.system("cls")
            print("Sesión Iniciada.")
            time.sleep(2)
            #Creamos un ciclo while, éste se encargará de que el menú sea recurrente.
            #Éste ciclo se ejecutara mientras el contador de errores sea menor a 5.
            while contadorerrores<5:
                os.system("cls")
                #Creamos un ciclo for que nos muestra cada elemento de la lista y su número
                #en líneas separadas.
                for x in range(len(listamenu)):
                    print(f"{x+1} - {listamenu[x]}")
                opcionelegida=int(input("Por favor selecciona una opción: ")) #Pedimos la opción que el usuario desea y la guardamos.
                if opcionelegida > 0 and opcionelegida < 8: #Confirmamos que la opción elegida sea válida para evitar problemas con la lista
                    #Guardamos el texto de la opción que el usuario elige en una variable
                    opcionelegidalista=listamenu[opcionelegida-1] #El -1 es para arreglar el desfaze visual de los números del menu.
                    #Comparamos el texto de la opción elegida, con los textos guardados para activar funcionalidad escalable.
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
                        nuevofavorito=int(input("Ingrese el número de la opción que desea mover: ")) #solicitamos la opción a mover.
                        if nuevofavorito == 1 or nuevofavorito ==2 or nuevofavorito ==3 or nuevofavorito ==4 or nuevofavorito==5: #ejecutamos sólo si se puede mover.
                            numerorndm=random.randint(0,10000)#generamos un número aleatorio y lo pedimos en la verificación.
                            if int(input(f"Por favor escriba el siguiente número: {numerorndm}:")) == numerorndm:
                                if int(input("Por favor resuelva la siguiente suma 9 + 9:"))==18:
                                    #guardamos en la variable mover, el elemento de la lista elegido por el usuario.
                                    mover=listamenu[nuevofavorito-1]
                                    listamenu.remove(mover)#eliminamos el objeto de la lista
                                    listamenu.insert(0,mover)#lo agregamos de nuevo en la posición inicial
                                #Inicia la cascada de errores según las condiciones.
                                else:
                                    os.system("cls")
                                    print("Error comprobación 2.")
                                    time.sleep(2)
                            else:
                                os.system("cls")
                                print("Error comprobación 1.")
                                time.sleep(2)
                        else:
                            os.system("cls")
                            print("Opción inválida.")
                            time.sleep(2)
                            continue #reiniciamos el ciclo while
                    elif opcionelegidalista==opc7:
                        os.system("cls")
                        print("Sesión Cerrada")
                        time.sleep(2)
                        exit()
                else:
                    contadorerrores+=1 #aumentamos el contador de errores
                    os.system("cls")
                    print("Opción no válida")
                    time.sleep(2)
                    continue    #reiniciamos el ciclo while         
    
        else:
            print("Error, captcha incorrecto.")
    else:
        print("Error, contraseña incorrecta")
else:
    print("Error, usuario incorrecto.")
