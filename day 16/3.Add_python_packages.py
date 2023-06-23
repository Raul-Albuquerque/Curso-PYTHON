############# PROGRAM: PYPI ###########
from prettytable import PrettyTable
table = PrettyTable()

#changing methods
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Eletric", "Water", "Fire"])

#changing attributes
table.align = "l"
print(table)