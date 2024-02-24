import pygame as pg
from random import randint
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

# Controla as velocidades do jogo
player_speed = 5
ball_speed = 5

# Criando os Players
player_1 = Rect_player(posx=0, posy=screen_size_y//2, widith=player_size_x, height=player_size_y, color='green', speed=player_speed)
player_2 = Rect_player(posx=screen_size_x - player_size_x, posy=screen_size_y//2, widith=player_size_x, height=player_size_y, color='red', speed=ball_speed)

# Características da bola
ray = 10
ball_color = 'purple'

# Criando a bola
ball = Ball(ray=ray, posx=screen_size_x//2, posy=screen_size_y//2, color=ball_color, speed=ball_speed)

# Relógio do jogo
clock = pg.time.Clock()

# Identificador de eventos
game_event = Game_Event()

# Seletor de movimentos
start = 0
up_left = 1
down_left = 2
up_right =  3
down_right = 4
direction_selector = start

running = True
while running:

    # Identificando as teclas usadas    
    key_list = pg.event.get()
    running = game_event.identify_loop_close(keys=key_list)

    # Preenche o background
    game_screen.change_background_color()

    # Desenha o player 1
    player_1.draw_player(screen=game_screen.game_window)
    if game_event.identify_key_up() and player_1.posy >= 0:
        player_1.move_up()
    if game_event.identify_key_down() and player_1.posy <= screen_size_y - player_size_y:
        player_1.move_down()

    # Desenha o player 2
    player_2.draw_player(screen=game_screen.game_window)

    # Desenha a bola
    ball.draw_ball(screen=game_screen.game_window)


    if direction_selector == start:
        direction_selector = randint(1, 2)

    ball.move_ball_to_direction(direction=direction_selector)

    score_tester = ball.set_collision_width(screen_size_x=screen_size_x)
    if score_tester == 'left':
        direction_selector = start
        ball.change_ball_position(posx=screen_size_x//2, posy=screen_size_y//2)
        pg.time.wait(1000)

    elif score_tester == 'right':
        direction_selector = start
        ball.change_ball_position(posx=screen_size_x//2, posy=screen_size_y//2)
        pg.time.wait(1000)
    score_tester = ''
    
    player_1_collided = ball.crash_test_player(player=player_1)
    if player_1_collided:
        if direction_selector == down_left:
            direction_selector = down_right

        elif direction_selector == up_left:
            direction_selector = up_right


    if ball.posx - ball.ray == player_1.return_x_pos() + player_1.xsize and player_1.return_y_pos() <= ball.posy and ball.posy <= player_1.return_y_pos() + player_size_y:
        print('Colidiu')

    height_finish_tester = ball.set_collision_height(screen_size_y=screen_size_y)
    if height_finish_tester == 'up':
        if direction_selector == down_right:
            direction_selector = up_right

        elif direction_selector == down_left:
            direction_selector = up_left

    elif height_finish_tester == 'down':
        if direction_selector == up_right:
            direction_selector = down_right

        elif direction_selector == up_left:
            direction_selector = down_left
    height_finish_tester = ''



    pg.display.flip()

    clock.tick(60)



pg.quit()
