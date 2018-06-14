class SadWalletError(Exception):
    '''
    vbn
    nothing
    '''
    pass

class NotInClosetError(Exception):
    '''
    nothing
    '''
    pass

class Person:
    '''
    nothing
    '''
    def __init__(self, clothes, money):
        '''
        nothing
        '''
        self.clothes = clothes
        self.closet = [clothes]
        self.money = money

    def purchase_clothes(self, clothes):
        '''
        nothing
        '''
        if self.money >= clothes.price:
            self.money -= clothes.price
            self.closet.append(clothes)
        else:
            raise SadWalletError

    def take_clothes(self, clothes):
        '''
        nothing
        '''
        if clothes in self.closet:
            self.clothes = clothes
        else:
            raise NotInClosetError

    def get_clothes_by_colour(self, colour):
        '''
        nothing
        '''
        raise NotImplementedError



class Clothes:
    '''
    nothing
    '''
    def __init__(self, brand, colour, price):
        '''
        nothing
        '''
        self.brand = brand
        self.colour = colour
        self.price = price

    def __repr__(self):
        '''
        nothing
        '''
        return 'Clothes(' + str(self.brand) + ', ' +\
                            str(self.colour)+ ', ' +\
                            str(self.price) + ')'

class Employee(Person):
    '''
    nothing
    '''
    def __init__(self, clothes, money):
        '''
        nothing
        '''
        super().__init__(clothes, money)
        self.store = []

    def purchase_clothes(self, clothes):
        '''
        nothing
        '''
        if self.money >= clothes.price * discount:
            self.money -= clothes.price * discount
            self.closet.append(clothes)
        else:
            raise SadWalletError

    def is_purchased(self, clothes):
        '''
        nothing
        '''
        self.store.remove(clothes)

    def get_clothes_by_colour(self, colour):
        '''
        nothing
        '''
        result = []
        for i in self.closet:
            if i.colour == colour:
                result.append(i)
        return result




if __name__ == '__main__':
    discount = 0.5
    import python_ta

    python_ta.check_all(config="lab_pyta.txt")
    import doctest

    doctest.testmod()
