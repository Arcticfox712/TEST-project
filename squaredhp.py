import pgzrun
import random
HEIGHT=500
WIDTH=500


def draw():
 for i in range (10):
    r=random.randint(0, 250)
    g=random.randint(0, 250)
    b=random.randint(0, 250)
    width=WIDTH - random.randint(50, 400)
    hight=HEIGHT - random.randint(50, 400)

    rect=Rect((0,0), (width, hight))
    rect.center=250,250
    screen.draw.rect(rect,(r,g,b))

pgzrun.go()

    

