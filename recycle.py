import random
import pgzrun

WIDTH=800
HEIGHT=600
TITLE= "recycle paper bag"

paper = Actor("paperimg")
paper.pos = (400,100)

def draw():
    screen.blit("bground",(0,0))

    paper.draw()

def update():
    paper.y += 2

def on_mouse_down(pos):
    if paper.collidepoint(pos):
        print("You clicked paper")
        
pgzrun.go()