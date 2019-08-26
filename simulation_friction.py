import tkinter
import time
from objects import *
from forces import *
import constantes


window = tkinter.Tk()
window.title('simulation chute libre')


##create canvas
canvas = tkinter.Canvas(window,width=constantes.width,height=constantes.height)
canvas.grid()


def start():
    ##create ball
    ball = Ball(r=0.1,x0=6,y0=0,mass=2,vx=0,vy=0,color='sky blue')
    ball.insert(canvas=canvas)

    ball2 = Ball(r=0.5,x0=5,y0=0,mass=2,vx=0,vy=0,color='grey')
    ball2.insert(canvas=canvas)

    while True:
        ##apply a force on the ball
        ball.apply_forces([Poids(ball), Friction_sphere(ball)])
        ball2.apply_forces([Poids(ball2), Friction_sphere(ball2)])

        ##move the ball
        ball.move(canvas)
        ball2.move(canvas)
        '''to remember pos object is a list like this Pos[left,top,right,bottom]'''

        ##change movement on collision
        if ball.check_collision_y():
            print('ball1 hit the ground at a speed of {} m/s'.format(ball.vy))
            ball.vy = -ball.vy*0.8

        if ball.check_collision_x():
            ball.vx = -ball.vx*0.8


        if ball2.check_collision_y():
            print('ball2 hit the ground at a speed of {} m/s'.format(ball2.vy))
            ball2.vy = -ball2.vy*0.8

        if ball2.check_collision_x():
            ball2.vx = -ball2.vx*0.8

        window.update()
        ##stop moving if ball almost stable
        if ball.check_stable():
            print('ball1 has stopped moving')
            break
        if ball2.check_stable():
            print('ball2 has stopped moving')
            break

        ##update the speed of the Ball
        ball.update(canvas)
        ball2.update(canvas)
        time.sleep(constantes.tscale)
    #window.destroy()

Bstart=tkinter.Button(window,text='Start simulation',command=start)
Bstart.grid(row=1,column=0)

window.mainloop()
