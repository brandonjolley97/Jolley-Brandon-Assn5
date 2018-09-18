import turtle

# Set up target turtle
window = turtle.Screen()
target = turtle.Turtle()
target.speed(20)
target.width(10)

# Adding prompts for user input
locationX,locationY = eval(input("Please enter a x and y coordinate for the center of the target. Seperate input with commas: "))
radiusCenter = eval(input("Please enter a radius for the center of the target: "))

# Variables for the location of the target
locationCenterX = locationX
biggestRadius = radiusCenter + 75
locationCenterY = locationY - biggestRadius

# Black Circle
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("black")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

# Blue Circle
biggestRadius -= 25
locationCenterY += 25
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("blue")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

# Red Circle
biggestRadius -= 25
locationCenterY += 25
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("red")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

# Yellow Circle (Bulls-eye)
biggestRadius -= 25
locationCenterY += 25
target.color("yellow")
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()



turtle.done()
