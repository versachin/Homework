import turtle








turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Traffic Turtle")
wn.bgcolor("lightgreen")
grotto = turtle.Turtle()

def draw_housing(grotto):
    grotto.pensize(3)
    grotto.color("black","darkgrey")
    grotto.begin_fill()
    grotto.forward(80)
    grotto.left(90)
    grotto.forward(200)
    grotto.circle(40, 180)
    grotto.forward(200)
    grotto.left(90)
    grotto.end_fill()

draw_housing(grotto)


