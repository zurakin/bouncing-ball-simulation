##constantes

g=10

##scale choice
width = 800
height = 600
hval = 10   #how long is the canvas irl
tscale = 1/60  #time scale
scale = height/hval   #distance scale


'''
parametres de frottement
formule:
    si 0 < v < 4m/s : F = n k v
    si 5 < v < 20m/s  :   F=-Cx * 1/2 * p * v**2 * S
    k = coefficient caractéristique de la géométrie du solide   k=6*Pi R (pour boule de rayon R)
    n= coefficient de viscosité du fluide (dépend de la température)
    F : force de frottement
    Cx : coefficient de traînée caractérisant la géométrie du solide(sans unité)
        disque: Cx =1.32
        boule: Cx = 0.45
        demi-boule+cône: Cx = 0.04
    S = aire du solide selon direction perpendiculaire à la vitesse
    P= masse volumique du fluide
        pour l'air : 1,225 kg/m3 à 15 °C

    source : https://owl-ge.ch/IMG/pdf/frottement.pdf
'''

p = 1.225
Cx = 0.45

def rconvert(pixels):
    return pixels/scale
