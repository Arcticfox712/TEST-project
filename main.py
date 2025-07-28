import pgzrun
HEIGHT=500
WIDTH=500

def draw():
    r=250
    g=100
    b=150
    width=WIDTH-100
    hight=HEIGHT-150

    rect=Rect((0,0), (width, hight))
    rect.center=250,250
    screen.draw.rect(rect,(r,g,b))

pgzrun.go()

    











