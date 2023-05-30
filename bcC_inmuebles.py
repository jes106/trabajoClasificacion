#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

class Atributos():
    '''Definición de atributo'''

    def __init__(self, nombre=None, atrib=None, defecto=None, booleano=None, valores=None):
        self.nombre = nombre
        self.atrib = atrib
        self.defecto = defecto
        self.booleano = booleano
        self.valores = valores


'''Definición de los atributos del sistema'''


class Prec(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Precio'
        atrib = 'Precio'
        valores = ['bajo', 'medio', 'alto']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Met(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Metros'
        atrib = 'Metros'
        valores = ['<100', '>100', '>500']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Ban(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Banos'
        atrib = 'Banos'
        valores = ['tiene', 'no tiene']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


def listaAtributos():
    '''Devuelve la lista de observables de la base del conocimiento'''
    atributos = []
    atributos.append(Prec())
    atributos.append(Met())
    atributos.append(Ban())

    return atributos


class Caracteristica():
    '''Definición de una caracteristica genérica'''

    def __init__(self, nombre=None, valoresPermitidos=None, valor=None):
        self.nombre = nombre
        self.valor = valor
        self.valoresPermitidos = valoresPermitidos


'''Definición de características precio, metros y baños'''


class Precio(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'precio'
        valoresPermitidos = ['bajo', 'medio', 'alto']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Metros(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'metros'
        valoresPermitidos = ['<100', '>100', '>500']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Banos(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'banos'
        valoresPermitidos = ['tiene', 'no tiene']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


def caracteristicas():
    '''Devuelve la lista de caracteristicas de la base de conocimiento'''
    obs = []
    obs.append(Precio())
    obs.append(Metros())
    obs.append(Banos())
    return obs


def creaCaracteristica(tp):
    if tp[0] == 'Precio':
        ob = Precio(tp[1])
        return ob
    elif tp[0] == 'Metros':
        ob = Metros(tp[1])
        return ob
    elif tp[0] == 'Banos':
        ob = Banos(tp[1])
        return ob
    return None


class Aspectos():
    '''Definición genérica de una zona'''

    def __init__(self, nombre):
        self.nombre = nombre


'''Definición de las zonas del sistema'''


class Piso(Aspectos):
    def __init__(self):
        # self.nombre='Piso'
        precio = Precio('alto')
        pocosMetros = Metros('>100')
        siBanos = Banos('tiene')
        self.debePresentar = [precio, pocosMetros, siBanos]
        Aspectos.__init__(self, nombre=u'Piso')


class Atico(Aspectos):
    def __init__(self):
        # self.nombre='Atico'
        precio = Precio('bajo')
        pocosMetros = Metros('<100')
        siBanos = Banos('tiene')
        self.debePresentar = [precio, pocosMetros, siBanos]
        Aspectos.__init__(self, nombre=u'Ático')


class Garaje(Aspectos):
    def __init__(self):
        # self.nombre='Garaje'
        precio = Precio('bajo')
        pocosMetros = Metros('<100')
        noBanos = Banos('no tiene')
        self.debePresentar = [precio, pocosMetros, noBanos]
        Aspectos.__init__(self, nombre=u'Garaje')


class Local_Comercial(Aspectos):
    def __init__(self):
        # self.nombre='Local_Comercial'
        precio =Precio('medio')
        muchosMetros = Metros('>500')
        siBanos = Banos('tiene')
        noBanos = Banos('no tiene')
        self.debePresentar = [precio, muchosMetros, siBanos, noBanos]
        Aspectos.__init__(self, nombre=u'Local Comercial')


class Chalet(Aspectos):
    def __init__(self):
        precio = Precio('alto')
        metros = Metros('>500')
        siBanos = Banos('tiene')
        self.debePresentar = [precio, metros, siBanos]
        Aspectos.__init__(self, nombre=u'Chalet')


def hipotesis():
    '''Devuelve la lista de zonas'''
    pis = Piso()
    atc = Atico()
    gar = Garaje()
    loc = Local_Comercial()
    cha = Chalet()
    lHp = [pis, atc, gar, loc, cha]
    return lHp
