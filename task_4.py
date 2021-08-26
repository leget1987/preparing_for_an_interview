# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
# отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self._ItemDiscount__name}: {self._ItemDiscount__price}P"


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_price(self, price):
        self._ItemDiscount__price = price

    def get_parent_data(self):
        print(self)


child = ItemDiscountReport('iphone', 70000)
child.get_parent_data()
child.set_price(80000)
child.get_parent_data()
