from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkRed")
timmy.shapesize(5)
# print(timmy)

my_screen = Screen()
print(my_screen.canvheight)

timmy.goto(150, 150)
timmy.goto(-150, 150)
timmy.goto(0,0)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Item", ["ox", "horse", "chicken"])
table.add_column("Tier", [3, 3, 2])
table.align["Item"] = "l"
print(table)
print(table.align)