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
score_player_1 = Score(points=0, posx=260, posy=30)

player_2 = Rect_player(posx=screen_size_x - player_size_x, posy=screen_size_y//2, widith=player_size_x, height=player_size_y, color='red', speed=player_speed)
score_player_2 = Score(points=0, posx=980, posy=30)

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
    if game_event.identify_key_w() and player_1.posy >= 0:
        player_1.move_up()
    if game_event.identify_key_s() and player_1.posy <= screen_size_y - player_size_y:
        player_1.move_down()

    # Desenha o player 2
    player_2.draw_player(screen=game_screen.game_window)
    if game_event.identify_key_up() and player_2.posy >= 0:
        player_2.move_up()
    if game_event.identify_key_down() and player_2.posy <= screen_size_y - player_size_y:
        player_2.move_down()

    # Desenha a bola
    ball.draw_ball(screen=game_screen.game_window)

    # Identifica se a bola está sem movimento
    if direction_selector == start:
        direction_selector = randint(1, 2)

    # Escolhe para onde a Bola vai se mexer
    ball.move_ball_to_direction(direction=direction_selector)

    # Testa se alguém marcou
    score_tester = ball.set_collision_width(screen_size_x=screen_size_x)
    if score_tester == 'left':
        score_player_2.increment_points(increment_value=1)
        direction_selector = start
        ball.change_ball_position(posx=screen_size_x//2, posy=screen_size_y//2)
        pg.time.wait(1000)

    elif score_tester == 'right':
        score_player_1.increment_points(increment_value=1)
        direction_selector = start
        ball.change_ball_position(posx=screen_size_x//2, posy=screen_size_y//2)
        pg.time.wait(1000)
    score_tester = ''
    
    # Testa a colisão da bola com o player 1
    player_1_collided = ball.crash_test_player_left(player=player_1)
    if player_1_collided:
        if direction_selector == down_left:
            direction_selector = down_right

        elif direction_selector == up_left:
            direction_selector = up_right

    # testa a colisão da bola com o player 2
    player_2_collided = ball.crash_test_player_right(player=player_2)
    if player_2_collided:
        if direction_selector == down_right:
            direction_selector = down_left

        elif direction_selector == up_right:
            direction_selector = up_left

    # Identifica se a bola colidiu com o teto ou com o solo
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

    # Desenha o Placar
    score_player_1.draw_score(screen=game_screen.game_window)
    score_player_2.draw_score(screen=game_screen.game_window)

    pg.display.flip()

    # Limita o FPS
    clock.tick(60)



pg.quit()
