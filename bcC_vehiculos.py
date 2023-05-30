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


class numeroRuedas(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Número de ruedas'
        atrib = 'numeroRuedas'
        valores = ['2', '3', '4']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class PMA(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Peso Máximo Autorizado'
        atrib = 'pma'
        valores = ['3500', '7500']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class edad(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Edad'
        atrib = 'edad'
        valores = ['15', '16', '18', '19', '20', '21', '24']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class numeroAsientos(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Número de asientos'
        atrib = 'numeroAsientos'
        valores = ['1', '9', '17']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class cilindrada(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Cilindrada'
        atrib = 'cilindrada'
        valores = ['49', '50', '125']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class potencia(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Potencia'
        atrib = 'potencia'
        valores = ['0', '15', '47']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


class pesoRemolque(Atributos):
    def __init__(self, defecto=None, booleano=False):
        nombre = 'Peso del remolque'
        atrib = 'pesoRemolque'
        valores = ['0', '750']
        Atributos.__init__(self, nombre, atrib, defecto, booleano, valores)


def listaAtributos():
    '''Devuelve la lista de observables de la base del conocimiento'''
    atributos = []
    atributos.append(numeroRuedas())
    atributos.append(PMA())
    atributos.append(edad())
    atributos.append(numeroAsientos())
    atributos.append(cilindrada())
    atributos.append(potencia())
    atributos.append(pesoRemolque())

    return atributos


class Caracteristica():
    '''Definición de una caracteristica genérica'''

    def __init__(self, nombre=None, valoresPermitidos=None, valor=None):
        self.nombre = nombre
        self.valor = valor
        self.valoresPermitidos = valoresPermitidos


'''Definición de características temperatura, precipitaciones y vegetacion'''


class NUMERORUEDAS(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'NumeroRuedas'
        valoresPermitidos = ['2', '3', '4']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class pma(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'PMA'
        valoresPermitidos = ['3500', '7500']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


class EDAD(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'edad'
        valoresPermitidos = ['15', '16', '18', '19', '20', '21', '24']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor

class NUMEROASIENTOS(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'NumeroAsientos'
        valoresPermitidos = ['1', '9', '17']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor

class CILINDRADA(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'cilindrada'
        valoresPermitidos = ['49', '50', '125']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor

class POTENCIA(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'potencia'
        valoresPermitidos = ['0', '15', '47']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor

class PESOREMOLQUE(Caracteristica):
    def __init__(self, valor=None):
        nombre = 'PesoRemolque'
        valoresPermitidos = ['0', '750']
        Caracteristica.__init__(self, nombre, valoresPermitidos, valor)
        self.valor = valor


def caracteristicas():
    '''Devuelve la lista de caracteristicas de la base de conocimiento'''
    obs = []
    obs.append(NUMERORUEDAS())
    obs.append(pma())
    obs.append(EDAD())
    obs.append(NUMEROASIENTOS())
    obs.append(CILINDRADA())
    obs.append(POTENCIA())
    obs.append(PESOREMOLQUE())
    return obs


def creaCaracteristica(tp):
    '''Crea una instancia de una caracteristica en el caso de que la tupla 
    coincida con la base de conocimiento'''
    if tp[0] == 'numeroRuedas':
        ob = NUMERORUEDAS(tp[1])
        return ob
    elif tp[0] == 'pma':
        ob = pma(tp[1])
        return ob
    elif tp[0] == 'edad':
        ob = EDAD(tp[1])
        # if tp[1] == 'True':
        #     ob.valor = True
        return ob
    elif tp[0] == 'numeroAsientos':
        ob = NUMEROASIENTOS(tp[1])
        return ob
    elif tp[0] == 'cilindrada':
        ob = CILINDRADA(tp[1])
        return ob
    elif tp[0] == 'potencia':
        ob = POTENCIA(tp[1])
        return ob
    elif tp[0] == 'pesoRemolque':
        ob = PESOREMOLQUE(tp[1])
        return ob
    return None


class Permiso():
    '''Definición genérica de un permiso'''

    def __init__(self, nombre):
        self.nombre = nombre


'''Definición de los permisos del sistema'''


class AM(Permiso):
    def __init__(self):
        nruedas = NUMERORUEDAS('2')
        edad = EDAD('15')
        cilindrada = CILINDRADA('50')
        self.debePresentar = [nruedas, edad, cilindrada]
        Permiso.__init__(self, nombre=u'AM')


class A(Permiso):
    def __init__(self):
        nruedas = NUMERORUEDAS('2')
        edad = EDAD('20')
        self.debePresentar = [nruedas, edad]
        Permiso.__init__(self, nombre=u'A')


class A1(Permiso):
    def __init__(self):
        nruedas = NUMERORUEDAS('2')
        edad = EDAD('16')
        cilindrada = CILINDRADA('125')
        potencia = POTENCIA('15')

        self.debePresentar = [nruedas, edad, cilindrada, potencia]
        Permiso.__init__(self, nombre=u'A1')


class A2(Permiso):
    def __init__(self):
        edad = EDAD('18')
        nruedas = NUMERORUEDAS('2')
        potencia = POTENCIA('47')

        self.debePresentar = [edad, nruedas, potencia]
        Permiso.__init__(self, nombre=u'A2')


class B(Permiso):
    def __init__(self):
        edad = EDAD('18')
        nasientos = NUMEROASIENTOS('9')
        pmA = pma('3500')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, nasientos, pmA, remolque]
        Permiso.__init__(self, nombre=u'B')


class C(Permiso):
    def __init__(self):
        edad = EDAD('21')
        pmA = pma('3500')
        nasientos = NUMEROASIENTOS('9')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, pmA, nasientos, remolque]
        Permiso.__init__(self, nombre=u'C')


class C1(Permiso):
    def __init__(self):
        edad = EDAD('18')
        pmA = pma('7500')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, pmA, remolque]
        Permiso.__init__(self, nombre=u'C1')


class D(Permiso):
    def __init__(self):
        edad = EDAD('24')
        nasientos = NUMEROASIENTOS('9')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, nasientos, remolque]
        Permiso.__init__(self, nombre=u'D')

class D1(Permiso):
    def __init__(self):
        edad = EDAD('21')
        nasientos = NUMEROASIENTOS('17')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, nasientos, remolque]
        Permiso.__init__(self, nombre=u'D1')

class E(Permiso):
    def __init__(self):
        edad = EDAD('18')
        remolque = PESOREMOLQUE('750')

        self.debePresentar = [edad, remolque]
        Permiso.__init__(self, nombre=u'E')


def hipotesis():
    '''Devuelve la lista de permisos'''
    am = AM()
    a = A()
    a1 = A1()
    a2 = A2()
    b = B()
    c = C()
    c1 = C1()
    d = D()
    d1 = D1()
    e = E()
    lHp = [am, a, a1, a2, b, c, c1, d, d1, e]
    return lHp
