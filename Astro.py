from ast import Constant
from calendar import LocaleHTMLCalendar 
import pygame
import math
from simpleeval import simple_eval
import sys


def vecsum(vect1, vect2):
    return (vect1[0] + vect2[0], vect1[1] + vect2[1])

def length(vect1):
    return math.sqrt(vect1[0] ** 2 + vect1[1] ** 2)

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] + pos2[1]) ** 2)


#a = int(simple_eval(input("The radius of the orbit(a.e.):"))) * 149.6 * 10 ** 9 #домножаем до метров
#i = int(simple_eval(input("The angle to the plane of the orbit:"))) / 57.29577951308 
#M1 = int(simple_eval(input("The mass of the first star(Mass of the Sun):"))) * 1.989 * 10 ** 30 #домножаем до кг
#M2 = int(simple_eval(input("The mass of the second star(Mass of the Sun):"))) * 1.989 * 10 ** 30 #домножаем до кг

a = 10 * 149.6 * 10 ** 9
i = 0 / 57.29577951308
M1 = 5 * 1.989 * 10 ** 30
M2 = 5 * 1.989 * 10 ** 30
G = 6.6743 * 10 ** -11

#первая звезда - красная
text1 = "Лучевая скорость, км/с"
text2 = "Время, с"


WIDTH = 800 #1 пиксель = 0.2 ае
HEIGHT = 600
FPS = 30
height_graf = 100
k_len = 10 / 149.6 / 10 ** 9 #отношение пикселей к реал длинеangle_F = 1
grid = 20 #четное
time = 0
fnt_size = 15

dt = 10 ** 7 * 3 / FPS
k_grafx = dt * 10 ** 2
dt = 10 ** 7 * 3 / FPS

#P = math.sqrt(4 * math.pi * 8 * a ** 3 / G / (M1 + M2)) #период
P1 = math.sqrt(4 * math.pi * 8 * a ** 3 / G / M1)
P2 = math.sqrt(4 * math.pi * 8 * a ** 3 / G / M2)

v01 = 2 * math.pi * a / P1
v02 = -1 * 2 * math.pi * a / P2
max_graf = abs(min(v02, v01) * math.sin(i)) #максимальное значение графика

if max_graf == 0:
    k_graf = 0
else:
    k_graf = (height_graf - 10) / max_graf

v1 = (0, 2 * math.pi * a / P1) #начальная скорость
v2 = (0, -1 * 2 * math.pi * a / P2) 
pos1 = (-1 * a, 0.01)
pos2 = (a, -0.01)
F1 = (0, 0)
F2 = (0, 0)

nol = (WIDTH / 2, HEIGHT / 2)
cen_graf = (WIDTH / 2, HEIGHT - height_graf)
pos_text1 = (nol[0], HEIGHT - 2 * height_graf)
pos_text2 = (WIDTH - 5 * fnt_size, HEIGHT - height_graf)



GRF_CLR = (197, 208, 230)
GRID_CLR = (10, 95, 173)
CLR1 = (253, 0, 110)
CLR2 = (25, 0, 253)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
nak = math.cos(i)
running = True
pygame.font.init()

path = pygame.font.match_font("arial")
Font = pygame.font.Font(path, fnt_size)
render_text1 = Font.render(text1, 1, (255, 255, 255))
render_text2 = Font.render(text2, 1, (255, 255, 255))

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    #математика
    vi_pos1 = (k_len * pos1[0] + nol[0], k_len * nak * pos1[1] + nol[1])
    vi_pos2 = (k_len * pos2[0] + nol[0], k_len * nak * pos2[1] + nol[1])
    angle_F = math.atan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]))
    F_mg = G * M1 * M2 / (distance(pos1, pos2) ** 2)
    F1 = (F_mg * math.cos(angle_F), 
          F_mg * math.sin(angle_F))

    
    F2 = (F1[0] * -1, F1[1] * -1)
    v1 = (v1[0] + F1[0] / M1 * dt, v1[1] + F1[1] / M1 * dt)    
    v2 = (v2[0] + F2[0] / M2 * dt, v2[1] + F2[1] / M2 * dt)
    pos1 = (pos1[0] + v1[0] * dt, pos1[1] + v1[1] * dt)
    pos2 = (pos2[0] + v2[0] * dt, pos2[1] + v2[1] * dt)
    
    #отрисовка
    screen.fill(BLACK)
    
    for I in range(0, int(grid / 2) + 1):   # сетка
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] + nak * HEIGHT / grid * I], [WIDTH, nol[1] + nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] - nak * HEIGHT / grid * I], [WIDTH, nol[1] - nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I, nol[1] + nol[1] * nak], [WIDTH / grid * I, nol[1] - nol[1] * nak])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I + nol[0], nol[1] + nol[1] * nak], [WIDTH / grid * I + nol[0], nol[1] - nol[1] * nak])

    #звезды
    pygame.draw.circle(screen, CLR1, vi_pos1, 7)
    pygame.draw.circle(screen, CLR2, vi_pos2, 7)
    
    #график
    time += dt #время в секундах

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 2 * height_graf, WIDTH, 2 * height_graf))
    pygame.draw.rect(screen, GRF_CLR, (0, HEIGHT - 2 * height_graf, WIDTH, 2 * height_graf), 5)
    pygame.draw.line(screen, GRF_CLR, (nol[0], HEIGHT - 2 * height_graf), (nol[0], HEIGHT))
    pygame.draw.line(screen, GRF_CLR, (0, HEIGHT - height_graf), (WIDTH, HEIGHT - height_graf))

    for i_graf in range(0, int(WIDTH)):
        y_1_1 = k_graf * v01 * math.cos(2 * math.pi * (time + k_grafx * i_graf / FPS) / P1) * math.sin(i)
        y_1_2 = k_graf * v01 * math.cos(2 * math.pi * (time + k_grafx * (i_graf - 1) / FPS) / P1) * math.sin(i)

        y_2_1 = k_graf * v02 * math.cos(2 * math.pi * (time + k_grafx * i_graf / FPS) / P2) * math.sin(i)
        y_2_2 = k_graf * v02 * math.cos(2 * math.pi * (time + k_grafx * (i_graf - 1) / FPS) / P2) * math.sin(i)


        pygame.draw.aaline(screen, CLR1, (WIDTH - i_graf, HEIGHT - height_graf + y_1_1), (WIDTH - i_graf - 1, HEIGHT - height_graf + y_1_2))

        pygame.draw.aaline(screen, CLR2, (WIDTH - i_graf, HEIGHT - height_graf + y_2_1), (WIDTH - i_graf - 1, HEIGHT - height_graf + y_2_2))


        screen.blit(render_text1, pos_text1)
        screen.blit(render_text2, pos_text2)
    #остальное
    pygame.display.flip()
    clock.tick(FPS)