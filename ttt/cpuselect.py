import pygame as pg, sys
import pygame_gui as pgui
from pygame.locals import QUIT

from ttt.colors import * 

OPT_HOTSEAT = 'HOTSEAT'
OPT_CPU = 'CPU'

class CpuSelect: 
    '''
    A class that represents the dialog that pops up when the game is first run.
    The dialogue asks the user whether they want to play a hotseat game or 
    against the computer.
    '''
    
    def __init__(self): 
        '''
        Constructor for the CpuSelect object.
        '''
        self._spawn_dialog()

    def is_hotseat(self) -> str: 
        '''
        Spawns a dialogue that has two buttons:
        + [Hotseat]: PvP mode 
        + [Solo]: PvCPU mode 

        Returns:
            is_hotseat (bool): True if the user clicks [Hotseat]
                               False if the user clicks [Solo]
        '''

        click_result = self._listen_for_clicks()

        return click_result


    def _spawn_dialog(self) -> None: 
        '''
        Helper function for spawning the dialog.
        '''
        
        # Wouldn't this conflict with board.py's own init() call? i don't know.
        # Maybe "de-init" the pygame before returning True or False in
        # is_hotseat() to keep it from conflicting? Is that even a thing? 
        
        pg.init()  
        pg.display.set_caption('Select Gamemode') 

        window_size = (800, 600)   # change this size later
        self._window = pg.display.set_mode(window_size)

        self.background = pg.Surface(window_size)
        self.background.fill(BLACK)
        self._manager = pgui.UIManager((800, 600))
        
        self._btn_hotseat = pgui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)), text='PvP', manager=self._manager)
        self._btn_cpu = pgui.elements.UIButton(relative_rect=pg.Rect((350, 225), (100, 50)), text='Solo', manager=self._manager)
        self._btn_exit = pgui.elements.UIButton(relative_rect=pg.Rect((350, 325), (100, 50)), text='Exit', manager=self._manager)

    def _listen_for_clicks(self) -> str: 
        '''
        Helper function for listening to clicks. 

        Returns: 
            option (str): OPT_HOTSEAT if [Hotseat] was clicked
                          OPT_CPU if [Solo] was clicked 
        '''
        clock = pg.time.Clock()
        while True:
            timer = clock.tick(60)/1000.0
            for event in pg.event.get(): 
                if event.type == pg.USEREVENT:
                    if event.user_type == pgui.UI_BUTTON_PRESSED:
                        if event.ui_element == self._btn_hotseat: 
                            return OPT_HOTSEAT
                        elif event.ui_element == self._btn_cpu: 
                            return OPT_CPU
                        elif event.ui_element == self._btn_exit:
                            pg.quit()
                            sys.exit()
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                self._manager.process_events(event)
            self._update_ui(timer)
            
    def _update_ui(self, timer) -> None:
        '''
        Helper function for updating selection screen with buttons
        '''
        self._manager.update(timer)
        self._window.blit(self.background, (0, 0))
        self._manager.draw_ui(self._window)
        pg.display.update()
    
    # Function not used at the moment, may be potentially used when we implement Exit Button
    '''
    def _destroy_dialog(self) -> None: 
        
        Helper function for destroying the current dialogue. 
        Do we have to "de-init" pygame for when Board.py takes over? I don't know. 
        
        self._window.quit()   # uhh, does this exist? 
    '''
