import turtle


#variables
paddle_speed = 40
ball_speed = 0.2

#init

wn = turtle.Screen()
wn.title("BagoPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed

#points
point = turtle.Turtle()
point.speed(0)
point.penup()
point.color("white")
point.hideturtle()
point.goto(0, 260)
point.write("Player A: 0  Player B: 0", align="center", font=("courier", 24, "normal"))

#Score
score_a = 0
score_b = 0


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_speed
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_speed
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_speed
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_speed
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#gameloop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
#border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        point.clear()
        point.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        point.clear()
        point.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

#ball and paddle colision
    if  (ball.xcor() > 330 and ball.xcor() < 340) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(330)
        ball.dx *= -1.0

    if  (ball.xcor() < -330 and ball.xcor() > -340) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-330)
        ball.dx *= -1.0
