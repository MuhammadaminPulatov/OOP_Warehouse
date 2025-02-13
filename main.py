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

class Basket:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return f"{product.name} qo'shildi.Barcha mahsulotlar: {self.show()}"

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"{product_name} olib tashlandi. Qoldiq mahsulotlar: {self.show()}"
        return "Mahsulot topilmadi."

    def show(self):
        if self.products:
            product_info = [product.info() for product in self.products]
            return product_info
        else:
            return "Mahsulotlar yo'q."


    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

#----------------------------------------------------------------


e = Electronics("Televizor", 1500000, 20, "2 yil")
print(e.info())
print(e.sell(5))

f = Food("Pasta", 2000, 100, "2025-10-01")
print(f.info())
print(f.sell(50))

expired_food = Food("Yaroqsiz Pasta", 2000, 50, "2023-01-01")
print(expired_food.sell(10))

basket = Basket()
basket.add_product(e)  
basket.add_product(f)  
print(basket.show())
print(f"Umumiy narx: {basket.total_price()} so'm")
basket.remove_product("Televizor")
print(basket.show())
