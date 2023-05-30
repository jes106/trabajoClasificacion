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


class Temp(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Temperatura'
        atrib = 'Temperatura'
        valores = ['muy baja', 'baja', 'suave', 'alta', 'muy alta']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Prec(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Precipitaciones'
        atrib = 'Precipitaciones'
        valores = ['escasas', 'alternantes', 'abundantes']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Veg(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Vegetacion'
        atrib = 'Vegetacion'
        valores = ['selva', 'sabana', 'escasa', 'bosque mediterraneo', 'bosque atlantico', 'bosque boreal o taiga',
                   'tundra', 'escalonada']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


def listaAtributos():
    '''Devuelve la lista de observables de la base del conocimiento'''
    atributos = []
    atributos.append(Temp())
    atributos.append(Prec())
    atributos.append(Veg())

    return atributos


class Caracteristica():
    '''Definición de una caracteristica genérica'''

    def __init__(self, nombre=None, valoresPermitidos=None, valor=None):
        self.nombre = nombre
        self.valor = valor
        self.valoresPermitidos = valoresPermitidos


'''Definición de características temperatura, precipitaciones y vegetacion'''


class Temperatura(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'temperatura'
        valoresPermitidos = ['muy baja', 'baja', 'suave', 'alta', 'muy alta']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Precipitaciones(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'precipitaciones'
        valoresPermitidos = ['escasas', 'alternantes', 'abundantes']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Vegetacion(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'vegetacion'
        valoresPermitidos = ['selva', 'sabana', 'escasa', 'bosque mediterraneo', 'bosque atlantico',
                             'bosque boreal o taiga', 'tundra', 'escalonada']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


def caracteristicas():
    '''Devuelve la lista de caracteristicas de la base de conocimiento'''
    obs = []
    obs.append(Temperatura())
    obs.append(Precipitaciones())
    obs.append(Vegetacion())
    return obs


def creaCaracteristica(tp):
    '''Crea una instancia de una caracteristica en el caso de que la tupla 
    coincida con la base de conocimiento'''
    if tp[0] == 'Temperatura':
        ob = Temperatura(tp[1])
        return ob
    elif tp[0] == 'Precipitaciones':
        ob = Precipitaciones(tp[1])
        return ob
    elif tp[0] == 'Vegetacion':
        ob = Vegetacion(tp[1])
        if tp[1] == 'True':
            ob.valor = True
        return ob
    return None


class Zona():
    '''Definición genérica de una zona'''

    def __init__(self, nombre):
        self.nombre = nombre


'''Definición de las zonas del sistema'''


class Ecuatorial(Zona):
    def __init__(self):
        # nombre='Ecuatorial'
        calor = Temperatura('muy alta')
        lluviasAbundantes = Precipitaciones('abundantes')
        plantas = Vegetacion('selva')
        self.debePresentar = [calor, lluviasAbundantes, plantas]
        Zona.__init__(self, nombre=u'Ecuatorial')


class Tropical(Zona):
    def __init__(self):
        # self.nombre='Tropical'
        calor = Temperatura('alta')
        lluviasAlternas = Precipitaciones('alternantes')
        plantas = Vegetacion('sabana')
        self.debePresentar = [calor, lluviasAlternas, plantas]
        Zona.__init__(self, nombre=u'Tropical')


class Desertico(Zona):
    def __init__(self):
        # self.nombre='Desertico'
        calor = Temperatura('muy alta')
        lluviasEscasas = Precipitaciones('escasas')
        plantas = Vegetacion('escasa')

        self.debePresentar = [calor, lluviasEscasas, plantas]
        Zona.__init__(self, nombre=u'Desertico')


class Mediterraneo(Zona):
    def __init__(self):
        # self.nombre='Mediterraneo'
        tempSuaveInvierno = Temperatura('suave')
        lluviasAlternas = Precipitaciones('alternantes')
        calorEstival = Temperatura('alta')
        plantas = Vegetacion('bosque mediterraneo')

        self.debePresentar = [tempSuaveInvierno, lluviasAlternas, calorEstival, plantas]
        Zona.__init__(self, nombre=u'Mediterraneo')


class Atlantico(Zona):
    def __init__(self):
        tempSuaveVerano = Temperatura('suave')
        lluviasAbundantes = Precipitaciones('abundantes')
        frioInvierno = Temperatura('alta')
        plantas = Vegetacion('bosque atlantico')

        self.debePresentar = [tempSuaveVerano, frioInvierno, plantas, lluviasAbundantes]
        Zona.__init__(self, nombre=u'Atlantico')


class Continental(Zona):
    def __init__(self):
        frioInvierno = Temperatura('baja')
        calorVerano = Temperatura('alta')
        lluviasAbundantes = Precipitaciones('abundantes')
        plantas = Vegetacion('bosque boreal o taiga')

        self.debePresentar = [frioInvierno, calorVerano, lluviasAbundantes, plantas]
        Zona.__init__(self, nombre=u'Continental')


class Polar(Zona):
    def __init__(self):
        frio = Temperatura('muy baja')
        lluviasEscasas = Precipitaciones('escasas')
        plantas = Vegetacion('tundra')

        self.debePresentar = [frio, lluviasEscasas, plantas]
        Zona.__init__(self, nombre=u'Polar')


class Montana(Zona):
    def __init__(self):
        frio = Temperatura('baja')
        lluviasAbundantes = Precipitaciones('abundantes')
        plantas = Vegetacion('escalonada')

        self.debePresentar = [frio, lluviasAbundantes, plantas]
        Zona.__init__(self, nombre=u'Montana')


def hipotesis():
    '''Devuelve la lista de zonas'''
    ecu = Ecuatorial()
    tro = Tropical()
    des = Desertico()
    med = Mediterraneo()
    atl = Atlantico()
    con = Continental()
    pol = Polar()
    mon = Montana()
    lHp = [ecu, tro, des, med, atl, con, pol, mon]
    return lHp
