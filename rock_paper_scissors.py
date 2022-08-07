import random
import time
import turtle


def screen_click(x, y):
    global run_check
    if not run_check:
        return
    run_check = False
    ch = None
    if -125 < x < -75 and -200 < y < -175:
        ch = 0
    elif -25 < x < 25 and -200 < y < -175:
        ch = 1
    elif 75 < x < 125 and -200 < y < -175:
        ch = 2
    if ch is not None:
        plays.append(ch)
        if len(plays) <= 3:
            plays.append(random.randint(0, 2))
        elif 3 < len(plays) < 11:
            if result(plays[-3], plays[-2]) == 'lose':
                if plays[-3] == 0:
                    plays.append(random.choice([0, 0, 0, 1, 2, 2, 2]))
                elif plays[-3] == 1:
                    plays.append(random.choice([0, 0, 0, 1, 1, 1, 2]))
                else:
                    plays.append(random.choice([0, 1, 1, 1, 2, 2, 2]))
            else:
                plays.append(random.randint(0, 2))
        else:
            pat_find = find_pattern(plays[-11:-1], plays[:-1])
            if pat_find is None:
                pat_find = find_pattern(plays[-9:-1], plays[:-1])
            if pat_find is None:
                pat_find = find_pattern(plays[-7:-1], plays[:-1])
            if pat_find is None:
                pat_find = find_pattern(plays[-5:-1], plays[:-1])
            if pat_find is None:
                if result(plays[-3], plays[-2]) == 'lose':
                    if plays[-3] == 0:
                        plays.append(random.choice([0, 0, 0, 1, 2, 2, 2]))
                    elif plays[-3] == 1:
                        plays.append(random.choice([0, 0, 0, 1, 1, 1, 2]))
                    else:
                        plays.append(random.choice([0, 1, 1, 1, 2, 2, 2]))
                else:
                    plays.append(random.randint(0, 2))
            else:
                plays.append(pat_find)
        pc_choice.clear()
        pc_choice.write('Rock' if plays[-1] == 0 else 'Paper' if plays[-1] == 1 else 'Scissors',
                        align='center', font=('Arial', 20, 'bold'))
        res = result(plays[-2], plays[-1])
        if res == 'win':
            scores[0] += 1
            hu_score.clear()
            hu_score.write(f'{scores[0]}', align='center', font=('Arial', 20, 'normal'))
        elif res == 'lose':
            scores[1] += 1
            pc_score.clear()
            pc_score.write(f'{scores[1]}', align='center', font=('Arial', 20, 'normal'))
        print(result(plays[-2], plays[-1]))
        time.sleep(1)
        run_check = True


def result(h, p):
    if h == p:
        return 'draw'
    if h == 0:
        if p == 1:
            return 'lose'
        else:
            return 'win'
    elif h == 1:
        if p == 2:
            return 'lose'
        else:
            return 'win'
    else:
        if p == 0:
            return 'lose'
        else:
            return 'win'


def find_pattern(pat, all_list):
    results = []
    for i in range(len(all_list) - len(pat)):
        if all_list[i:i + len(pat)] == pat:
            results.append(all_list[i + len(pat)])

    if not results:
        return None

    results_dict = {}
    for i in results:
        if i in results_dict:
            results_dict[i] += 1
        else:
            results_dict[i] = 1
    max_c = max(list(results_dict.values()))
    for i in list(results_dict.keys()):
        if results_dict[i] < max_c:
            del results_dict[i]

    h_choice = random.choice(list(results_dict.keys()))
    if h_choice == 0:
        return 1
    elif h_choice == 1:
        return 2
    else:
        return 0


scores = [0, 0]
plays = []
run_check = True

screen = turtle.Screen()
screen.screensize(600, 600, 'gainsboro')
turtle.hideturtle()

rock = turtle.Turtle()
paper = turtle.Turtle()
scissors = turtle.Turtle()
frame = turtle.Turtle()

general_text = turtle.Turtle()
general_text.hideturtle()
pc_choice = turtle.Turtle()
pc_choice.hideturtle()
pc_score = turtle.Turtle()
pc_score.hideturtle()
hu_score = turtle.Turtle()
hu_score.hideturtle()

frame.speed('fastest')
frame.hideturtle()
frame.pensize(2)
frame.pencolor('light gray')
frame.fillcolor('white')
frame.penup()
frame.goto(-133, -212)
frame.pendown()
frame.begin_fill()
frame.forward(270)
frame.left(90)
frame.forward(45)
frame.left(90)
frame.forward(270)
frame.left(90)
frame.forward(45)
frame.left(90)
frame.end_fill()
frame.penup()
frame.goto(-135, -210)
frame.pencolor('dim gray')
frame.pendown()
frame.forward(270)
frame.left(90)
frame.forward(45)
frame.left(90)
frame.forward(270)
frame.left(90)
frame.forward(45)
frame.left(90)
frame.penup()

frame.pencolor('light gray')
frame.goto(-358, 198)
frame.pendown()
frame.begin_fill()
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.penup()
frame.end_fill()
frame.goto(-360, 150)
frame.pendown()
frame.forward(160)
frame.penup()
frame.pencolor('dim gray')
frame.goto(-360, 200)
frame.pendown()
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.penup()
frame.goto(-360, 150)
frame.pendown()
frame.forward(160)
frame.penup()

frame.pencolor('light gray')
frame.goto(202, 198)
frame.pendown()
frame.begin_fill()
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.penup()
frame.end_fill()
frame.goto(200, 150)
frame.pendown()
frame.forward(160)
frame.penup()
frame.pencolor('dim gray')
frame.goto(200, 200)
frame.pendown()
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.forward(160)
frame.right(90)
frame.penup()
frame.goto(200, 150)
frame.pendown()
frame.forward(160)
frame.penup()

rock.speed('fastest')
rock.hideturtle()
rock.pensize(3)
rock.pencolor('darkgreen')
rock.fillcolor('darkgreen')
rock.penup()
rock.goto(-125, -200)
rock.begin_fill()
rock.pendown()
rock.forward(50)
rock.left(90)
rock.forward(25)
rock.left(90)
rock.forward(50)
rock.left(90)
rock.forward(25)
rock.end_fill()
rock.penup()
rock.backward(5)
rock.left(90)
rock.forward(12)
rock.pencolor('white')
rock.write('Rock', font=('Arial', 10, 'normal'))

paper.speed('fastest')
paper.hideturtle()
paper.pensize(3)
paper.pencolor('darkgreen')
paper.fillcolor('darkgreen')
paper.penup()
paper.goto(-25, -200)
paper.begin_fill()
paper.pendown()
paper.forward(50)
paper.left(90)
paper.forward(25)
paper.left(90)
paper.forward(50)
paper.left(90)
paper.forward(25)
paper.end_fill()
paper.penup()
paper.backward(5)
paper.left(90)
paper.forward(10)
paper.pencolor('white')
paper.write('Paper', font=('Arial', 10, 'normal'))

scissors.speed('fastest')
scissors.hideturtle()
scissors.pensize(3)
scissors.pencolor('darkgreen')
scissors.fillcolor('darkgreen')
scissors.penup()
scissors.goto(75, -200)
scissors.begin_fill()
scissors.pendown()
scissors.forward(50)
scissors.left(90)
scissors.forward(25)
scissors.left(90)
scissors.forward(50)
scissors.left(90)
scissors.forward(25)
scissors.end_fill()
scissors.penup()
scissors.backward(5)
scissors.left(90)
scissors.forward(1)
scissors.pencolor('white')
scissors.write('Scissors', font=('Arial', 10, 'normal'))

general_text.pensize(5)
general_text.speed('fastest')
general_text.penup()
general_text.goto(0, 200)
general_text.write('AI Choice:', align='center', font=('Arial', 24, 'normal'))
general_text.goto(-280, 160)
general_text.write('AI Score:', align='center', font=('Arial', 20, 'normal'))
general_text.goto(280, 160)
general_text.write('Your Score:', align='center', font=('Arial', 20, 'normal'))

pc_choice.penup()
pc_choice.goto(0, 100)

pc_score.penup()
pc_score.goto(-280, 80)
pc_score.write('0', align='center', font=('Arial', 20, 'normal'))

hu_score.penup()
hu_score.goto(280, 80)
hu_score.write('0', align='center', font=('Arial', 20, 'normal'))

turtle.onscreenclick(screen_click)
screen.mainloop()
