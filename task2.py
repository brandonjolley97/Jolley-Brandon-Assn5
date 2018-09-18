import turtle

window = turtle.Screen()
target = turtle.Turtle()
target.speed(10)
target.width(10)


locationX,locationY = eval(input("Please enter a x and y coordinate for the center of the target. Seperate input with commas: "))
radiusCenter = eval(input("Please enter a radius for the center of the target: "))

locationCenterX = locationX
locationCenterY = locationY - radiusCenter


target.penup()
target.goto(locationCenterX,locationCenterY + 75)
target.pendown()
target.color("yellow")
target.begin_fill()
target.circle(radiusCenter)
target.end_fill()

target.penup()
target.goto(locationCenterX,locationCenterY + 50)
target.pendown()
target.color("red")
target.begin_fill()
target.circle(100)
target.end_fill()

target.penup()
target.goto(locationCenterX,locationCenterY + 25)
target.pendown()
target.color("blue")
target.begin_fill()
target.circle(150)
target.end_fill()

target.color("black")
target.penup()
target.goto(locationCenterX,locationCenterY)
target.pendown()
target.begin_fill()
target.circle()
target.end_fill()







turtle.done()
