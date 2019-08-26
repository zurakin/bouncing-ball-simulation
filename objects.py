import constantes
from math import pi

class Object():

    def __init__(self,x0,y0,mass,vx=0,vy=0,color='blue'):
        self.mass = mass
        self.x = x0
        self.y = y0
        self.vx = vx
        self.vy = vy
        self.ax=0
        self.ay=0
        self.color=color


    def apply_forces(self,forces):
        self.fx = []
        self.fy = []
        for f in forces:
                self.fx.append(f.x)
                self.fy.append(f.y)
                self.ax = sum(self.fx)/self.mass
                self.ay = sum(self.fy)/self.mass

    def delete(self,canvas):
        canvas.delete(self.image)

    def convert_pos(self):
        return (self.x * constantes.scale , self.y * constantes.scale)

    def convert_sp(self):
        return (self.vx * constantes.scale * constantes.tscale ,
         self.vy * constantes.scale * constantes.tscale)

    def move(self,canvas):
        canvas.move(self.image, self.convert_sp()[0], self.convert_sp()[1])


class Ball(Object):

    def __init__(self,r,x0,y0,mass,vx=0,vy=0,color='blue'):
        self.rayon = r
        self.volume = 4 * pi / 3 * r**3
        self.surface = 4 * pi * r**2
        Object.__init__(self,x0=x0,y0=y0,mass=mass,vx=vx,vy=vy,color=color)

    def insert(self,canvas):
        self.image = canvas.create_oval(
        self.convert_pos()[0]-self.rayon*constantes.scale,
        self.convert_pos()[1]-self.rayon*constantes.scale,
        self.convert_pos()[0]+self.rayon*constantes.scale,
        self.convert_pos()[1]+self.rayon*constantes.scale,
        fill=self.color)
    def update(self,canvas):
        self.vx = self.ax * constantes.tscale + self.vx
        self.vy = self.ay * constantes.tscale + self.vy
        self.y = constantes.rconvert(canvas.coords(self.image)[1])+self.rayon
        self.x = constantes.rconvert(canvas.coords(self.image)[0])+self.rayon

    def check_collision_y(self):
        return self.y >= constantes.hval-self.rayon and self.vy >= 0

    def check_collision_x(self):
        return ( self.x >= constantes.width * constantes.hval / constantes.height -
        self.rayon and ball.vx >= 0 ) or ( self.x <= 0 + self.rayon
        and self.vx <= 0 )

    def check_stable(self):
        return -0.5 <= self.vy <= 0.5 and self.y >= constantes.hval-self.rayon*1.1
