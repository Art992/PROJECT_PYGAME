import pygame
import sys


def Intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2 - db1) and (x1 < x2 + db2) and (y1 > y2 - db1) and (y1 < y2 + db2):
        return 1
    else:
        return 0


window = pygame.display.set_mode((800, 670))
pygame.display.set_caption('Menu')
screen = pygame.Surface((800, 640))
info = pygame.Surface((800, 30))


class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Menu:
    def __init__(self, punkts=[400, 350, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] - 30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] - 30))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            info.fill((0, 100, 200))
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        exit()
                    elif punkt == 2:
                        Draw()
                    elif punkt == 3:
                        Draw_2()
            window.blit(info, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()


class Draw:
    def __init__(self):
        super().__init__()
        self.draw()

    def draw(self):
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 255))
        font = pygame.font.Font(None, 50)
        text = font.render("Авторы", 1, (11, 0, 77))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass


class Draw_2:
    def __init__(self):
        super().__init__()
        self.draw()

    def draw(self):
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 200))
        font = pygame.font.Font(None, 50)
        text = font.render("Управление", 1, (11, 0, 77))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        screen.blit(text, (text_x, text_y))
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 0, 155), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass


pygame.font.init()
punkts = [(350, 260, u'Играть', (11, 0, 77), (0, 0, 204), 0),
          (310, 300, u'Управление', (11, 0, 77), (0, 0, 204), 3),
          (315, 340, u'Об авторах', (11, 0, 77), (0, 0, 204), 2),
          (350, 380, u'Выход', (11, 0, 77), (0, 0, 204), 1)]
game = Menu(punkts)
game.menu()
