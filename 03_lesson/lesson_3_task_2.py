from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "17", "+79800678910"),
    Smartphone("Samsung", "Galaxy", "+79555444111"),
    Smartphone("Xiaomi", "Redmi", "+79111222333")
]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
