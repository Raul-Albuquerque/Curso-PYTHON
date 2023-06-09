          ######################   DICTIONARY ###########################

#Key: Value
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary
#print(programming_dictionary["Bug"])

#Adding new items
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary["Loop"])

#Creating a empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Function"] = "Raul"
#print(programming_dictionary["Function"])

#Loop through a dictionary
for thing in programming_dictionary:
  #this command will print the key
  print(thing)
  #this command will print the value
  print(programming_dictionary[thing])