import ipaddress


class Interface:
    def __init__(self, interface, ip_address):
        self.interface = interface
        self.ip_address = ip_address

    def __str__(self):
        return f'Интерфейс {self.interface}, его ip адрес {self.ip_address}'


class Route:
    def __init__(self, destination, gateway):
        self.destination = destination
        self.gateway = gateway

    def __eq__(self, other):
        return self.destination == other.destination and self.gateway == other.gateway

    def __str__(self):
        return f'Маршрут до {self.destination}, через {self.gateway}'


class Router:
    def __init__(self):
        self.interface_table = []
        self.route_table = []

    def add_interface(self):
        interface = Interface(input('Введите название интерфейса\n'), ipaddress.ip_interface(input('Введите ip адрес интерфейса\n')))
        route = Route(ipaddress.ip_network(interface.ip_address, False), interface.ip_address)

        self.interface_table.append(interface)
        if route not in self.route_table:
            self.route_table.append(route)

    def add_route(self):
        if not self.route_table:
            raise Exception('Сначала нужно добавить интерфейс!')

        route = Route(ipaddress.ip_network(input('Введите адрес подсети\n')), ipaddress.ip_interface(input('Введите адрес шлюза\n')))
        for r in self.route_table:
            if route.gateway.ip in r.destination:
                self.route_table.append(route)
                break

        if route not in self.route_table:
            raise Exception(f'Никак не дойти до {route.gateway}!')

    def show_route_table(self):
        [print(x) for x in self.route_table]

    def delete_route_table(self):
        self.route_table = []

    def show_interface_table(self):
        [print(x) for x in self.interface_table]

    def delete_interface_table(self):
        self.interface_table = []


router = Router()
while True:
    if not router.route_table:
        print('Здравствуйте! На данный момент таблица маршрутов пуста'
                    ', чтобы начать работу вам нужно настроить хотя бы один интерфейс\n')
        router.add_interface()

    inp = input('Введите:\nr чтобы добавить рут\ni чтобы добавить интерфейс\n'
                'dr чтобы очистить таблицу маршрутов\ndi чтобы очистить таблицу интерфейсов\n'
                'sr чтобы показать таблицу маршрутов\nsi чтобы показать таблицу интерфейсов\n'
                'exit чтобы закончить работу\n')
    if inp == 'r':
        router.add_route()
    elif inp == 'i':
        router.add_interface()
    elif inp == 'dr':
        router.delete_route_table()
    elif inp == 'di':
        router.delete_interface_table()
    elif inp == 'sr':
        router.show_route_table()
    elif inp == 'si':
        router.show_interface_table()
    elif inp == 'exit':
        break
    input('Нажмите любую кнопку чтобы продолжить')
