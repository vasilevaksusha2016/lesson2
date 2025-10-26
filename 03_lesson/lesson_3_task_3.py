from address import Address
from mailing import Mailing

to_address = Address(123456, "Москва", "Пушкина", 1, 100)
from_address = Address(654321, "Санкт-Петербург", "Пушкина", 2, 200)
price = 690
track_num = "TN923473875"

mailing = Mailing(to_address, from_address, price, track_num)


print(mailing)
