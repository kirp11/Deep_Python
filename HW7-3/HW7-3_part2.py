
class Employee:
    def __init__(self, name, access_zones):
        self.__name = name
        self.__access_zones = access_zones

    def get_name(self):
        return self.__name

    def get_access_zones(self):
        return self.__access_zones


class SecuritySystem:
    def __init__(self):
        self.__closed_zones = ["Office", "Storage"]
        self.__employies = []

    def get_closed_zones(self):
        return self.__closed_zones

    def add_employee(self, employee):
        self.__employies.append(employee)


    def enter_zone(self, employee, zone):
        if zone in employee.get_access_zones():
            print(f"Сотруднику {employee.get_name()} ВОЙДИТЕ!")
        else:
            print(f"Сотруднику {employee.get_name()} вход ЗАПРЕЩЕН")


def requires_access(zone, lst_zones):
    def decorator(func):
        if zone in lst_zones:
            def wrapper(*args):
                func(*args)
            return wrapper
    return decorator


def log_access():
    pass


bob = Employee("Bob", ["Office", "Storage", "Lab"])
snak = Employee("Snak", ["Office", "Storage"])
dub = Employee("Dub", ["Lobby", "Cafeteria"])
ivi = Employee("Ivi", ["Lobby", "Storage"])

system = SecuritySystem()
system.add_employee(bob)
system.add_employee(snak)
system.add_employee(dub)
system.add_employee(ivi)




