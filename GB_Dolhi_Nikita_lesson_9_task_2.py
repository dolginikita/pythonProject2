class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def count_mass(self, layer, thickness):
        print(f'Масса асфальта = {int((layer * self.__length * self.__width * thickness) / 1000)} т.')


road_lw = Road(5000, 25)
road_lw.count_mass(20, 5)