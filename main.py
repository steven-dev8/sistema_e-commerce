from graphics import *

class Main:
    def __init__(self, TITLE: str, RESOLUTION: tuple):
        self.engine = GraphWin(TITLE, RESOLUTION[0], RESOLUTION[1])
        self._items = {}

    def draw_items(self, position, width, height, path, key):
        items = Image(Point(position[0] + width / 2, position[1] + height / 2), path)
        items.draw(self.engine)
        self._add_items(key, items)
    
    def draw_fontes(self, ):
        ...
    
    def _add_items(self, key, value):
        if self._items.get(key):
            self._items[key].append(value)
        else:
            self._items[key] = [value, {}]


main = Main('DREAMPORT', (1277, 720))

while True:
    main.draw_items((0, 0), 1280, 720, 'image\homepage1.ppm', 'homepage')
    position = main.engine.getMouse()
    print(f'X: {position.getX()}, Y: {position.getY()}')