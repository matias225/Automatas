import Functions as fnc
from os import path

if not path.exists("./Usuarios WiFi.txt"):
    print("El archivo no existe. Asegurese de que se encuentre en el mismo directorio.")
    exit()    

with open("./Usuarios WiFi.txt", "r") as file:
    data = file.readlines()

while True:
    fnc.menu()
    try:
        option = int(input("Opción: "))
    except ValueError:
        print("\nPor favor, ingrese un numero valido.")
        continue
    if option == 0:
        break
    elif option == 1:
        # users, connectionsIds = fnc.getUsersAndIds(data)
        usersDir = fnc.getUsersAndIds(data)
        print("\nLista de usuarios y sus id de conexion:")
        # for i in range(len(users)):
        #     print("{:<25}".format(users[i]), connectionsIds[i])
        for user, ids in usersDir.items():
            print(f"\nUsuario: {user}\nIDs: {', '.join(ids)}")
    elif option == 2:
        date = input("Ingrese la fecha en formato DD/MM/YYYY: ")
        if fnc.validateDate(date):
            loggedUsers = fnc.getLoggedUsersList(data, date)
            if loggedUsers:
                print(f"\nLista de usuarios con inicio de sesion en la fecha {date}:\n")
                for user in loggedUsers:
                    print(user)
            else:
                print("\nNo se encontro inicios de sesion en la fecha indicada.")
        else:
            print("\nFormato de fecha incorrecto.")        
    elif option == 3:
        requestedUser = input("Ingrese el nombre del usuario: ")
        result = fnc.getSessionTimeByUser(data, requestedUser)
        if result == "WrongUser":
            print("\nUsuario incorrecto.")
        elif result:
            print(f"\nTiempo total de sesion para {requestedUser}:", result)
        else:
            print("\nSin tiempo total de sesion.")
    elif option == 4:
        requestedUser = input("Ingrese el nombre del usuario: ")
        macs = fnc.getUserMac(data, requestedUser)
        if macs:
            print(f"\nMACs del usuario {requestedUser} son: \n")
            for mac in macs:
                print(mac)
        else:
            print("\nEl usuario ingresado no existe.")
    elif option == 5:
        apMac = input("Ingrese el AP: ")
        macs = fnc.getApMac(data, apMac)
        if macs:
            print(f"\nMACs asociadas al AP {apMac}:\n")
            for mac in macs: 
                print(mac)
        else:
            print("\nEl AP ingresado no existe o no tiene MACs asociadas.")
    else:
        print("\nOpción inválida. Por favor intente de nuevo.")