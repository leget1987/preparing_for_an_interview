# 5. Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self._ItemDiscount__name}: {self._ItemDiscount__price}P"


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def set_price(self, price):
        self._ItemDiscount__price = price

    def __str__(self):
        return f"{self._ItemDiscount__name}: " \
               f"{self._ItemDiscount__price - self._ItemDiscount__price * self.discount / 100}"

    def get_parent_data(self):
        print(self)


child = ItemDiscountReport('iphone', 70000, 5)
child.get_parent_data()
