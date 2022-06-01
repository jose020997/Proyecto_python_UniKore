import heapq
import itertools
import pandas as pd

class PrioridadCola():
    
    def __init__(self,l=[],e={}):
        self.lista = l
        self.entry_finder = e
        self.contar = itertools.count()
        self.REMOVED = '<removed-task>'
    
    def add_task(self,task,priority=0): #agregar tarea o modificar prioridad 
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.contar)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.lista, entry)
        
    def remove_task(self,task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED
        
    def pop_task(self):
        while self.lista:
            priority, count, task = heapq.heappop(self.lista)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
            raise KeyError('No se puede popear un elemento vacio')
                
lista=[]
entr={}
j=PrioridadCola(lista,entr)

tareas = pd.read_csv('tareas_admin.csv') #leemos el archivo
for x in range(0,len(tareas)):
    j.add_task(tareas.iat[x,0],tareas.iat[x,1])