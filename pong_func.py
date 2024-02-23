import pygame as pg

pg.init()

class Window_display:
    def __init__(self, xproportion, yproportion):
        self.propx = xproportion
        self.propy = yproportion

    def create_display(self) -> None:
        self.game_window = pg.display.set_mode((self.propx, self.propy))
        
    def change_background_color(self, color_background='#020526') -> None:
        self.game_window.fill(color= color_background)

class Game_Event:    
    def __init__(self) -> None:
        self.keys = pg.event.get()
    
    def identify_loop_close(self, keys) -> bool:
        self.keys = keys
        if self.keys != []:
            for event in self.keys:
                if event.type == pg.QUIT:
                    return False
        return True
    
    def identify_key_up(self) -> bool:
        self.keys_pressed = pg.key.get_pressed()
        if self.keys_pressed[pg.K_w] or self.keys_pressed[pg.K_UP]:
            return True
    
    def identify_key_down(self) -> bool:
        self.keys_pressed = pg.key.get_pressed()
        if self.keys_pressed[pg.K_s] or self.keys_pressed[pg.K_DOWN]:
            return True

class Rect_player:
    def __init__(self, posx, posy, widith, height, color) -> None:
        self.posx = posx
        self.posy = posy
        self.xsize = widith
        self.ysize = height
        self.color= color
        
    def move_up(self, speed) -> None:
        self.posy -= speed

    def move_down(self, speed) -> None:
        self.posy += speed
        
    def return_x_pos(self) -> int:
        return self.posx
    
    def return_y_pos(self) -> int:
        return self.posy
    
    def draw_player(self, screen) -> None:
        pg.draw.rect(color=self.color, surface=screen, rect=((self.posx, self.posy), (self.xsize, self.ysize)))

class Ball:
    def __init__(self) -> None:
        pass

    
class Score:
    def __init__(self, points=int) -> None:
        self.points = points
        
    def increment_points(self, increment_value) -> None:
        self.points += increment_value
        
    def return_score(self) -> int:
        return self.points
        