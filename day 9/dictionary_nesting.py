######################   DICTIONARY 2#########################

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "Total_visits": 10}
}
#print(travel_log["France"])

#Nesting a dictionary in a list
travel_log = [
    {
      "Country": "France", 
      "cities_visited": ["Paris", "Lille", "Dijon"], 
      "Total_visits": 12
    },
    {
      "Country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "Total_visits": 10
    }, 
]