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
    def __init__(self, posx, posy, widith, height, color, speed) -> None:
        self.posx = posx
        self.posy = posy
        self.xsize = widith
        self.ysize = height
        self.color= color
        self.speed = speed

    def move_up(self) -> None:
        self.posy -= self.speed

    def move_down(self) -> None:
        self.posy += self.speed
        
    def return_x_pos(self) -> int:
        return self.posx
    
    def return_y_pos(self) -> int:
        return self.posy
    
    def draw_player(self, screen) -> None:
        pg.draw.rect(color=self.color, surface=screen, rect=((self.posx, self.posy), (self.xsize, self.ysize)))

class Ball:
    def __init__(self, ray, posx, posy, color, speed) -> None:
        self.ray = ray
        self.posx = posx
        self.posy = posy
        self.color = color
        self.speed = speed

    def move_ball_up_right(self) -> None:
        self.posx += self.speed
        self.posy -= self.speed

    def move_ball_up_left(self) -> None:
        self.posx -= self.speed
        self.posy -= self.speed

    def move_ball_down_right(self) -> None:
        self.posx += self.speed
        self.posy += self.speed

    def move_ball_down_left(self) -> None:
        self.posx -= self.speed
        self.posy += self.speed

    def draw_ball(self, screen) -> None:
        pg.draw.circle(color=self.color, surface=screen, center=[self.posx, self.posy], radius=self.ray)
        
    def set_start(self, screen_size_x, screen_size_y) -> bool:
        if self.posx == screen_size_x//2 and screen_size_y//2:
            return True
        else:
            return False
        
    def set_finish_height(self, screen_size_y) -> str:
        if self.posy == 0:
            return 'down'
        elif self.posy == screen_size_y - self.ray:
            return 'up'

    def set_finish_width(self, screen_size_x) -> str:
        if self.posx == 0:
            return 'left'
        elif self.posx == screen_size_x - self.ray:
            return 'right'

class Score:
    def __init__(self, points=int) -> None:
        self.points = points
        
    def increment_points(self, increment_value) -> None:
        self.points += increment_value
        
    def return_score(self) -> int:
        return self.points
        