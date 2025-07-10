
def requires_access(func):
    def wrapper(self, user, zone, *args):
        if zone in self.get_closed_zones():
            if zone in user.get_access_zones():
                result = func(self, user, zone, *args)
                return result
            else:
                print(f"Сотруднику {user.get_name()} ОТКАЗАНО В ДОСТУПЕ")
        else:
            print(f"Сотруднику {user.get_name()} можно войти в свободную зону")
    return wrapper

def log_access(func):
    access_granted = []
    access_denied = []
    def wrapper(self, user, zone, *args):
        result = func(self, user, zone, *args)
        if result == "Сотруднику {user.get_name()} ОТКАЗАНО В ДОСТУПЕ":
            access_granted.append(user.get_name())
            print(access_granted)
        else:
            access_denied.append(user.get_name())
            print(access_denied)

    return wrapper


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

    def get_employies(self):
        return self.__employies

    def add_employee(self, employee):
        self.__employies.append(employee)

    @log_access
    @ requires_access
    def enter_zone(self, employee, zone):
        if zone in employee.get_access_zones():
            print(f"Сотруднику {employee.get_name()} ВОЙДИТЕ!")
        else:
            print(f"Сотруднику {employee.get_name()} вход ЗАПРЕЩЕН")




bob = Employee("Bob", ["Office", "Storage", "Lab"])
snak = Employee("Snak", ["Office", "Storage"])
dub = Employee("Dub", ["Lobby", "Cafeteria"])
ivi = Employee("Ivi", ["Lobby", "Storage"])

system = SecuritySystem()
system.add_employee(bob)
system.add_employee(snak)
system.add_employee(dub)
system.add_employee(ivi)
system.enter_zone(bob, "Office")
system.enter_zone(bob, "Lobby")
system.enter_zone(ivi, "Office")





