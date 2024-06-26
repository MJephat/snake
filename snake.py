import turtle  # importing the modules
import time
import random
delay = 0.1
score = 0
high_score = 0
wn = turtle.Screen() # creating window screen.
wn.title = ("Snake Game")
wn.bgcolor = ("blue")
wn.setup(width =600, height = 600)
wn.tracer(0)
head = turtle.Turtle()  # creating head of the snake.
head.shape("circle")
head.color("black")
head.penup()
head.goto (0, 0)
head.direction = "stop"
food = turtle.Turtle() # snake food
color = random.choice(['red', 'green', 'black'])
shape = random.choice(['circle', 'triangle', 'square'])
food.speed(0)
food.shape(shape)
food.color(color)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape = ("square")
pen.color = ("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("score: 0 High Score : 0", align = "center", font =("candara", 24, "bold"))
# assign directions
def group():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goright():
    if head.direction != "left":
        head.direction = "right"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
 
 
wn.listen()
wn.onkeypress(group, "W")
wn.onkeypress(godown, "S")
wn.onkeypress(goleft, "A")
wn.onkeypress(goright, "D")
# The main game
segments = []
while True:
    wn.update()
    if head.xcor()> 290 or head.xcor()< -290 or head.ycor()> 290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        colors = random.choice(['red','green','blue'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("score : {} High Score: {}".format(score, high_score), align = "center", font =("candara", 24, "bold"))
    if head.distance(food)<20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
         # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("score : {} High Score: {}".format(score, high_score), align = "center", font =("candara", 24, "bold"))
    time.sleep(delay)
wn.mainloop()