import pygame as pg, sys
from pygame.locals import QUIT

class PlayerName():
    def __init__(self):
        self._name = ""

    def _spawn_dialog(self) -> None:
        pg.init()
        pg.display.set_caption('Enter your name below and press Enter to submit!')
        clock = pg.time.Clock()
        screen = pg.display.set_mode([800,800])
        base_font = pg.font.Font(None,32)
        
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        if self._name:
                            return None
                    elif event.key == pg.K_BACKSPACE:
                        self._name = self._name.rstrip(self._name[-1])
                    elif event.key == pg.K_SPACE:
                        self._name += event.unicode
                    else:    
                        if event.unicode.isalpha():
                                self._name += event.unicode
                    
            screen.fill((0,0,0))
            text_surface = base_font.render(self._name, True, (255,255,255))
            screen.blit(text_surface, (0,0))
            
            pg.display.flip()
            clock.tick(30)

    def _change_name(self, newName):
        self._name = newName

    @property
    def name(self) -> str:
        return self._name