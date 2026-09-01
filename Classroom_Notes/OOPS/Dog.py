class Dog:
    species = "Canis familiaris"  # Class attribute
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    #Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    @classmethod
    def common_species(cls):
        return f"All dogs belong to the species {cls.species}."
    @staticmethod
    def is_dog_older_than(dog_age, age):
        return dog_age > age