import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Traffic Turtle")
wn.bgcolor("lightgreen")
grotto = turtle.Turtle()

def draw_housing():
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

draw_housing()

grotto.penup()
grotto.forward(40)
grotto.left(90)
grotto.forward(50)
grotto.shape("circle")
grotto.shapesize(3)
grotto.fillcolor("green")

state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:
        grotto.forward(70)
        grotto.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine, 500)
    elif state_num == 1:
        grotto.forward(70)
        grotto.fillcolor("red")
        wn.ontimer(advance_state_machine, 3000)
        state_num = 2
    else:
        grotto.back(140)
        grotto.fillcolor("green")
        wn.ontimer(advance_state_machine, 3000)
        state_num = 0
advance_state_machine()


wn.listen()
wn.mainloop()
