import pygame as pg
from pong_func import *

pg.init()

# Dimensões da tela
screen_size_x = 1280
screen_size_y = 720

# Criação da tela
game_screen = Window_display(xproportion=screen_size_x, yproportion=screen_size_y)
game_screen.create_display()

# Dimensões do Player
player_size_x = 30
player_size_y = 100

# Criando os Players
player_1 = Rect_player(posx=0, posy=screen_size_y//2, widith=player_size_x, height=player_size_y, color='green')
player_2 = Rect_player(posx=screen_size_x - player_size_x, posy=screen_size_y//2, widith=player_size_x, height=player_size_y, color='red')

# Controla a velocidade do jogo
player_speed = 5
ball_speed = 0

clock = pg.time.Clock()

# Identificador de eventos
game_event = Game_Event()

running = True
while running:

    # Identificando as teclas usadas    
    key_list = pg.event.get()
    running = game_event.identify_loop_close(keys=key_list)

    game_screen.change_background_color()

    player_1.draw_player(screen=game_screen.game_window)
    if game_event.identify_key_up() and player_1.posy >= 0:
        player_1.move_up(speed=player_speed)
    if game_event.identify_key_down() and player_1.posy <= screen_size_y - player_size_y:
        player_1.move_down(speed=player_speed)

    player_2.draw_player(screen=game_screen.game_window)

    pg.display.flip()

    clock.tick(60)



pg.quit()
