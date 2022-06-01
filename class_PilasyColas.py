class Cola:
    def __init__ (self):
        self.Initial = None
        self.Final = None
        self.Cola = []
        
    def GetInicial(self):
        return self.Initial
    
    def GetFinal(self):
        return self.Final
    
    def add(self, elemento):
        self.Cola.append(elemento)
        self.Final = elemento
        return self.Final
    
    def remove(self):
        self.Cola.pop(0)
        self.Initial = self.Final
        self.Final = -1
        return self.Initial
    
    def __str__(self):
        return str(self.Cola)    

    def __len__(self):
        return len(self.Cola)    
    
    def vacia(self): ##Creamos la funcion empty
        return self.Initial == []
    
mcol=Cola()  
listaaa = ("Reviar los admin")
listaaa2= ("Mandar correos")
listaaa3= ("Revisar errores")
mcol.add(listaaa)
mcol.add(listaaa2)
mcol.add(listaaa3)