from graphics import *

class ItemManage:
    """"""
    def add_items(self, key, value):
        self._items[key] = [value, {}]
    
    def _convert_coords(self, Ax, Ay, Bx, By, x, y):
        left = min(Ax, Bx)
        right = max(Ax, Bx)
        top = min(Ay, By)
        bottom = max(Ay, By)

        if left <= x <= right and top <= y <= bottom:
            return True
        
        return False
    
    def process_click(self, keyA, keyB, cords, item):
        self._items[keyA][1][keyB] = {'coordinates': cords, 'function': item}
    
    def verify_click(self, keyA, x, y):
        for coords in self._items[keyA][1].values():
            Ax, Ay, Bx, By = coords['coordinates']
            if self._convert_coords(Ax, Ay, Bx, By, x, y):
                coords['function'][0].draw(self.engine)


class Main(ItemManage):
    def __init__(self, TITLE: str, RESOLUTION: tuple):
        self.engine = GraphWin(TITLE, RESOLUTION[0], RESOLUTION[1])
        self._items = {}

    def draw_items(self, position, width, height, path, key):
        items = Image(Point(position[0] + width / 2, position[1] + height / 2), path)
        items.draw(self.engine)
        self.add_items(key, items)
    
    def draw_fontes(self, ):
        ...
                
    @property
    def items(self):
        return self._items


main = Main('DREAMPORT', (1280, 720))
