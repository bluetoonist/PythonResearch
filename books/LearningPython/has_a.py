from Is_a import PizzaRobot, Server


class Customer:

    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, " orders from", server)

    def pay(self, server):
        print(self.name, "pays for item to", server)


class Oven:
    def bake(self):
        print("oven bakes")


class PizzaShop:  # Container, Controller
    def __init__(self):
        self.server = Server("pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()  # 복합 객체 생성
    scene.order('Homer')  # Homer의 주문을 시뮬레이션
    print('...')
    scene.order('Shaggy')  # Shaggy의 주문을 시뮬레이션
