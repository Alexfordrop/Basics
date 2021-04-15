import turtle

p1 = turtle.Pen()
p2 = turtle.Pen()

p1.forward(200)
p2.left(90)
p2.forward(150)

class instruments_for_draw:
    def kto_roditel(self):
        print('Родитель: инструменты для рисования')
    pass

class pan(instruments_for_draw):
    pass

class paintprush(instruments_for_draw):
    def __init__(self, _price):
        self.my_price = _price
    def read_price(self):
        print('Моя цена: %s' % self.my_price)
    def write_price(self, _new_price):
        self.my_price = _new_price
    def kto_ya(self):
        print('Я кисточка')
    pass

obj1 = paintprush(205.57)
obj1.kto_ya()
obj1.kto_roditel()
obj1.read_price()
obj1.write_price(505.73)
obj1.read_price()

obj2 = paintprush(333.15)
obj2.read_price()