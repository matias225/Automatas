tokens = ["=","+","*","/","-",".","0","1","2","3","4","5","6","7","8","9"]
errorl = 0
errors = 0
i = 0
cadena = []

cadena = input("Ingrese la operación matemática a resolver:\n")
print("Operación ingresada:")
print(cadena)

num = len(cadena)
while i < num:
    if tokens[0] in cadena[i]:
        print("signo =")
    elif tokens[1] in cadena[i]:
        print("signo +")
    elif tokens[2] in cadena[i]:
        print("signo *")
    elif tokens[3] in cadena[i]:
        print("signo /")
    elif tokens[4] in cadena[i]:
        print("signo -")
    elif tokens[5] in cadena[i]:
        print("punto")
    elif tokens[6] in cadena[i]:
        print("Numero 0")
    elif tokens[7] in cadena[i]:
        print("Numeor 1")
    elif tokens[8] in cadena[i]:
        print("Numero 2")
    elif tokens[9] in cadena[i]:
        print("Numero 3")
    elif tokens[10] in cadena[i]:
        print("Numero 4")
    elif tokens[11] in cadena[i]:
        print("Numero 5")
    elif tokens[12] in cadena[i]:
        print("Numero 6")
    elif tokens[13] in cadena[i]:
        print("Numero 7")
    elif tokens[14] in cadena[i]:
        print("Numero 8")
    elif tokens[15] in cadena[i]:
        print("Numero 9")
    else:
        errorl += 1
        print("Error lexico: caracter no valido: " +cadena[i])
    i = i + 1

if(errorl == 0):
    for i in range(num-1):
        if(cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/" or cadena[i]=="="):
            if (cadena[i+1] == "+" or cadena[i+1] == "-" or cadena[i+1] == "*" or cadena[i+1] == "/" or cadena[i+1] == "="):
                print("Error sintactico: La operacion no puede contener signos seguidos")
                errors += 1

    if(cadena[0] == "*" or cadena[0] == "/" or cadena[0] == "="):
        print("Error sintactico: La operacion solo puede comenzar con signo + o -")
        errors += 1

    if(cadena[num - 1] != "="):
        print("Error sintactico: La operacion debe terminar con signo =")
        errors += 1
else:
    if(errorl > 1):
        print("Se encontraron "+ str(errorl) +" errores léxicos, no se analizaran errores sintácticos")
    else:
        print("Se encontró " + str(errorl) + " error léxico, no se analizaran errores sintácticos")

if(errors > 0):
    if(errors > 1):
        print("Se encontraron " + str(errors) + " errores sintácticos")
    else:
        print("Se encontró " + str(errors) + " error sintactico")

if(errors == 0 and errorl == 0):
    print("No hay errores léxicos, ni errores sintácticos")