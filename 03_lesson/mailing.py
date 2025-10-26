class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_a = to_address
        self.from_a = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.to_a} в {self.from_a}."
                f"Стоимость {self.cost} рублей.")
