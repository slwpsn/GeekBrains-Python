class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, weight = 25, thick = 5):
        asph_mass = self._length * self._width * weight * thick
        print(f'{self._length} м * {self._width} м * {weight} кг * {thick} см = {asph_mass} т')

a = Road(20, 30)
a.asphalt_mass()
