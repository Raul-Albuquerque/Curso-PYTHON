import turtle

timmy = turtle.Turtle()

#################### SAME THING ###################

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

####### ACESSING THE ATRIBUTES #####

# SYNTAX =  object.attribute
my_screen =  Screen()
print(my_screen.canvheight) 
timmy.shape("turtle")
timmy.color("coral")
#making the turtle move
timmy.forward(100)

############ ACESSING THE METHODS #################
# SYNTAX =  object.method()
my_screen.exitonclick()
