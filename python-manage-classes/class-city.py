class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        if self.name in instance.__dict__:
            del instance.__dict__[self.name]


class City:
    name = Descriptor("name")
    region = Descriptor("region")
    population = Descriptor("population")
    districts = Descriptor("districts")

    def __init__(self, name, region, population, districts):
        self.name = name
        self.region = region
        self.population = population
        self.districts = districts


# Example usage
if __name__ == "__main__":
    city = City("Kyiv", "Kyiv Region", 2800000, ["Shevchenkivskyi", "Pecherskyi", "Podilskyi"])
    print(city.name)  
    print(city.region)  
    print(city.population)  
    print(city.districts) 
    city.population = 3000000
    print(city.population) 
    del city.districts
    print(city.districts)