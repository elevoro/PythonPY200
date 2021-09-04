class Glass:
    """Тест"""

    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана


if __name__ == "__main__":
    #  TODO самостоятельно создайте экземпляр класса Glass и выведите  его атрибуты capacity_volume и occupied_volume
    ...
