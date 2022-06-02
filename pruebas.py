import class_Hash_table
import class_PrioridadCola
from sklearn import tree
from csv import reader
from csv import writer
import class_PilasyColas
import pandas as pd
from PIL import Image
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

prio_cola = class_PrioridadCola.j


a = recortar_listaprioridad(prio_cola.lista,2)
print("" if a is None else a)