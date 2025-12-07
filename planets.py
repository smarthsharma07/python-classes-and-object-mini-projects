class Planet:
    def __init__(self,name,planet_type,star):
        if not all(isinstance(x, str) for x in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")
        if (planet_type and name and star) == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
        self.name=name
        self.planet_type=planet_type
        self.star=star
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
planet_1 = Planet("Mercury", "terrestrial", "Sun")
planet_2 = Planet("Jupiter", "gas giant", "Sun")
planet_3 = Planet("Neptune", "ice giant", "Sun")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
