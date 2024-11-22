from datetime import datetime

def getUsersAndIds(data):
    usersDir = {}
    # users = []
    # idConnections = []
    # for row in data:
    #     fields = row.strip().split(';')
    #     if len(fields) > 1:
    #         idConnection, user = fields[0], fields[1]
    #         if user not in usersDir and user:
    #             usersDir[user] = idConnection
    # for user, idConnection in usersDir.items():
    #     users.append(user)
    #     idConnections.append(idConnection)
    # return users, idConnections
    for row in data[1:]:
        fields = row.strip().split(';')
        if len(fields) > 1:
            idConnection, user = fields[0], fields[1]
            if user:
                if user not in usersDir:
                    usersDir[user] = []
                usersDir[user].append(idConnection)
    return usersDir

def getLoggedUsersList(data, date):
    loggedUsers = set()
    for row in data:
        fields = row.strip().split(';')
        sessionDate = fields[2]
        if date in sessionDate:
            loggedUsers.add(fields[1])
    return loggedUsers

def getSessionTimeByUser(data, requestedUser):
    totalTime = 0
    users = []
    for row in data:
        fields = row.strip().split(';')
        user = fields[1]
        if user not in users:
            users.append(user)
        if user == requestedUser:
            totalTime += int(fields[4])
    if requestedUser not in users:
        return "WrongUser"
    if totalTime:
        totalHours = totalTime // 3600
        totalMinutes = (totalTime // 60) - (totalHours * 60 )
        totalSeconds = totalTime - ((totalMinutes*60) + (totalHours * 3600))
        result = "\n"+ str(totalHours)+ " horas " + str(totalMinutes) + " minutos " + str(totalSeconds) + " segundos\n"
        return result
        
def getUserMac(data, requestedUser):
    mac = set()
    for row in data:
        fields = row.strip().split(';')
        user = fields[1]
        if user == requestedUser:
            mac.add(fields[8])
    if mac:
        return mac
    if requestedUser not in user:
        return False

def getApMac(data, apMac):
    macs = set()
    for row in data:
        fields = row.strip().split(';')
        if len(fields) > 8:
            ap, mac = fields[7], fields[8]
            if ap == apMac:
                macs.add(mac)
    return macs

def menu():
    print('\nSeleccione una opción:')
    print('1. Lista de todos los usuarios con su ID')
    print('2. Lista de inicio de sesión en una determinada fecha.')
    print('3. Tiempo total de la sesión de un usuario.')
    print('4. MAC de un usuario')
    print('5. MAC de un AP')
    print('0. Salir')
    
def validateDate(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        return True
    except ValueError:
        return False
    