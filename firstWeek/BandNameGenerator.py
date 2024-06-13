class BandNameGenerator:
    def __init__(self):
        pass
    def run(self):

        print("Welcome to the band Name Generator, ")
        city_name = input( "What's the name of the city you grew up in\n")
        pet_name = input("What's your pet's name?\n")
        print("Your band name could be " + city_name + " " + pet_name)