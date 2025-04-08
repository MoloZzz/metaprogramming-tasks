import logging

logging.basicConfig(level=logging.INFO)

class CityDescriptor:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.attr_name}")

    def __set__(self, obj, value):
        # Логування зміни через декоратор буде викликано автоматично
        setattr(obj, f"_{self.attr_name}", value)

    def __delete__(self, obj):
        delattr(obj, f"_{self.attr_name}")

class City:
    name = CityDescriptor("name")
    region = CityDescriptor("region")
    population = CityDescriptor("population")
    districts = CityDescriptor("districts")

    def __init__(self, name, region, population, districts):
        self._name = name
        self._region = region
        self._population = population
        self._districts = districts

    def __str__(self):
        return f"City: {self.name}, Region: {self.region}, Population: {self.population}, Districts: {self.districts}"

# 2. Декоратор attr_change_logger
def attr_change_logger(cls):
    loggers = {
        'name': logging.getLogger('name_logger'),
        'population': logging.getLogger('population_logger'),
        'districts': logging.getLogger('districts_logger')
    }

    for attr, logger in loggers.items():
        handler = logging.FileHandler(f'static/{attr}_changes.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    original_set = cls.__setattr__

    def new_setattr(self, name, value):
        # Перевірка, чи змінюється відслідковуваний атрибут
        if name in ['_name', '_population', '_districts']:
            attr_name = name[1:]  # Видаляємо підкреслення
            old_value = getattr(self, attr_name, None)
            if old_value != value:
                loggers[attr_name].info(
                    f"Changed {attr_name} from {old_value} to {value}"
                )
        original_set(self, name, value)

    cls.__setattr__ = new_setattr
    return cls

class FixNumCreator(type):
    _instances = []
    _max_instances = 3
    _creation_logger = logging.getLogger('creation_logger')

    @classmethod
    def _setup_logger(cls):
        handler = logging.FileHandler('static/city_creation.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        cls._creation_logger.addHandler(handler)
        cls._creation_logger.setLevel(logging.INFO)

    def __new__(cls, name, bases, attrs):
        cls._setup_logger()
        return super().__new__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        if len(cls._instances) >= cls._max_instances:
            raise ValueError(f"Cannot create more than {cls._max_instances} instances of {cls.__name__}")
        
        instance = super().__call__(*args, **kwargs)
        cls._instances.append(instance)
        
        cls._creation_logger.info(
            f"Created new city: {instance.name}, Region: {instance.region}, "
            f"Population: {instance.population}, Districts: {instance.districts}"
        )
        
        return instance

@attr_change_logger
class City(metaclass=FixNumCreator):
    name = CityDescriptor("name")
    region = CityDescriptor("region")
    population = CityDescriptor("population")
    districts = CityDescriptor("districts")

    def __init__(self, name, region, population, districts):
        self._name = name
        self._region = region
        self._population = population
        self._districts = districts

    def __str__(self):
        return f"City: {self.name}, Region: {self.region}, Population: {self.population}, Districts: {self.districts}"

if __name__ == "__main__":
    try:
        city1 = City("Kyiv", "Kyiv Oblast", 2800000, ["Pechersk", "Obolon"])
        print(city1)
        
        city1.population = 2900000
        city1.districts = ["Pechersk", "Obolon", "Podil"]
        
        city2 = City("Lviv", "Lviv Oblast", 720000, ["Halych", "Sykhiv"])
        print(city2)
        
        city3 = City("Odesa", "Odesa Oblast", 1000000, ["Primorsky", "Kyivsky"])
        city4 = City("Kharkiv", "Kharkiv Oblast", 1400000, ["Shevchenkivsky"])  # Викличе помилку
        
    except ValueError as e:
        print(f"Error: {e}")