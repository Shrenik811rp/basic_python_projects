import turtle
import time
import random

#speed of animation
delay = 0.2

# Score
score = 0
high_score = 0

#setup screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600,height=600)
#turns off animation on screen
window.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
#once drawn stop drawing line
head.penup()
head.goto(0,0)
head.direction = "stop"



#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
#once drawn stop drawing line
food.penup()
food.goto(200,100)



#snake body made of segments
segments = []


# Pen
#for writing score onto the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 16, "normal"))


def moveUp():
    #if snake is moving up cannot switch to down
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    #if snake is moving down cannot switch to up
    if head.direction != "up":
        head.direction = "down"
    
def moveRight():
    #if snake is moving right cannot switch to left
    if head.direction != "left":
        head.direction = "right"
    
def moveLeft():
    #if snake is moving left cannot switch to right
    if head.direction != "right":
        head.direction = "left"


def move():

    if head.direction == "up":

        #update the y coordinate
        y = head.ycor()
        #move up in yaxis by 20 px
        head.sety(y+20)

    if head.direction == "down":

        #update the y coordinate
        y = head.ycor()
        #move down in yaxis by 20 px
        head.sety(y-20)

    if head.direction == "left":

        #update the x coordinate
        x = head.xcor()
        #move left in xaxis by 20 px
        head.setx(x-20)
    if head.direction == "right":

        #update the x coordinate
        x = head.xcor()
        #move right in xaxis by 20 px
        head.setx(x+20)

#keyboard bindings listening for input
window.listen()
window.onkeypress(moveUp,"Up")
window.onkeypress(moveDown,"Down")
window.onkeypress(moveRight,"Right")
window.onkeypress(moveLeft,"Left")


def changeFood():
    # Move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 270)
    food.goto(x,y)

def stopGame():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"
    
    
#main game loop
while True:

    window.update()

    '''
    When snake hits the walls or border window
    '''

    #check for collision,change food locaiton
    #increase snake body
    #when snake goes out of bound return it back to center of screen
    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        stopGame()
        changeFood()

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score when collision with walls
        score = 0

        # Reset the delay
        delay = 0.2

        pen.clear()

        #reset the score and display text again
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal")) 


    '''
    When snake eats food
    '''
    # Check for a collision with the food
    if head.distance(food) < 20:
        changeFood()
       

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.007

        # Increase the score when snake eats food
        score += 10

        # set the highscore until game play
        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal")) 


    '''
    Add new snake segments when snake eats food
    - everytime snake eats increase segments
    '''
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    '''
    When snake collides with its own body
    '''
    # Check for head collision with the body segments
    for segment in segments:

        #when it hits its body stop moving
        #go to origin and start again 
        if segment.distance(head) < 20:
            stopGame()
            changeFood()
        
            # Hide the segments 
            # so we see only the snake head
            # when we start new game and not bidy 
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.2
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "normal"))

    time.sleep(delay)



window.mainloop()