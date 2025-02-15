from graphics import *
from config import *
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
        self._fontes = {}

    def draw_items(self, position, resolution, path, key):
        items = Image(Point(position[0] + resolution[0] / 2, position[1] + resolution[1] / 2), path)
        self._add_items(key, items)
        if key == self._current_screen:
            items.draw(self.engine)
        
    def draw_fontes(self, coord, text):
        for coords in coord: 
            ...
    
    @property
    def items(self):
        
        return self._items
    
# Em desenvolvimento
class Product:
    def __init__(self, lista):
        self.nome = lista[1]
        self.preco = lista[2]
        self.classe = lista[3]

# Em desenvolvimento
class ManageProduct:
    def __init__(self, path):
        self.products = dict()
        self.path = path
        self._open_file()

    def open_file(self):
        with open(self.path, 'r') as file:
            file = file.readlines()
            file = [lista.strip().split(';') for lista in file]

            for num, item in enumerate(file):
                if num != 0:
                    self.products[item[0]] = item[1:]
    
    def save_file(self):
        with open(self.path, 'w') as file:
            inicio = ['id', 'nome', 'preco', 'categoria']
            file.write(';'.join(inicio) + '\n')

            for cod in self.products.keys():
                produto = self.products[cod]
                linha = [str(cod), produto.nome, produto.preco, produto.classe]
                file.write(';'.join(linha) + '\n')


main = Main(TITLE, SCREEN_RESOLUTION)

# Carregando as imagens de cada página
main.set_current_screen('inicio')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, HOMEPAGE_IMG, 'inicio')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, MENU_IMG, 'menu')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, PRODUCT_IMAGE, 'produto')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, ABOUT_IMG, 'sobre')
main.draw_items(DEFAULT_COORDS, SCREEN_RESOLUTION, CART_IMG, 'carrinho')

# Áreas clicaveis - inicio
main.process_click('inicio', 'botao_menu', HOMEPAGE_MENU_COORDS, HOMEPAGE_MENU_ANI, 'inicio')
main.process_click('inicio', 'botao_secao', HOMEPAGE_SECAO_COORDS, HOMEPAGE_SECAO_ANI, 'secao')
main.process_click('inicio', 'botao_inicio', HOMEPAGE_INICIO_COORDS, HOMEPAGE_INICIO_ANI, 'inicio')
main.process_click('inicio', 'botao_secao', HOMEPAGE_CARRINHO_COORDS, HOMEPAGE_CARRINHO_ANI, 'carrinho')
main.process_click('inicio', 'botao_sobre', HOMEPAGE_SOBRE_COORDS, HOMEPAGE_SOBRE_ANI, 'sobre')
main.process_click('inicio', 'produto1', HOMEPAGE_PRODUCT1_COORDS, HOMEPAGE_IMG, 'produto')
main.process_click('inicio', 'produto2', HOMEPAGE_PRODUCT2_COORDS, HOMEPAGE_IMG, 'produto')
main.process_click('inicio', 'produto3', HOMEPAGE_PRODUCT3_COORDS, HOMEPAGE_IMG, 'produto')
main.process_click('inicio', 'produto4', HOMEPAGE_PRODUCT4_COORDS, HOMEPAGE_IMG, 'produto')

# Áreas clicaveis - carrinho
main.process_click('carrinho', 'botao_menu', CART_MENU_COORDS, CART_MENU_ANI, 'inicio')
main.process_click('carrinho', 'botao_secao', CART_SECAO_COORDS, CART_SECAO_ANI, 'secao')
main.process_click('carrinho', 'botao_inicio', CART_INICIO_COORDS, CART_INICIO_ANI, 'inicio')
main.process_click('carrinho', 'botao_secao', CART_CARRINHO_COORDS, CART_CARRINHO_ANI, 'carrinho')
main.process_click('carrinho', 'botao_sobre', CART_SOBRE_COORDS, CART_SOBRE_ANI, 'sobre')

# Áreas clicaveis - sobre
main.process_click('sobre', 'botao_menu', ABOUT_MENU_COORDS, ABOUT_MENU_ANI, 'inicio')
main.process_click('sobre', 'botao_secao', ABOUT_SECAO_COORDS, ABOUT_SECAO_ANI, 'secao')
main.process_click('sobre', 'botao_inicio', ABOUT_INICIO_COORDS, ABOUT_INICIO_ANI, 'inicio')
main.process_click('sobre', 'botao_secao', ABOUT_CARRINHO_COORDS, ABOUT_CARRINHO_ANI, 'carrinho')
main.process_click('sobre', 'botao_sobre', ABOUT_SOBRE_COORDS, ABOUT_SOBRE_ANI, 'sobre')

# Áreas clicaveis - produto
main.process_click('produto', 'botao_menu', PRODUCT_MENU_COORDS, PRODUCT_MENU_ANI, 'inicio')
main.process_click('produto', 'botao_secao', PRODUCT_SECAO_COORDS, PRODUCT_SECAO_ANI, 'secao')
main.process_click('produto', 'botao_inicio', PRODUCT_INICIO_COORDS, PRODUCT_INICIO_ANI, 'inicio')
main.process_click('produto', 'botao_secao', PRODUCT_CARRINHO_COORDS, PRODUCT_CARRINHO_ANI, 'carrinho')
main.process_click('produto', 'botao_sobre', PRODUCT_SOBRE_COORDS, PRODUCT_SOBRE_ANI, 'sobre')

while True:
    position = main.engine.getMouse()
    x, y = position.getX(), position.getY()
    print(x, y)
    main.verify_click(x, y)