from datetime import datetime


class ZooDatabase:
    def get_animals(self, species):
        return None

    def get_food_period(self, species):
        return None

    def feed_animal(self, name, when):
        pass


def do_round(database, species, *, now=datetime.now):
    now = now()
    feeding_timedelta = database.get_food_period(species)
    animals = database.get_animals(species)
    fed = 0

    for name, last_mealtime in animals:
        if (now - last_mealtime) >= feeding_timedelta:
            database.feed_animal(name, now)
            fed += 1
    return fed
