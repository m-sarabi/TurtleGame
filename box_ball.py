import random
import time
import turtle
import drawings

# for playing sounds
try:
    import winsound


    def play_sound(sound):
        winsound.PlaySound(sound, winsound.SND_ASYNC)
except ImportError:
    try:
        import pygame


        def play_sound(sound):
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

    except ImportError:
        screen = turtle.Screen()
        screen.setup(400, 300)
        turtle.bgcolor('black')
        turtle.hideturtle()
        turtle.speed(0)
        turtle.penup()
        turtle.pencolor('white')
        turtle.goto(-20, -20)
        turtle.write('You need to install playsound:\n\n       pip install pygame', False, align='center',
                     font=('Arial', 14, 'normal'))
        turtle.done()
        quit()


def shape_maker(points, colors, name):
    shape = turtle.Shape('compound')
    for i, path in enumerate(points):
        points = path + [path[0]]
        shape.addcomponent(points, colors[i])
    screen.register_shape(name, shape)


class PlayGame:
    def __init__(self):
        self.wait_time = 0.05
        self.spawn_rate = 2.1
        self.initial_time = 30
        self.extra_time = self.initial_time
        self.started = False
        self.finished = False
        self.scores = 0
        self.last_ball = (None, None)
        self.t = time.time()
        self.ball_t = time.time()
        self.first_tick = time.time()
        self.start_btn = turtle.Turtle()
        self.start_btn.hideturtle()
        self.play_again_btn = turtle.Turtle()
        self.play_again_btn.hideturtle()
        self.high_score = 0

        turtle.listen()
        turtle.onkey(be_done, 'Escape')
        turtle.onkeypress(self.up, "Up")
        turtle.onkeypress(self.up, "w")
        turtle.onkeypress(self.down, "Down")
        turtle.onkeypress(self.down, "s")
        turtle.onkeypress(self.left, "Left")
        turtle.onkeypress(self.left, "a")
        turtle.onkeypress(self.right, "Right")
        turtle.onkeypress(self.right, "d")
        turtle.onkey(self.start, 'space')
        turtle.onscreenclick(self.click_events)
        timer_board.write(f'Time: {self.initial_time}', False, font=('Arial', 14, 'normal'))
        self.new_game()

    def score_check(self):
        if len(balls) > 0:
            box_pos = (int(box.xcor()), int(box.ycor()))
            ball_pos = (balls[-1].xcor(), balls[-1].ycor())
            if box_pos == ball_pos and ball_pos != self.last_ball:
                self.last_ball = ball_pos
                self.scores += 1
                play_sound('sounds/eat.wav')
                sc_board.clear()
                sc_board.write(f'Score: {self.scores}', False, font=('Arial', 14, 'normal'))
                balls[0].hideturtle()
                balls[0].clear()
                self.extra_time += 1.6
                del balls[0]
                if self.scores > self.high_score:
                    self.high_score = self.scores
                    hs_board.clear()
                    hs_board.write(f'High Score: {self.scores}', False, font=('Arial', 14, 'normal'))

    def move(self, x, y):
        if self.finished is True:
            return
        box_pos = (box.xcor(), box.ycor())
        new_pos = [box_pos[0] + x, box_pos[1] + y]
        if new_pos[0] > 350:
            new_pos[0] = -350
        if new_pos[0] < -350:
            new_pos[0] = 350
        if new_pos[1] > 250:
            new_pos[1] = -300
        if new_pos[1] < -300:
            new_pos[1] = 250
        box.goto(new_pos[0], new_pos[1])
        self.score_check()

    def right(self):
        t2 = time.time()
        if t2 - self.t < self.wait_time:
            return
        self.t = time.time()
        box.shape(image_right)
        self.move(50, 0)

    def up(self):
        t2 = time.time()
        if t2 - self.t < self.wait_time:
            return
        self.t = time.time()
        box.shape(image_up)
        self.move(0, 50)

    def left(self):
        t2 = time.time()
        if t2 - self.t < self.wait_time:
            return
        self.t = time.time()
        box.shape(image_left)
        self.move(-50, 0)

    def down(self):
        t2 = time.time()
        if t2 - self.t < self.wait_time:
            return
        self.t = time.time()
        box.shape(image_down)
        self.move(0, -50)

    def draw_ball(self):
        while len(balls) > 0:
            balls[0].hideturtle()
            balls[0].clear()
            del balls[0]
        balls.append(turtle.Turtle(visible=False))
        balls[-1].shape('apple')
        balls[-1].shapesize(0.4, 0.4)
        balls[-1].left(90)
        balls[-1].penup()
        balls[-1].speed(0)
        balls[-1].setx(random.randint(-350 // 50, 350 // 50) * 50)
        balls[-1].sety(random.randint(-300 // 50, 250 // 50) * 50)
        balls[-1].showturtle()
        self.last_ball = (None, None)

    def ball_process(self):
        now = time.time()
        if now - self.ball_t >= self.spawn_rate or balls == []:
            self.draw_ball()
            self.ball_t = now
        timer_board.clear()
        timer = self.extra_time - (now - self.first_tick)
        timer_board.write(f'Time: {max([0, round(timer, 1)])}', False, font=('Arial', 14, 'normal'))
        if timer > 0:
            screen.ontimer(self.ball_process, 10)
        if timer <= 0:
            self.finished = True
            self.game_over()
        screen.update()

    def click_events(self, x, y):
        if -50 < x < 50 and -20 < y < 20 and self.started is False and self.finished is False:
            self.start()
        if -75 < x < 75 and -25 < y < 25 and self.started is False and self.finished is True:
            self.play_again_btn.clear()
            turtle.update()
            self.new_game()

    def start(self):
        self.started = True
        self.start_btn.clear()
        box.showturtle()
        self.first_tick = time.time()
        self.ball_process()

    def game_over(self):
        self.started = False

        # play again button
        self.play_again_btn.speed(0)
        self.play_again_btn.pensize(2)
        self.play_again_btn.color('black', 'darkred')
        self.play_again_btn.penup()
        self.play_again_btn.goto(-75, -25)
        self.play_again_btn.begin_fill()
        self.play_again_btn.pendown()
        self.play_again_btn.forward(150)
        self.play_again_btn.left(90)
        self.play_again_btn.forward(50)
        self.play_again_btn.left(90)
        self.play_again_btn.forward(150)
        self.play_again_btn.left(90)
        self.play_again_btn.forward(50)
        self.play_again_btn.left(90)
        self.play_again_btn.penup()
        self.play_again_btn.end_fill()
        self.play_again_btn.hideturtle()
        self.play_again_btn.speed(0)
        self.play_again_btn.pencolor('white')
        self.play_again_btn.goto(-69, -14)
        self.play_again_btn.write('Play Again', False, font=('Arial', 20, 'bold'))

    def new_game(self):
        box.goto(0, 0)
        box.shape(image_up)
        while len(balls) > 0:
            balls[0].hideturtle()
            balls[0].clear()
            del balls[0]
        box.hideturtle()
        self.extra_time = self.initial_time
        self.started = False
        self.finished = False
        self.scores = 0
        self.last_ball = (None, None)

        self.start_btn = turtle.Turtle()
        self.start_btn.speed(0)
        self.start_btn.pensize(2)
        self.start_btn.color('black', 'darkgreen')
        self.start_btn.penup()
        self.start_btn.goto(-50, -20)
        self.start_btn.begin_fill()
        self.start_btn.pendown()
        self.start_btn.forward(100)
        self.start_btn.left(90)
        self.start_btn.forward(40)
        self.start_btn.left(90)
        self.start_btn.forward(100)
        self.start_btn.left(90)
        self.start_btn.forward(40)
        self.start_btn.left(90)
        self.start_btn.penup()
        self.start_btn.end_fill()
        self.start_btn.hideturtle()
        self.start_btn.speed(0)
        self.start_btn.pencolor('white')
        self.start_btn.goto(-28, -14)
        self.start_btn.write('Start', False, font=('Arial', 18, 'bold'))
        sc_board.clear()
        sc_board.write('Score: 0', False, font=('Arial', 14, 'normal'))
        turtle.update()


def be_done():
    turtle.bye()


screen = turtle.Screen()
screen.setup(800, 700)
turtle.bgcolor('lightblue')
# turtle.screensize(600, 600, 'lightblue')
turtle.resetscreen()
screen.cv._rootwindow.resizable(False, False)
turtle.tracer(0, 0)

balls = []

# drawing a border
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-382, -330)
border.fillcolor('skyblue')
border.begin_fill()
dist = 760
dash = True
while dist > 0:
    if dash:
        border.pendown()
    else:
        border.penup()
    dash = not dash
    border.forward(min([dist, 10]))
    dist -= 10
dist = 610
dash = True
border.left(90)
while dist > 0:
    if dash:
        border.pendown()
    else:
        border.penup()
    dash = not dash
    border.forward(min([dist, 10]))
    dist -= 10
dist = 760
dash = True
border.left(90)
while dist > 0:
    if dash:
        border.pendown()
    else:
        border.penup()
    dash = not dash
    border.forward(min([dist, 10]))
    dist -= 10
dist = 610
dash = True
border.left(90)
while dist > 0:
    if dash:
        border.pendown()
    else:
        border.penup()
    dash = not dash
    border.forward(min([dist, 10]))
    dist -= 10
border.end_fill()

sc_board = turtle.Turtle()
sc_board.hideturtle()
sc_board.speed(0)
sc_board.penup()
sc_board.goto(-380, 300)
sc_board.write('Score: 0', False, font=('Arial', 14, 'normal'))

# high score board
hs_board = turtle.Turtle()
hs_board.hideturtle()
hs_board.speed(0)
hs_board.penup()
hs_board.goto(-60, 300)
hs_board.write('High Score: 0', False, font=('Arial', 14, 'normal'))

timer_board = turtle.Turtle()
timer_board.hideturtle()
timer_board.speed(0)
timer_board.penup()
timer_board.goto(300, 300)

box = turtle.Turtle()
box.hideturtle()
box.speed(0)
box.pensize(3)
box.pencolor('blue')
box.fillcolor('yellow')

image_up = 'images/turtle-up.gif'
image_right = 'images/turtle-right.gif'
image_left = 'images/turtle-left.gif'
image_down = 'images/turtle-down.gif'
screen.addshape(image_up)
screen.addshape(image_right)
screen.addshape(image_left)
screen.addshape(image_down)
box.shape(image_up)
box.shapesize(2, 2)
box.penup()

shape_maker(drawings.apple_points, drawings.apple_colors, 'apple')

screen.update()

game = PlayGame()

turtle.Screen().mainloop()
