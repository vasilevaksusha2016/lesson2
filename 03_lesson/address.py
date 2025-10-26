class Address:

    def __init__(self, postcode, city, street, house, apartment):
        self.p = postcode
        self.c = city
        self.s = street
        self.h = house
        self.a = apartment

    def __str__(self):
        return f"{self.p}, {self.c}, {self.s}, {self.h} - {self.a}"
