#Se Inicializan las variables internas que usará el programa.
UsuarioGuardado="usuario" #Variable de tipo string
ClaveGuardada=123 #Variable de tipo entero
captcha1=123
captcha2=int((2*2)+(2**2)/(2+2)-1)  #El casteo a int; es por que la operación arroja como resultado un 4.0.
captcha=captcha1-captcha2 #Tener en cuenta que aquí se guarda el resultado de la operación matemática.

print("Bienvenido a la práctica de Python")
UsuarioIngresado=input("Ingrese su usuario: ") #Es importante guardar el dato que el usuario ingresa para escalabilidad.
if UsuarioIngresado==UsuarioGuardado: #El doble igual es una comparación, el igual sencillo es una asignación.
    
    #Podemos comparar directamente el input; pero no podríamos acceder al dato ingresado por el usuario
    #en un futuro; por eso es más recomendable usar el método de las línea 10 y 11
    if int(input("Ingrese su contraseña: ")) == ClaveGuardada: 
        verificacion=int(input(f"Por favor resuelva la siguiente operación {captcha1} - {captcha2}: "))
         #La F se usa para dar formato y concatenar cadenas más fácilmente; dentro de las llaves llamamos las variables que queremos mostrar.
         #Sólo es necesario usar comillas al comienzo y al final de la cadena de texto.
        if verificacion == captcha:
            print("Sesión Iniciada.")
        #Cascada de errores; revisar la indentación para saber de que if viene cada uno (están al mismo nivel)
        #Recomendación crear los else al momento de crear el IF para facilidad de organización.
        #Usar el pass para evitar que el IF arroje errores.
        else:
            print("Error, captcha incorrecto.")
    else:
        print("Error, contraseña incorrecta")
else:
    print("Error, usuario incorrecto.")
