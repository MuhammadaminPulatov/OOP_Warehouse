from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"{self.name} - {self.quantity} x {self.price} so'm"

    def sell(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            return f"{amount} dona {self.name} sotildi. Qoldiq: {self.quantity} dona."
        else:
            return "Xato: Mahsulot yetarli emas!"

    def restock(self, amount):
        self.quantity += amount
        return f"{amount} dona {self.name} omborga qo'shildi. Yangi qoldiq: {self.quantity} dona."

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        return f"{self.name} - {self.quantity} x {self.price} so'm | Kafolat: {self.warranty}"

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def info(self):
        return f"{self.name} - {self.quantity} x {self.price} so'm | Yaroqlilik muddati: {self.expiration_date.date()}"

    def sell(self, amount):
        if datetime.now() > self.expiration_date:
            return "Xato: Yaroqlilik muddati o'tgan mahsulot sotib olinmaydi."
        return super().sell(amount)

e = Electronics("Televizor", 1500000, 20, "2 yil")
print(e.info())
print(e.sell(5))

f = Food("Pasta", 2000, 100, "2025-10-01")
print(f.info())
print(f.sell(50))

expired_food = Food("Yaroqsiz Pasta", 2000, 50, "2023-01-01")
print(expired_food.sell(10))