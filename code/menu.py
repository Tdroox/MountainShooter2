import pygame
from code.Const import MENU_OPTIONS, WIN_WIDTH, COLOR_ORANGE, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assest/bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('assest/the_mountain-calm-507994.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.Menu_text(text_size=50, text="Mountain", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 70))
            self.Menu_text(text_size=50, text="Shooter", text_color=COLOR_ORANGE, text_center_pos=(WIN_WIDTH / 2, 120))

            for i in range(len(MENU_OPTIONS)):
                self.Menu_text(text_size=20, text=MENU_OPTIONS[i], text_color=C_WHITE,
                               text_center_pos=(WIN_WIDTH / 2, 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    # Um recuo (Tab) para a direita coloca a função dentro da classe Menu
    def Menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont(name="Arial", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

