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


class Equip(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Equipaje'
        atrib = 'Equipaje'
        valores = ['mucho', 'poco']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Fam(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Familia'
        atrib = 'Familia'
        valores = ['Si', 'No']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class Est(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Estancia'
        atrib = 'Estancia'
        valores = ['<10 días', '> 10 días']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)

class Hot(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Hotel'
        atrib = 'Hotel'
        valores = ['Si', 'No']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)

class Vue(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Vuelta'
        atrib = 'Vuelta'
        valores = ['Si', 'No']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)

def listaAtributos():
    '''Devuelve la lista de observables de la base del conocimiento'''
    atributos = []
    atributos.append(Equip())
    atributos.append(Fam())
    atributos.append(Est())
    atributos.append(Hot())
    atributos.append(Vue())

    return atributos


class Caracteristica():
    '''Definición de una caracteristica genérica'''

    def __init__(self, nombre=None, valoresPermitidos=None, valor=None):
        self.nombre = nombre
        self.valor = valor
        self.valoresPermitidos = valoresPermitidos


'''Definición de características precio, metros y baños'''


class Equipaje(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'equipaje'
        valoresPermitidos = ['mucho', 'poco']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Familia(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'familia'
        valoresPermitidos = ['Si', 'No']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Estancia(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'estancia'
        valoresPermitidos = ['<10 días', '>10 días']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor

class Hotel(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'estancia'
        valoresPermitidos = ['Si', 'No']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class Vuelta(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'vuelta'
        valoresPermitidos = ['Si', 'No']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor




def caracteristicas():
    '''Devuelve la lista de caracteristicas de la base de conocimiento'''
    obs = []
    obs.append(Equipaje())
    obs.append(Familia())
    obs.append(Estancia())
    obs.append(Hotel())
    obs.append(Vuelta())

    return obs


def creaCaracteristica(tp):
    if tp[0] == 'Equipaje':
        ob = Equipaje(tp[1])
        return ob
    elif tp[0] == 'Familia':
        ob = Familia(tp[1])
        return ob
    elif tp[0] == 'Estancia':
        ob = Estancia(tp[1])
        return ob
    elif tp[0] == 'Hotel':
        ob = Hotel(tp[1])
        return ob
    elif tp[0] == 'Vuelta':
        ob = Vuelta(tp[1])
        return ob
    return None


class Aspectos():
    '''Definición genérica de una zona'''

    def __init__(self, nombre):
        self.nombre = nombre


'''Definición de las zonas del sistema'''


class Ilegal(Aspectos):
    def __init__(self):
        # self.nombre='Ilegal'
        equipaje = Equipaje('mucho')
        familia = Familia('Si')
        familiaNo = Familia('No')
        estancia = Estancia('>10 días')
        estancia2 = Estancia('<10 días')
        hotel = Hotel('No')
        vuelta = Vuelta('No')
        self.debePresentar = [equipaje, familia, familiaNo, estancia, estancia2, hotel, vuelta]
        Aspectos.__init__(self, nombre=u'Ilegal')

class Legal(Aspectos):
    def __init__(self):
        # self.nombre='Legal'
        equipaje = Equipaje('poco')
        familia = Familia('Si')
        familiaNo = Familia('No')
        estancia = Estancia('<10 días')
        hotel = Hotel('Si')
        vuelta = Vuelta('Si')
        self.debePresentar = [equipaje, familia, familiaNo, estancia, hotel, vuelta]
        Aspectos.__init__(self, nombre=u'Legal')


def hipotesis():
    '''Devuelve la lista de zonas'''
    ilg = Ilegal()
    leg = Legal()
    lHp = [ilg, leg]
    return lHp
