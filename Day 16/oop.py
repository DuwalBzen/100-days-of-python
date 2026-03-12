
# from turtle import Turtle, Screen
#
# turtle1 = Turtle()
# turtle1.shape("turtle")
# turtle1.color("blue3")
# turtle1.forward(100)
# print(turtle1)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
cartoon = PrettyTable()

table.field_names = ["Name", "Followers (M)", "Profession", "Country"]

table.add_row(["Cristiano Ronaldo", 630, "Footballer", "Portugal"])
table.add_row(["Lionel Messi", 505, "Footballer", "Argentina"])
table.add_row(["Selena Gomez", 430, "Singer / Actress", "USA"])
table.add_row(["Kylie Jenner", 400, "Businesswoman", "USA"])
table.add_row(["Dwayne Johnson", 395, "Actor / Wrestler", "USA"])
table.add_row(["Ariana Grande", 380, "Singer", "USA"])

print(table)

cartoon.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
cartoon.add_column("Type",["Electric","Water","Fire"])
cartoon.align = 'l'
print(cartoon)





