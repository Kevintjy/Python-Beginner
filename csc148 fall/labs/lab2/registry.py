class Player:

    def __init__(self, name, email, speed_category):
        self.name = name
        self.email = email
        self.speed_category = speed_category

    def __repr__(self):
        return 'Player({},{},{})'.format(self.name,self.email,self.speed_category)

    def change_speed(self, new_speed):
        self.speed_category = new_speed

    def change_email(self, new_email):
        self.email = new_email

    def withdraw(self):
        raise NotImplementedError


class Category:
    def __init__(self):
        self.under_twenty = []
        self.under_thirty = []
        self.under_forty = []
        self.above_forty = []


    def creat_player(self, name, email, speed_category):
        p1 = Player(name, email, speed_category)
        if speed_category == '20-':
            self.under_twenty.append(p1)
        if speed_category == '30-':
            self.under_thirty.append(p1)
        if speed_category == '40-':
            self.under_forty.append(p1)
        if speed_category == '40+':
            self.above_forty.append(p1)
        return p1


if __name__ == '__main__':
    cat = Category()
    Gerhard = cat.creat_player('Gerhard', 'Gerhard.gmail.com', '40-')
    Tom = cat.creat_player('Tom', 'Tom.gmail.com', '30-' )
    Toni = cat.creat_player('Toni', 'Toni.gmail.com', '20-')
    Margot = cat.creat_player('Margot', 'Margot.gmail.com', '30-')
    Gerhard.change_speed('30-')
    print(cat.under_thirty)


