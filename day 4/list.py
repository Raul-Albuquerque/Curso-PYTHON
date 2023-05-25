import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#random_state = random.randint(0 , 49)

#[] -> positive number starts for the left side.
#[- ] -> negative number starts for the right side.

#manipulatting a item from the list
state = states_of_america[1] = "Pencilvania"
print(states_of_america)

#append a item to the list
states_of_america.append("Rauland")
print(states_of_america)

#extend a list
states_of_america.extend(["Angeland", "Jack Bauer land"])
print(states_of_america)