


# Пример использования
address = "Варшавское Шоссе, 144 к. 2"
coordinates = get_coordinates(address)
if coordinates:
    print("Координаты адреса {}: {}".format(address, coordinates))
else:
    print("Адрес не найден.")