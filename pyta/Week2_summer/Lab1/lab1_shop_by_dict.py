






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