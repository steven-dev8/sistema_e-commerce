from graphics import *
from config import *
import csv
from time import sleep

class ItemManage:
    """
    Essa classe serve para gerenciar os Items, ou páginas, que vão ser desenhadas na página

    Atributos: 
    self._current_screen: guarda como string a tela atual que está sendo exibida
    self._items: um dicionário que guarda, as funcionalidades da página
    """

    def __init__(self):
        self._current_screen = None
        self._items = {}

    def _add_items(self, key, value):
        """essa função adiciona páginas no dicionários self._items"""
        self._items[key] = [value, {}]
    
    def set_current_screen(self, key):
        """configura a tela atual de forma bruta"""
        self._current_screen = key
    
    def _clear_screen(self, key):
        """limpa a tela atual"""
        self._items[key][0].undraw()
    
    def _convert_coords(self, Ax, Ay, Bx, By, x, y):
        """função para conversão das coordenadas e checar se o click foi feito naquela área"""
        left = min(Ax, Bx)
        right = max(Ax, Bx)
        top = min(Ay, By)
        bottom = max(Ay, By)

        if left <= x <= right and top <= y <= bottom:
            return True
        
        return False

class Click(ItemManage):
    """
    Essa classe gerencia os clicks do usuário na tela, redirecionando a outras páginas e executando mini animações
    """

    def process_click(self, keyA, keyB, cords, path,  item):
        """Cria funcionalidades na página, recebendo a área a ser clicada, a animação e a página a ser redirecionado"""
        x, y = self._format_screen((0, 0), self._resolution[0], self._resolution[1])
        self._items[keyA][1][keyB] = {'coordinates': cords, 
                                      'function': Image(Point(x, y), path),
                                      'redirect': item}
    
    def verify_click(self, x, y):
        """executa as ações em uma área registrada"""
        for coords in self._items[self._current_screen][1].values():
            Ax, Ay, Bx, By = coords['coordinates']
            if self._convert_coords(Ax, Ay, Bx, By, x, y):
                coords['function'].draw(self.engine) # Desenhar a animação
                self._clear_screen(self._current_screen)
                sleep(0.1)
                self._items[coords['redirect']][0].draw(self.engine) # Desenha a página
                coords['function'].undraw()
                self._current_screen = coords['redirect']
    
    def _format_screen(self, position, width, height):
        """centraliza a página"""
        return position[0] + width / 2, position[1] + height / 2
        

class Main(Click):
    """
    Essa classe serve para o gerenciamento da janela, que usa a biblioteca Graphics
    Atributos:
    self._engine: motor do programa, onde tudo vai ser desenhado
    self._resolution: guarda informações da resolução
    """
    def __init__(self, TITLE: str, RESOLUTION: tuple):
        super().__init__()
        self.engine = GraphWin(TITLE, RESOLUTION[0], RESOLUTION[1])
        self._resolution = RESOLUTION

    def draw_items(self, position, resolution, path, key):
        items = Image(Point(position[0] + resolution[0] / 2, position[1] + resolution[1] / 2), path)
        self._add_items(key, items)
        if key == self._current_screen:
            items.draw(self.engine)
        
    def draw_fontes(self):
        ...
    
    @property
    def items(self):
        
        return self._items

class FileProduct:
    def __init__(self):
        self.matriz = []

    def _open_file(self, path):
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)

            for rows in csv_reader:
                self.matriz.append(rows)
    
    def _search_product(self, name):
        for item in self.matriz:
            ...


main = Main(TITLE, SCREEN_RESOLUTION)

# Carregando as imagens de cada página
main.set_current_screen('login')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, LOGIN_IMG, 'login')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, HOMEPAGE_IMG, 'homepage')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, MENU_IMG, 'menu')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, PRODUCT_IMAGE, 'product')

# Página de Login
main.process_click('login', 'button_pass', LOGIN_PASS_COORDS, LOGIN_PASS_ANI , 'homepage')

# Homepage
main.process_click('homepage', 'button_menu', HOMEPAGE_MENU_COORDS, HOMEPAGE_MENU_ANI, 'homepage')
main.process_click('homepage', 'button_product', HOMEPAGE_PRODUCT_COORDS, HOMEPAGE_PRODUCT_ANI , 'product')

# Pagina do Produto 
main.process_click('product', 'button_menu', PRODUCT_MENU_COORDS, PRODUCT_MENU_ANI , 'homepage')


while True:
    position = main.engine.getMouse()
    x, y = position.getX(), position.getY()
    main.verify_click(x, y)
