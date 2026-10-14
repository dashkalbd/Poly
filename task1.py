class CourierDelivery:
    name = "Кур'єр"

    def calculate_cost(self, weight):
        return weight * 10


class PostDelivery:
    name = "Пошта"

    def calculate_cost(self, weight):
        return weight * 5


class PickupDelivery:
    name = "Самовивіз"

    def calculate_cost(self, weight):
        return 0

deliveries = [CourierDelivery(), PostDelivery(), PickupDelivery()]

def show_costs(deliveries, weight):
    for delivery in deliveries:
        cost = delivery.calculate_cost(weight)
        print(f"{delivery.name}: {cost} грн")


weight = float(input("Вага замовлення, кг: "))
show_costs(deliveries, weight)