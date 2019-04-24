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
