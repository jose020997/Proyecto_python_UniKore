#Errores en la lista de prio sale un none debajo, mirar lo de los operadores logicos
#Comprobar si existe el user para no crear y darle a recordar contraseña
#importaciones
import class_Hash_table
import class_PrioridadCola
from sklearn import tree
from csv import reader
from csv import writer
import class_PilasyColas
import pandas as pd
from PIL import Image


#declaracion de variables iniciales y abreviadas
h = class_Hash_table.H
prio_cola = class_PrioridadCola.j
mcola = class_PilasyColas.mcol
im = Image.open('imagen_juego.png')

#creamos las definiciones
def lectura(fich): #leemos todos los datos del csv y los insertamos en la lista hash
    with open(fich, 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        cadena=len(list_of_rows) #nos da la lista con todo el csv

    jose = "" #creamos una cadena vacia
    for palabra in list_of_rows:
        jose += str(palabra)
    
    characters = "'!?[" #caracteres que vamos a quitar

    for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
        jose = jose.replace(characters[x],"")

    separador = "]"
    separado = jose.split(separador) #sin los caracteres recortamos por el que hemos dejado
    #separado tiene ['jose:123', 'carlos:carlos123', 'manu123:clave123', 'admin:admin', '']
    for x in range(0,len(separado)-1): #hacemos un bucle y como hemos recortado
        h.Insert(separado[x]) #insertamos uno a uno

def lectura_sin_cortar(fich): #no cortamos ningun dato
    with open(fich, 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        return list_of_rows

#Escritura de archivos
def escribir(archivo,lista): #definicion para guardar los datos en una lista
    with open(archivo,'a', newline='') as datos:
        writer_object = writer(datos)
        writer_object.writerow(lista)

#Juego del servicio
def juego():
        clf = tree.DecisionTreeClassifier()
        X = [[1,0,0,0,1,0],[1,0,0,0,0,1],[0,0,0,0,1,1],[0,1,1,0,0,0],[0,0,0,0,0,1],[0,0,1,0,0,0],[0,0,1,0,1,1],[0,0,0,1,0,0],[0,0,1,0,1,0],[1,0,0,0,1,1],[0,0,0,0,0,0],[0,1,1,0,0,1],[0,0,0,1,1,0],[1,1,0,1,0,0],[0,0,1,0,0,1],[0,0,0,1,0,0],[1,0,0,0,0,0]]
        Y = ['tigre','raton','perro','cabra','hormiga','cerdo','jirafa','ballena','cebra','gato','mono','elefante','pez','morsa','oveja','murcielago','leon']
        clf = clf.fit(X,Y)
        #dato = [150,70,35]
        im.show()
        animal=input("piensa en tu animal ->  ")
        
        bigote=input("Tiene Bigote : ")
        if bigote == "si" or bigote == "s" or bigote == "1":
            bigote = 1
        else:
            bigote = 0
        cuernos=input("Tiene Cuernos/Dientes largos : ")
        if cuernos == "si" or cuernos == "s" or cuernos == "1":
            cuernos = 1
        else:
            cuernos = 0
        pezu=input("Tiene Pezuñas : ")
        if pezu == "si" or pezu == "s" or pezu == "1":
            pezu = 1
        else:
            pezu = 0
        alas=input("Tiene Alas/Escanas : ")
        if alas == "si" or alas == "s" or alas == "1":
            alas = 1
        else:
            alas = 0
        ralla=input("Tiene Rallas o Lunares : ")
        if ralla == "si" or ralla == "s" or ralla == "1":
            ralla = 1
        else:
            ralla = 0
        ojo=input("Tiene ojos azules : ")
        if ojo == "si" or ojo == "s" or ojo == "1":
            ojo = 1
        else:
            ojo = 0

        dato=[bigote,cuernos,pezu,alas,ralla,ojo]


        prediction = clf.predict([dato])
        
        print("¿habras acertado? ")
        if animal == prediction:
            print("Correcto")
            p=1
        else:
            print("No es correcto, lo siento campeon")
            p=0
        return p

#Recortar de las Listas de prioridad solo muestra la primera tarea mas importante
def recortar_listaprioridad(lista,num):
    jose = "" #creamos una cadena vacia
    for palabra in lista:
        jose += str(palabra)
    
    characters = "'!?[" 
    for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
        jose = jose.replace(characters[x],"")
    
    separador = "]"
    separado = jose.split(separador)#sin los caracteres recortamos por el que hemos dejado
    separador2 = ","
    separado2 = separado[0].split(separador2)
    print(separado2[num])

def lectura_existe(fich,varia): #leemos todos los datos del csv y los insertamos en la lista hash
    with open(fich, 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        cadena=len(list_of_rows) #nos da la lista con todo el csv

    jose = "" #creamos una cadena vacia
    for palabra in list_of_rows:
        jose += str(palabra)
    p=""
    characters = "'!?[" #caracteres que vamos a quitar

    for x in range(len(characters)): #recorremos todos los caracteres y quitamos lo que sobra
        jose = jose.replace(characters[x],"")

    separador = "]"
    separado = jose.split(separador) #sin los caracteres recortamos por el que hemos dejado
    #separado tiene ['jose:123', 'carlos:carlos123', 'manu123:clave123', 'admin:admin', '']
    for x in range(0,len(separado)-1): #hacemos un bucle y como hemos recortado
        separador2= ","
        existe=separado[x].split(separador2)
        p+=existe[varia] + ":"
    return p

#verdadero main del programa
try:
    x=1
    lectura("datos.csv")
    while x!=0:
        print("---------------------------")
        print("--->   Hola / Ciao     <---")
        print("                           ")
        print("1. Loggearse")
        print("2. No recuerdo mi contraseña")
        print("3. Crear una nueva cuenta")
        print("4. Salir")
        try:
            iniC=int(input("---> "))
            if iniC == 1:
                nombre=input("Introduce el usuario  ")
                clave=input("Introduce la contraseña  ")
                validacion=h.Search(nombre+":"+clave)
                es_admin=(nombre+":"+clave)

                if validacion!=None: #Si el usuario existe
                    p=lectura_existe("puntuacion.csv",0)
                    separador=":"
                    s=p.split(separador)
                    if nombre in s: #Si esta creado en el fichero pun
                        print("existe")
                    else: #Si no esta creado en el fichero pun
                        print("no existe") 
                        l=[nombre,0]
                        escribir("puntuacion.csv",l)
                        
                    if es_admin==("root:root"): #funciones de root
                        print("Hola root")
                        menu = 0
                        salir=False
                        while not salir:
                            print("1. Anotar tareas")
                            print("2. Revisar tareas")
                            print("3. Eliminar tarea completada")
                            print("4. Poner puntos a 0 o sumar 5")
                            print("5. Salir")
                            print("----------------")
                            try: #posible error en el campo menú
                                menu=int(input("Que vamos a hacer hoy : "))
            
                                if menu == 1:
                                    print("1")
                                    tare=(input("Que tarea quiere añadir: "))
                                    añadir=(tare)
                                    mcola.add(añadir)
                                    
                                elif menu ==2:
                                    print("2")
                                    print(mcola)
                                    
                                elif menu == 3:
                                    if len(mcola) == 0:
                                        print("No tienes mas tareas")
                                        print("")
                                        print("")
                                    else:    
                                        print(mcola)
                                        print("      ^")
                                        jose=mcola.remove()
                                        print("Has completado la tarea, tareas pendientes :")
                                        if len(mcola)==0:
                                            print("No tienes mas tareas")
                                        else:    
                                            print(mcola)
                                        print("")
                                        print("")
                                        
                                elif menu == 4:
                                    lista=[]
                                    lista2=[]        
                                    lista=lectura_sin_cortar("puntuacion.csv")

                                    for x in range(0,len(lista)):
                                        lista2.append(int(lista[x][1]))
                                        
                                    cuadrados = list(map(lambda x : x + 5, lista2))
                                    menu=int(input("1 para poner a 0 y cualquiera para sumar 5 : "))
                                    if menu == 1:
                                        df = pd.read_csv("puntuacion.csv",header=None, names=None) #cambiamos el score en el csv
                                        for x in range(0,len(cuadrados)):
                                            df.iat[x,1]=0
                                            df.to_csv("puntuacion.csv", index=False, header=False)
                                            print("Datos reseteados")
                                    else:
                                        df = pd.read_csv("puntuacion.csv",header=None, names=None) #cambiamos el score en el csv
                                        for x in range(0,len(cuadrados)):
                                            df.iat[x,1]=cuadrados[x]
                                            df.to_csv("puntuacion.csv", index=False, header=False)
                                            print("Valores modificados, Felicidades")
                                            
                                else:
                                    print("¿Has completado el dia? Esperemos que si")
                                    salir=True
                                    x=0
                                    
                            except ValueError: #Control en root de menu
                                print("Porfavor introduzca un numero querido Root")
                                
                    elif es_admin==("admin:admin"): #Si eres Admin las lista de tareas
                        print("")
                        print("Bienvenido Administrador")
                        menu = 0
                        salir=False
                        while not salir:
                            print("")
                            print("1. Completar las tareas")
                            print("2. Salir")
                            print("----------------")
                            print("")
                            try: #Control del mismo try en admin
                                menu=int(input("Que vamos a hacer hoy : "))
                                if menu == 1:
                                    cerrar=0
                                    for x in range(0,len(prio_cola.lista)):
                                        if cerrar==1:
                                            break
                                        else:
                                            #Es none tipe entonces me sale el None ese pochisimo
                                            a = recortar_listaprioridad(prio_cola.lista,2)
                                            print("" if a is None else a)
                                            conti=0
                                            while conti!= 1:
                                                print("")
                                                print("para descansar pulse cualquier numero")
                                                continuar=int(input("Cuando termine la tarea pulse 1:    "))
                                                print("")
                                                if continuar==1:
                                                    prio_cola.pop_task()
                                                    conti=1
                                                else:
                                                    cerrar=1
                                                    break
                                                
                                    print("No queda tareas o has descansado")
                                else :    
                                    print("Hasta otro dia Admin")
                                    salir=True
                                    x=0
                                    
                            except ValueError: #Control en menu de admin 
                                print("Porfavor introduzca un numero querido Admin")        
                    else: #Cualquier usuario valido
                        usuario=False
                        while not usuario:
                            print("     ")
                            print(" --------------------    ")
                            print("     ")
                            print("1. Jugar al minijuego")
                            print("2. Reportar un problema o error")
                            print(" ")
                            print("- Para Salir cualquier numero -")
                            print("  ")
                            try:
                                menu=int(input("Que desea hacer hoy: " + nombre +"  ")) #sale NONE nose porque
                                # Añadir cosas al menu
                                if menu == 1: # muestra la puntuacion
                                    p2=lectura_existe("puntuacion.csv",0)
                                    puntos=lectura_existe("puntuacion.csv",1)
                                    separador=":"
                                    s2=p2.split(separador)
                                    punto = puntos.split(separador)

                                    indice=(s2.index(nombre))
                                    print("tienes"+punto[indice]+" puntos")
                                    nuevo_score=int(punto[indice])
                                    nuevo_indice=int(indice)
                                    
                                    score=nuevo_score #parte del juego
                                    salir=False
                                    while not salir:
                                        #print(juego())
                                        if juego() == 1:
                                            score=score+1
                                        else:
                                            score=score
                                        print("Puntos :")
                                        print(score)    
                                        menu=input("Quiere salir : ")
                                        if menu == "si" or menu == "s":
                                            salir=True
                                    #final del juego
                                    df = pd.read_csv("puntuacion.csv",header=None, names=None) #cambiamos el score en el csv
                                    a=nuevo_indice
                                    df.iat[a,1]=score
                                    df.to_csv("puntuacion.csv", index=False, header=False)
                                    print("puntuacion modificada")
                                    
                                elif menu == 2:
                                    print("Hola, cual es su problema") #Se añade con prioridad 10 siempre
                                    añadir=input("Escriba aqui : ")
                                    añadir_cola= añadir + " del usu -> "+ nombre
                                    if añadir_cola.find("user")!= -1 or añadir_cola.find("usuario")!= -1: #problema de usuario es nvl 3
                                        print("usuario problema")
                                        prio_cola.add_task(añadir_cola,3)
                                        cosas_admin=[añadir_cola , 4]
                                        escribir("tareas_admin.csv",cosas_admin)                       
                                    elif añadir_cola.find("clave")!=-1 or añadir_cola.find("contraseña")!=-1: #problema de clave nvl 1
                                        print("clave problema")
                                        prio_cola.add_task(añadir_cola,1)
                                        cosas_admin=[añadir_cola , 2]
                                        escribir("tareas_admin.csv",cosas_admin)
                                    else:
                                        print("nada raro")
                                        prio_cola.add_task(añadir_cola,10)
                                        cosas_admin=[añadir_cola , 10]
                                        escribir("tareas_admin.csv",cosas_admin)
                                    
                                else:
                                    usuario=True   
                                    x=0
                            except ValueError: #Control en menu de user
                                print("Porfavor introduzca un numero")          
                else:
                    a = lectura_existe("datos.csv",0)   
                    if nombre in a:
                        print(" ")
                        print("La contraseña no es correcta")
                        print(" ")
                    else:
                        print(" ")
                        print("El usuario no existe")
                        print(" ")
                    
            elif iniC==2:
                intento=0
                quedarse = False
                while not quedarse:
                    print("")
                    print("para salir escriba -> salir")
                    print("Hola, cual es su usuario") #Se añade con prioridad 10 siempre
                    añadir=input("--->  ")
                    a = lectura_existe("datos.csv",0)   
                    if añadir in a:
                        añadir_correo=input("Introduce el correo en el que desea optener la informacion:    ")
                        añadir_cola= "No recuerda la calve el usu -> "+ añadir + " mandar al correo " + añadir_correo
                        prio_cola.add_task(añadir_cola,1) #Es lo mas urgente porque no puede acceder al correo
                        cosas_admin=[añadir_cola , 1]
                        escribir("tareas_admin.csv",cosas_admin)  
                        print("Se le mandara la informacion lo antes posible")
                        quedarse=True
                        
                    elif añadir == "salir" or añadir == "Salir": #Si quiere salir el usuario
                        quedarse=True
                        
                    else:
                        print(" ")
                        print("Este usuario no existe, introduce uno diferente")
                        print(" ")
                        intento+=1
                        if intento==3: #Bloquear si lo intenta 3 veces
                            print("Maximo de intentos superados")
                            print("")
                            quedarse=True
                            x=0

            elif iniC==3:
                print("opcion 3")
                nnnombre=input("Introduce tu usuario  ")
                nnclave=input("Introduce tu clave   " ) 
                lista=[nnnombre+':'+nnclave]
                a = lectura_existe("datos.csv",0)   
                if nnnombre in a:
                    print(" ")
                    print("Este usuario ya existe, introduce uno diferente")
                    print("En la opcion 2 puede recuperar su clave")
                    print(" ")
                else:
                    escribir("datos.csv",lista)
                    h.Insert(nnnombre+":"+nnclave)   
                    print("Usuario creado correctamente")
            else:
                x=0
        except  ValueError :
            print("Valor introducido no correcto")          
except ValueError:
    print("Se ha introducido un valor no esperado")