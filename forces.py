import constantes

class Constant_force():
    def __init__(self,object,fx,fy):
        self.object = object
        self.x = fx
        self.y = fy

class Poids(Constant_force):
    def __init__(self,object):
        Constant_force.__init__(self,object,fx=0,fy=constantes.g*object.mass)

class Friction_sphere():
    def __init__(self,object):
        self.object = object
        self.x = -constantes.Cx * 1/2 * constantes.p * object.vx**2 * (object.surface/2)
        self.y = -constantes.Cx * 1/2 * constantes.p * object.vy**2 * (object.surface/2)
