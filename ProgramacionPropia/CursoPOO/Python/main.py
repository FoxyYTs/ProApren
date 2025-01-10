from car import Car

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car()
    car.id = 1987
    car.license = "QWE123"
    car.drive = "Foxy"
    car.passegenger = 4
    print(vars(car))

    car2 = Car()
    car2.license = "PEP012"
    car2.drive = "Booni"
    car2.passegenger = 2
    print(vars(car2))