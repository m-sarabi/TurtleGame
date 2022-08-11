import random
import time
import turtle

wait_time = 0.05
scores = 0
last_ball = (None, None)
t = time.time()
ball_t = time.time()
first_tick = time.time()
spawn_time = 3.5
extra_time = 8
started = False
turtle.tracer(0, 0)
finished = False


def score_check():
    global scores, last_ball, extra_time
    if len(balls) > 0:
        box_pos = (int(box.xcor()), int(box.ycor()))
        ball_pos = (balls[-1].xcor(), balls[-1].ycor())
        if box_pos == ball_pos and ball_pos != last_ball:
            last_ball = ball_pos
            scores += 1
            sc_board.clear()
            sc_board.write(f'Score: {scores}', False, font=('Arial', 14, 'normal'))
            balls[0].hideturtle()
            balls[0].clear()
            extra_time += 2.5
            del balls[0]


def move(x, y):
    if finished is True:
        return
    box_pos = (box.xcor(), box.ycor())
    new_pos = [box_pos[0] + x, box_pos[1] + y]
    if new_pos[0] > 350:
        new_pos[0] = -350
    if new_pos[0] < -350:
        new_pos[0] = 350
    if new_pos[1] > 300:
        new_pos[1] = -300
    if new_pos[1] < -300:
        new_pos[1] = 300
    box.goto(new_pos[0], new_pos[1])
    score_check()


def right():
    global t
    t2 = time.time()
    if t2 - t < wait_time:
        return
    t = time.time()
    move(50, 0)


def up():
    global t
    t2 = time.time()
    if t2 - t < wait_time:
        return
    t = time.time()
    move(0, 50)


def left():
    global t
    t2 = time.time()
    if t2 - t < wait_time:
        return
    t = time.time()
    move(-50, 0)


def down():
    global t
    t2 = time.time()
    if t2 - t < wait_time:
        return
    t = time.time()
    move(0, -50)


def draw_ball():
    global last_ball
    while len(balls) > 0:
        balls[0].hideturtle()
        balls[0].clear()
        del balls[0]
    balls.append(turtle.Turtle(visible=False))
    balls[-1].shape('circle')
    balls[-1].color('red', 'red')
    balls[-1].penup()
    balls[-1].speed(0)
    balls[-1].setx(random.randint(-300 // 50, 300 // 50) * 50)
    balls[-1].sety(random.randint(-300 // 50, 300 // 50) * 50)
    balls[-1].showturtle()
    last_ball = (None, None)


def ball_process():
    global ball_t, spawn_time, extra_time, finished
    now = time.time()
    if now - ball_t >= spawn_time or balls == []:
        draw_ball()
        ball_t = now
        spawn_time = (0.95 ** ((now - first_tick) // 10)) * 5
    timer_board.clear()
    timer = extra_time - (now - first_tick)
    timer_board.write(f'Time: {max([0, round(timer, 1)])}', False, font=('Arial', 14, 'normal'))
    if timer > 0:
        screen.ontimer(ball_process, 50)
    if timer <= 0:
        finished = True
    screen.update()


def start(x, y):
    global started, first_tick
    if -50 < x < 50 and -20 < y < 20 and started is False:
        started = True
        start_btn.clear()
        box.showturtle()
        first_tick = time.time()
        ball_process()


def be_done():
    turtle.bye()


screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
turtle.screensize(600, 600, 'lightblue')

balls = []

sc_board = turtle.Turtle()
sc_board.hideturtle()
sc_board.speed(0)
sc_board.penup()
sc_board.goto(-380, 300)
sc_board.write('Score: 0', False, font=('Arial', 14, 'normal'))

timer_board = turtle.Turtle()
timer_board.hideturtle()
timer_board.speed(0)
timer_board.penup()
timer_board.goto(270, 300)
timer_board.write(f'Time: {extra_time}', False, font=('Arial', 14, 'normal'))

box = turtle.Turtle()
box.hideturtle()
box.speed(0)
box.pensize(3)
box.pencolor('blue')
box.fillcolor('yellow')

box.shape('square')
box.penup()
box.goto(0, 0)

turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(up, "w")
turtle.onkey(down, "Down")
turtle.onkey(down, "s")
turtle.onkey(left, "Left")
turtle.onkey(left, "a")
turtle.onkey(right, "Right")
turtle.onkey(right, "d")
turtle.onkey(be_done, 'Escape')

turtle.tracer(0)
start_btn = turtle.Turtle()
start_btn.speed(0)
start_btn.pensize(2)
start_btn.color('black', 'darkgreen')
start_btn.penup()
start_btn.begin_fill()
start_btn.goto(-50, -20)
start_btn.pendown()
start_btn.forward(100)
start_btn.left(90)
start_btn.forward(40)
start_btn.left(90)
start_btn.forward(100)
start_btn.left(90)
start_btn.forward(40)
start_btn.left(90)
start_btn.penup()
start_btn.end_fill()
start_btn.hideturtle()
start_btn.speed(0)
start_btn.pencolor('white')
start_btn.goto(-28, -14)
start_btn.write('Start', False, font=('Arial', 18, 'bold'))

screen.update()
turtle.onscreenclick(start)

turtle.Screen().mainloop()
