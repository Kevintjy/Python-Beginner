class Object:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number



class ShopCatalogue:
    def __init__(self, name):
        self.name = name
        self.object_list = []

    def add_item(self, name, price, number):
        object = Object(name, price, number)
        for i in range(len(self.object_list)):
            if name == self.object_list[i].name:
                self.object_list[i].number += number
        name_list = []
        for j in self.object_list:
            name_list.append(j.name)
        if name not in name_list:
            self.object_list.append((object))

    def remove_item(self, name, number):
        for i in range(len(self.object_list)):
            if self.object_list[i].name == name:
                self.object_list[i].number -= number
            if self.object_list[i].number == 0:
                    self.object_list.remove(self.object_list[i])
    def get_items_below(self, price):
        result = []
        for i in self.object_list:
            if i.price < price:
                result.append(i.name)
        return result

    def __str__(self):
        result = []
        result.append("{} has: {} (x{}) for {} each".format(self.name,
                                                            self.object_list[0].name,
                                                            self.object_list[0].number,
                                                            self.object_list[0].price))
        for i in self.object_list[1:]:
            result.append(" {} (x{}) for {:.2f} each".format(i.name, i.number, i.price))
        return ','.join(result)









if __name__ == '__main__':
    s = ShopCatalogue("UofT Bookstore")
    s.add_item("Chips", 0.99, 3)
    assert str(s) == "UofT Bookstore has: Chips (x3) for 0.99 each"
    s.add_item("Chips", 0.99, 10)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pencil", 2.50, 3)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil (x3) for 2.50 each"
    s.remove_item("Pencil", 2)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each, Pencil (x1) for 2.50 each"
    s.remove_item("Pencil", 1)
    assert str(s) == "UofT Bookstore has: Chips (x13) for 0.99 each"
    s.add_item("Pop", 1.95, 3)
    s.add_item("Pencil", 2.50, 2)
    assert s.get_items_below(2.00) == ['Chips', 'Pop']