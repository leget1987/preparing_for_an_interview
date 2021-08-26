# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self._ItemDiscount__name}: {self._ItemDiscount__price}P"


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self)


child = ItemDiscountReport('iphone', 70000)
child.get_parent_data()
