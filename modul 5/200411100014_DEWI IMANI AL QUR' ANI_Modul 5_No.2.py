import turtle

d=turtle
d.pen()
box=turtle.Screen()
d.speed(5)

def fraktal(panjang, level):
    if level == 0:
        d.forward(panjang/2)
        d.right(180)
        d.forward(panjang)
        d.right(180)
        d.forward(panjang/2)
        d.right(90)
        d.forward(panjang/2)
        d.right(180)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang/2)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang/2)
    else:
        d.forward(panjang/2)
        d.right(180)
        d.forward(panjang)
        d.right(180)
        d.forward(panjang/2)
        d.right(90)
        d.forward(panjang/2)
        d.right(180)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang/2)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang)
        d.right(90)
        d.forward(panjang/2)
        d.right(90)
        d.forward(panjang/4)
        d.right(90)
        d.forward(panjang/4)
        d.right(180)
        fraktal(panjang/2, level-1)
        
fraktal(400,4)