import turtle

window = turtle.Screen()
target = turtle.Turtle()
target.speed(10)
target.width(10)


locationX,locationY = eval(input("Please enter a x and y coordinate for the center of the target. Seperate input with commas: "))
radiusCenter = eval(input("Please enter a radius for the center of the target: "))

locationCenterX = locationX
biggestRadius = radiusCenter + 75
locationCenterY = locationY - biggestRadius

target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("black")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

biggestRadius -= 25
locationCenterY += 25
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("blue")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

biggestRadius -= 25
locationCenterY += 25
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.color("red")
target.begin_fill()
target.circle(biggestRadius)
target.end_fill()

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
