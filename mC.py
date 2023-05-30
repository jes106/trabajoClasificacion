#!/usr/bin/env python
# -*- coding: iso-8859-1 -*

import bcC

class MetodoPoda():
    '''Método de poda para la tarea de clasificacion'''
    def __init__(self,propiedades):
        self.propiedades=propiedades
        self.diferencial=[]
        self.resultado=[]
        
    def obtenerConjuntoDiferencial(self):
        '''
        Obtiene el conjunto diferencial
        
        @rtype:   list
        @return:  Conjunto de hipotesis
        '''
        p=Poda(self.propiedades)#Invoca la inferencia de poda
        self.diferencial=p.execute()
 
        return self.diferencial
        
    def execute(self):
        '''
        Ejecución del metodo de poda para la tarea de clasificacion
        
        @rtype:   list
        @return:  Devuelve conjunto de hipotesis compatibles con los observables
        '''
        p=Poda(self.propiedades)
        self.diferencial=p.execute()
        
        lpropi=len (self.propiedades)
        for i in range(lpropi):
            #obtiene atributo
            atr=Especificar(self.propiedades,i)
            self.atributo=atr.execute()
            #obtiene valor atributo
            valor=Obtener(self.atributo)
            self.valor=valor.execute()
            #Comprueba el valor en cada clase
            self.ultimo=False
            j=0
            while self.diferencial:


                igualdad=Equiparar(self.valor,self.diferencial[j])
                self.igual=igualdad.execute()
                if not self.igual:
                    #Comprueba si el que se va a borrar es el último,
                    #si es asi se espera a que se borre la hipotesis para salir del bucle
                    if self.diferencial[-1] == self.diferencial[j]:
                        self.ultimo=True
                    self.diferencial.remove(self.diferencial[j])
                    if self.ultimo:
                        break
                else:
                    #Comprueba si se ha terminado de recorrer el array
                    if self.diferencial[-1] == self.diferencial[j]:
                        break
                    else:
                        j+=1
                    
        self.resultado=self.diferencial

        return self.resultado
            
        
            
class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass
      
class Poda(Inferencia):
    '''
    Se presenta una lista de propiedades y proporciona una lista de posibles 
    hipotesis
    '''
    def __init__(self,propiedades):
        Inferencia.__init__(self)
        self.propiedades=propiedades
        self.listaHipotesis=[]
    def execute(self):
        '''
        Genera las clases candidatas a ser solucion
        '''
        hipotesis= bcC.hipotesis()
        self.listaHipotesis=hipotesis
        return hipotesis
        
class Especificar(Inferencia):
    '''    
    Devuelve un atributo cuyo valor (desconocido)
    sera de utilidad para distinguir entre las clases candidatas
    '''
    def __init__(self,propiedades,indice):
        Inferencia.__init__(self)
        self.propiedades=propiedades
        self.indice=indice
    def execute(self):
        atributo=self.propiedades[self.indice]
        return atributo
        
class Obtener(Inferencia):
    '''
    Obtiene el valor asociado a un atributo en el
    objeto a clasificar
    '''
    def __init__(self,caracteristica):
        Inferencia.__init__(self)
        self.caracteristica=caracteristica
    def execute(self):
        return self.caracteristica.valor
        
class Equiparar(Inferencia):
    '''
    Comprueba si una clase candidata tiene una caracteristica
    '''
    def __init__(self,valor,claseCandidata):
        Inferencia.__init__(self)
        self.valor=valor
        self.claseCandidata=claseCandidata
        self.igual=False
    def execute(self):
        
        nRasgos=len (self.claseCandidata.debePresentar)
        for i in range(nRasgos):
            #print i
            if self.valor==self.claseCandidata.debePresentar[i].valor:
                self.igual=True
                
        return self.igual
                
        
if __name__ == '__main__':
    
    if True:
        precio=bcC.Precio('bajo')
        metros=bcC.Metros('<100')
        banos=bcC.Banos('no tiene')
        mp=MetodoPoda([precio,metros,banos])
        mp.execute()
