#snake game


import turtle
import time
import random




delay = 0.1


score = 0
high_score = 0


#schermo di gioco


wn = turtle.Screen()
wn.title("Snake Game for POLPETTINA")
wn.bgcolor("green")
wn.setup(width=600 , height=600)
wn.tracer(0)


#testa del serpente


head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


# cibo


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


corpo = []




# conteggio punti

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0 , 260)
pen.write("Score: 0  High Score = 0" , align="center" , font=("Courier", 24 , "normal"))



# movimento


def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

    if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

    if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)





# connessione comandi di gioco

 
wn.listen()
wn.onkeypress(go_up , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_right , "d")
wn.onkeypress(go_left , "a")



#main loop


while True:
    wn.update()

    


    # controllo collisioni

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for pezzi in corpo:
            pezzi.goto(1000, 1000)
        corpo.clear()
        score = 0


    # mecchanica del cibo che viene mangiato

    if head.distance(food) < 20:
        x = random.randint(-290 , 250)
        y = random.randint(-290 , 290)
        food.goto(x,y)

        nuovocorpo = turtle.Turtle()
        nuovocorpo.speed(0)
        nuovocorpo.shape("square")
        nuovocorpo.color("orange")
        nuovocorpo.penup()
        corpo.append(nuovocorpo)

        score +=10

        if score  > high_score:
            high_score = score
        pen.clear()
        pen.write(" Score: {}  High Score: {}".format(score, high_score), align="center" , font=("Courier", 24 , "normal"))
             

    #ancoraggio corpo alla testa 

    for i in range(len(corpo)-1 , 0 , -1):
        x = corpo[i -1].xcor()
        y = corpo[i - 1].ycor()
        corpo[i].goto(x,y)

    if len(corpo) > 0:
        x = head.xcor()
        y = head.ycor()
        corpo[0].goto(x,y)
        

    

    move()


    # controllo collisioni con corpo

    for pezzi in corpo:
        if pezzi.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for pezzi in corpo:
                pezzi.goto(1000, 1000)
            corpo.clear()
            score = 0
            


    time.sleep(delay)


wn.mainloop()


