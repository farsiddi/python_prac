# Nesting a list in a dictionary
from turtle import clear

# List inside a dictionary
travel1 = {
    "Gujarat": ["Rajkot", "Ahmedabad"],
    "Uttar Pradesh": ["Agra", "Kanpur", "Lucknow"],
    "Punjab": ["Amritsar", "Ludhiana", "Jalandhar"]
}
print(travel1)
print(travel1["Punjab"])

# List inside a dictionary which itself is inside a dictionary
travel2 = {
    "Gujarat": {"cities_visited": ["Rajkot", "Ahmedabad"], "transport": "Flight"},
    "Uttar Pradesh": ["Agra", "Kanpur", "Lucknow"],
    "Punjab": ["Amritsar", "Ludhiana", "Jalandhar"]
}

# Dictionary inside List
my_travel_list = [
    {"country": "England",
     "cities_visited": ["London", "Bristol", "Liverpool"],
     "visit": 10
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "visit": 6
     }
]
