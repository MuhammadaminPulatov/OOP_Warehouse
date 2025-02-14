from datetime import datetime
import uuid

class Product:
    def __init__(self, name, price, quantity):
        self.__id = uuid.uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_id(self):
        return self.__id

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
        self.__id = uuid.uuid4()
        self.products = {}

    def get_id(self):
        return self.__id

    def add_product(self, product):
        product_id = product.get_id()
        if product_id not in self.products:
            self.products[product_id] = product
            return f"{product.name} qo'shildi. Barcha mahsulotlar: {self.show()}"
        else:
            return f"Xato: {product.name} allaqachon savatda bor."

    def remove_product(self, product_id):
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            return f"{removed_product.name} olib tashlandi. Qoldiq mahsulotlar: {self.show()}"
        else:
            return "Xato: Mahsulot topilmadi."

    def show(self):
        if self.products:
            product_info = [product.info() for product in self.products.values()]
            return product_info
        else:
            return "Mahsulotlar yo'q."

    def total_price(self):
        total = 0
        for product in self.products.values():
            total += product.price * product.quantity
        return total


def main_menu():
    print("\n=== Savat Menyusi ===")
    print("1. Mahsulot qo'shish")
    print("2. Mahsulotni olib tashlash")
    print("3. Savatdagi mahsulotlarni ko'rish")
    print("4. Umumiy narxni ko'rish")
    print("5. Chiqish")
    choice = input("Tanlang (1/2/3/4/5): ")
    return choice


def add_product_menu(basket):
    name = input("Mahsulot nomini kiriting: ")
    price = float(input("Narxini kiriting: "))
    quantity = int(input("Miqdorini kiriting: "))
    category = input("Kategoriya (electronics/food): ").lower()

    if category == "electronics":
        warranty = input("Kafolat muddatini kiriting (masalan, '2 yil'): ")
        product = Electronics(name, price, quantity, warranty)
    elif category == "food":
        expiration_date = input("Yaroqlilik muddatini kiriting (YYYY-MM-DD): ")
        product = Food(name, price, quantity, expiration_date)
    else:
        print("Xato: Noto'g'ri kategoriya.")
        return

    print(basket.add_product(product))


def remove_product_menu(basket):
    product_id = input("Olib tashlanadigan mahsulotning ID raqamini kiriting: ")
    try:
        product_id = uuid.UUID(product_id)  # Convert string to UUID
        print(basket.remove_product(product_id))
    except ValueError:
        print("Xato: Noto'g'ri ID formati.")


def view_products_menu(basket):
    products = basket.show()
    if isinstance(products, list):
        for product in products:
            print(product)
    else:
        print(products)


def total_price_menu(basket):
    print(f"Umumiy narx: {basket.total_price()} so'm")


def main():
    basket = Basket()
    while True:
        choice = main_menu()
        if choice == "1":
            add_product_menu(basket)
        elif choice == "2":
            remove_product_menu(basket)
        elif choice == "3":
            view_products_menu(basket)
        elif choice == "4":
            total_price_menu(basket)
        elif choice == "5":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Xato: Noto'g'ri tanlov. Iltimos, qaytadan urinib ko'ring.")


main()