class Flower:
    is_happy = False
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements


    def water(self, quantity: int):
        if quantity >= self.water_requirements:
            Flower.is_happy = True
        else: Flower.is_happy = False

    def status(self):
        if Flower.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())