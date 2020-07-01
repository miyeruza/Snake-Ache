from turtle import *
import time
import random

def _set_window():    
    pantalla = Screen()
    pantalla = title("Snake Ache")
    pantalla = bgcolor("black")
    pantalla = setup(700, 700)
    onkeypress(righty, "Right")
    onkeypress(lefty, "Left")
    listen()
    
def snake_start(color):
    
    global snake

    snake = Turtle()
    snake.penup()
    snake.color(color)
    snake.shape("circle")
    snake.shapesize(.45)
    snake.pensize(10)
    snake.speed(0)

#colocamos las cualidades de cada tortuga, como forman el marco para jugar todas tienen las mismas cualidades.

def _set_turtle_frame(frames:Turtle):

    frames.hideturtle()
    frames.speed(0)
    frames.color("blue")
    frames.shape("square")
    frames.pensize(10)
    frames.penup()
    
    return frames


def draw_frame(marco1:Turtle,marco2:Turtle,marco3:Turtle,marco4:Turtle):

    #movemos cada tortuga a el punto donde empezarán su recorrido

    marco1.goto(0,250)
    marco2.goto(0,250)
    marco3.goto(0,-250)
    marco4.goto(0,-250)
    
    #empezamos a dibujar el marco

    marco1.pendown()
    marco2.pendown()
    marco3.pendown()
    marco4.pendown()
    
    for i in range(15):
        marco1.goto(-20*i,250) 
        marco2.goto(20*i,250)
        marco3.goto(-20*i,-250)
        marco4.goto(20*i,-250)
    
    for i in range(14):
        marco1.sety(250-20*i)
        marco2.sety(250-20*i)
        marco3.sety(-250+20*i)
        marco4.sety(-250+20*i)


def _food():

    global food
    food = Turtle()
    food.hideturtle()
    food.penup()
    food.color("red")
    food.shape("square")
    food.turtlesize(0.5)
    food.goto(random.randint(-268,268),random.randint(-238,238))
    food.showturtle()


def _score(score):
    
    global num_score

    num_score = Turtle()
    num_score.speed(0)
    num_score.shape("square")
    num_score.color("white")
    num_score.penup()
    num_score.hideturtle()
    num_score.goto(0,250)
    num_score.write("Score: {}".format(score), align="center", font=("courier","24","normal"))
  
def kill_snake():
    
    global snake, score, snakebody
    
    score = 0
    num_score.reset()
    snake.goto(0,0)
    _score(score)

    for bodypart in snakebody:
        bodypart.reset()
        bodypart.goto(300,300)

    snakebody.clear()
    react_time = 0.1

def lefty():
    snake.left(90)

def righty():
    snake.right(90)

def forwy():
   
    snake.forward(11)

if __name__ == "__main__":

    #Iniciamos la pantalla
    _set_window()

    #Iniciamos la serpiente
    snake_start("white")
    
    snakebody = []

    #creamos un marco con cuatro tortugas para hacer una animación bonita
    frame1 = Turtle()
    frame2 = Turtle()
    frame3 = Turtle()
    frame4 = Turtle()

    #cada argumento es una función que configura cada tortuga y dibuja con ellas el tablero

    draw_frame(_set_turtle_frame(frame1),_set_turtle_frame(frame2),_set_turtle_frame(frame3),_set_turtle_frame(frame4))
    
    #puntuación inicial y marcador
    score = 0
    _score(score)
    
    #pone el primer plato de comida
    _food()
   
    abort = 0

    react_time = 0.1
    
    #es el loop principal
    while True:
        abort +=1

        forwy()
        

        if snake.xcor() >= 270 or snake.xcor() <= -270:

            kill_snake()


        if snake.ycor() >= 240 or snake.ycor() <= -240:
            
            kill_snake()


        #revisa si la serpiente está comiendo

        if snake.distance(food) < 11:

            food.reset()
            num_score.reset()
            _food()
            score += 1
            _score(score)

        #si la serpiente come, crece, además disminuye el tiempo de reacción

            body = Turtle()
            body.penup()
            body.shape("square")
            body.color("white")
            body.shapesize(.45)
            body.speed(0)
            snakebody.append(body)
        
        #acelera la serpiente, por alguna razón cada vez va mas lento
        #imagino que se debe a la forma en que se crea el cuerpo, hay que corregirlo

            if score <= 10:
                react_time = react_time - react_time*score/10
            else:
                react_time = react_time - react_time*0.5

        
        #el cuerpo de la serpiente se mueve junto con la cabeza

        if len(snakebody) > 0:

            xhead = snake.xcor()
            yhead = snake.ycor()
            

            for count_body, bodypart in reversed(list(enumerate(snakebody))):
                
                if count_body == 0:
                    
                    bodypart.goto(xhead,yhead)

                else:
                    xneck = snakebody[count_body-1].xcor()
                    yneck = snakebody[count_body-1].ycor()
                    snakebody[count_body].goto(xneck,yneck)


        #revisar que la serpiente no choque consigo misma

        for bodypart in snakebody[1:]:
            if bodypart.distance(snake) < 11:
                kill_snake()

        #por alguna razón que no entiendo, rara vez, el juego se buguea al iniciar, esto evita que tu pc muera
        if abort > 10000:
            break

        time.sleep(react_time)

    mainloop()    
