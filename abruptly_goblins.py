# Create an empty list called gamers. This will be your list of people who are attending game night.

gamers = []

# Create a function called add_gamer that takes two parameters: gamer and gamers_list. The function should check that the argument passed to the gamer parameter has both "name" and a "availability" as keys and if so add gamer to gamers_list.


def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Incomplete gamer information.")

# Create a dictionary called kimberly with the name and availability given above.
# Call add_gamer with kimberly as the first argument and gamers as the second.


kimberly = {'name': "Kimberly Warner",
            'availability':  ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)

print(gamers)

# Add more gamers!

add_gamer({'name': 'Thomas Nelson', 'availability': [
          "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': [
          "Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': [
          "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': [
          "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': [
          "Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': [
          "Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': [
          "Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': [
          "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': [
          "Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)

# Create a function called build_daily_frequency_table that takes no argument returns a dictionary with the days of the week as keys and 0s for values. We'll be using this to count the availability per night. Call build_daily_frequency_table and save the results to a variable called count_availability.


def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0
    }


count_availability = build_daily_frequency_table()

# Write a function called calculate_availability that takes a list of gamers as an argument gamers_list and a frequency table available_frequency. The function should iterate through each gamer in gamers_list and iterate through each day in the gamer's availability. For each day in the gamer's availability, add one to that date on the frequency table.


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            if day in available_frequency:
                available_frequency[day] += 1

# Call calculate_availability with gamers and count_availability. Print out count_availability afterwards.


calculate_availability(gamers, count_availability)
print(count_availability)

# Write a function find_best_night that takes a dictionary availability_table and returns the key with the highest number.


def find_best_night(availability_table):
    most_available = 0
    for day, availability in availability_table.items():
        if availability > most_available:
            best_night = day
            most_available = availability
    return best_night

# Call find_best_night with count_availability, store the result in a variable called game_night. Print out game_night to find out which day it is.


game_night = find_best_night(count_availability)
print(game_night)
