capitals = {
    "Japan" : "Tokyo",
    "Nepal" : "Kathmandu",
    "Russia" : "Muscow"
}

travel_log ={
    "Japan" : {
         "num_times_visited" : 2,
         "cities_visited": ["Tokyo","Osaka","Nara","Kyoto"]
    },
    "Nepal" : ["Kathmandu","Bhaktapur","Lalitpur"]
}

# How you can print Osaka

print(travel_log["Japan"]["cities_visited"][1])


nested_list = ["A", "B", ["C","D"]]
print(nested_list[2][1])


