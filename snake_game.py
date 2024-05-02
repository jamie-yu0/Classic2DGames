import turtle
import time
import random

delay=0.1
score=0
high_score=0

wn=turtle.Screen()
wn.title("SnakeGame")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

wn.register_shape('snake.gif')
wn.register_shape('candy.gif')

#head
head=turtle.Turtle()
head.speed(0)
head.shape('snake.gif')
# head.shape('square')

head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food=turtle.Turtle()
food.speed(0)
food.shape("candy.gif")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0, High Score: 0", align="center", font=("Courier", 24, "normal"))

#functions
def go_up():
    # if head.direction != "down":
        head.direction="up"
def go_down():
    # if head.direction != "up":
        head.direction="down"
def go_left():
    # if head.direction != "right":
        head.direction="left"
def go_right():
    # if head.direction != "left":
        head.direction="right"
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

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
#main game loop
while True:
    wn.update()
    #check collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        #hide segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear segments list
        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write("Score: {}, High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for a collision with food
    if head.distance(food) < 20: #collided
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay-=0.001

        #increase the score
        score+=10
        if score>high_score: high_score=score
        pen.clear()
        pen.write("Score: {}, High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment0 to where head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check head collision with segment
    for segment in segments:
        if segment.distance(head) < 20: #collided
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
             #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            #clear segments list
            segments.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write("Score: {}, High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
