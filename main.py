import pygame as pg
from random import randrange
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

color_ = (255, 255, 255)
balls = 0
waters = 0

def S_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 25)
    shape.color = pg.Color('gray')
    space.add(body, shape)

def Seg(pos_1, pos_2):
    segment_shape = pymunk.Segment(space.static_body, (pos_1), (pos_2), 20)
    segment_shape.elasticity = 0.5
    segment_shape.friction = 0.2
    segment_shape.color = pg.Color('white')
    space.add(segment_shape)

def Box(space, pos, color):
    box_mass, box_size = 4825, (50, 50)
    box_moment = pymunk.moment_for_box(box_mass, box_size)
    box_body = pymunk.Body(box_mass, box_moment)
    box_body.position = pos
    box_shape = pymunk.Poly.create_box(box_body, box_size)
    box_shape.elasticity = 0.4
    box_shape.friction = 0.5
    box_shape.color = pg.Color(color)
    space.add(box_body, box_shape)

def Water(space, pos, color):
    print("Water =", waters)
    ball_mass, ball_radius = 2.5, 5
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.4
    ball_shape.friction = 0.5
    if waters < 350:
        ball_shape.color = color_
    else:
        ball_shape.color = pg.Color(color)
    space.add(ball_body, ball_shape)

def Sand(space, pos, color):
    print("\t\t  Balls =", balls)
    ball_mass, ball_radius = 10, 12
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.4
    ball_shape.friction = 0.5
    if balls < 550:
        ball_shape.color = color_
    else:
        ball_shape.color = pg.Color(color)

    space.add(ball_body, ball_shape)

def seg_1():
    segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT // 4), (WIDTH // 2, HEIGHT), 20)
    segment_shape.elasticity = 0.5
    segment_shape.friction = 0.2
    space.add(segment_shape)

def seg_2():
    segment_shape = pymunk.Segment(space.static_body, (WIDTH, HEIGHT // 4), (WIDTH // 2, HEIGHT), 20)
    segment_shape.elasticity = 0.5
    segment_shape.friction = 0.2
    space.add(segment_shape)

def Segment_Down_1():
    segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
    segment_shape.elasticity = 0.5
    segment_shape.friction = 0.2
    space.add(segment_shape)

def Segment_Left_1():

    segment_shape_2 = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, -HEIGHT * 250), 20)
    segment_shape_2.elasticity = 0.5
    segment_shape_2.friction = 0.2
    space.add(segment_shape_2)

def Segment_Right_1():

    segment_shape_2 = pymunk.Segment(space.static_body, (WIDTH, 700), (WIDTH, -HEIGHT * 250), 20)
    segment_shape_2.elasticity = 0.5
    segment_shape_2.friction = 0.2
    space.add(segment_shape_2)


RES = WIDTH, HEIGHT = 1350, 700
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)

clock = pg.time.Clock()

space = pymunk.Space()
space.gravity = 0, 2000
draw_options = pymunk.pygame_util.DrawOptions(surface)

Segment_Down_1()
Segment_Left_1()
Segment_Right_1()
seg_1()
seg_2()

while True:

    surface.fill(pg.Color('black'))
    color_ = [randrange(256) for i in range(4)]
    keys = pg.key.get_pressed()

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()

    if i.type == pg.MOUSEBUTTONDOWN:
        if i.button == 1:
            if keys[pg.K_b]:
                Box(space, i.pos, 'gold')
            elif keys[pg.K_s]:
                Seg(i.pos, i.pos)
            elif keys[pg.K_j]:
                S_ball(space, i.pos)
            elif keys[pg.K_w]:
                Water(space, i.pos, 'blue')
                waters += 1
                if waters == 1 or waters % 5 == 0:
                    Water(space, i.pos, 'blue')
                if keys[pg.K_m]:
                    Water(space, i.pos, 'blue')  # 1
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 2
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 3
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 4
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 5
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 6
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 7
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 8
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 9
                    color_ = [randrange(256) for i in range(4)]
                    Water(space, i.pos, 'blue')  # 10
                    waters += 10
                    if waters == 1 or waters % 5 == 0:
                        Water(space, i.pos, 'blue')
            else:
                Sand(space, i.pos, 'red')
                balls += 1
                if balls == 1 or balls % 5 == 0:
                    Sand(space, i.pos, 'red')
                if keys[pg.K_m]:
                    Sand(space, i.pos, 'red')  # 1
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 2
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 3
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 4
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 5
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 6
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 7
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 8
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 9
                    color_ = [randrange(256) for i in range(4)]
                    Sand(space, i.pos, 'red')  # 10
                    balls += 10

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    pg.display.flip()
    clock.tick(FPS)