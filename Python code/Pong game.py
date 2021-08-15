# Pong game
import turtle
import winsound

# Game window
window = turtle.Screen()
window.title("Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Player A
Player_A = turtle.Turtle()
Player_A.speed(0)
Player_A.shape("square")
Player_A.color("white")
Player_A.shapesize(stretch_wid=5, stretch_len=1)
Player_A.penup()
Player_A.goto(-390, 0)

# Player B
Player_B = turtle.Turtle()
Player_B.speed(0)
Player_B.shape("square")
Player_B.color("white")
Player_B.shapesize(stretch_wid=5, stretch_len=1)
Player_B.penup()
Player_B.goto(380, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.1
Ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def player_a_up():
    y = Player_A.ycor()
    y += 5
    Player_A.sety(y)


def player_a_down():
    y = Player_A.ycor()
    y -= 5
    Player_A.sety(y)


def player_b_up():
    y = Player_B.ycor()
    y += 5
    Player_B.sety(y)


def player_b_dowm():
    y = Player_B.ycor()
    y -= 5
    Player_B.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(player_a_up, "w")
window.onkeypress(player_a_down, "s")
window.onkeypress(player_b_up, "Up")
window.onkeypress(player_b_dowm, "Down")

# run window
while True:
    window.update()

    # Moved Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Borad checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("game_over", winsound.SND_ASYNC)

    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("game_over", winsound.SND_ASYNC)

    # Player and ball collisions
    if (Ball.xcor() > 360) and (Ball.xcor() < 370) and (
            Ball.ycor() < Player_B.ycor() + 50 and Ball.ycor() > Player_B.ycor() - 50):
        Ball.setx(360)
        Ball.dx *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

    if (Ball.xcor() < -370) and (Ball.xcor() > -380) and (
            Ball.ycor() < Player_A.ycor() + 50 and Ball.ycor() > Player_A.ycor() - 50):
        Ball.setx(-370)
        Ball.dx *= -1
        winsound.PlaySound("jump.wav", winsound.SND_ASYNC)

