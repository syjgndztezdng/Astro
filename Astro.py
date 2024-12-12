from ast import Constant
from calendar import LocaleHTMLCalendar
import pygame
import math
import scipy #для физических констант
from simpleeval import simple_eval


def vecsum(vect1, vect2):
    return (vect1[0] + vect2[0], vect1[1] + vect2[1])

def length(vect1):
    return math.sqrt(vect[0] ** 2 + vect[1] ** 2)

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] + pos2[1]) ** 2)


#a = int(simple_eval(input("The radius of the orbit(a.e.):"))) * 149.6 * 10 ** 6
#i = int(simple_eval(input("The angle to the plane of the orbit:"))) / 57.29577951308
#M1 = int(simple_eval(input("The mass of the first star(Mass of the Sun):"))) * 1.989 * 10 ** 30
#M2 = int(simple_eval(input("The mass of the second star(Mass of the Sun):"))) * 1.989 * 10 ** 30

a = 10 * 149.6 * 10 ** 6
i = 0 / 57.29577951308
M1 = 5 * 1.989 * 10 ** 30
M2 = 5 * 1.989 * 10 ** 30

#первая звезда - красная

WIDTH = 800 #1 пиксель = 0.2 ае
HEIGHT = 600
FPS = 30
height_graf = 100
k_grafx = 10 ** 3
koef = 10 ** 6
koef1 = 15
k_len = 10 / 149.6 / 10 ** 6 #отношение пикселей к реал длине
angle_F = 1
nak = 0
grid = 20 #четное
time = 0

P = math.sqrt(4 * math.pi * a ** 3 / scipy.constants.G / (M1 + M2)) #период
V0 = 2 * math.pi * a / P #скалярная величина круг. скорости
if i = 0:
    k_graf = 0
else:
    max_graf = abs(V0 * math.sin(i)) #максимальное значение графика
    k_graf = (height_graf - 10) / max_graf
v1 = (0, koef1 * math.sqrt(scipy.constants.G * M1 / a)) #начальная скорость
v2 = (0, -1 * koef1 * math.sqrt(scipy.constants.G * M2 / a)) 
pos1 = (-1 * a, 0.01)
pos2 = (a, -0.01)
F1 = (0, 0)
F2 = (0, 0)

nol = (WIDTH / 2, HEIGHT / 2)
cen_graf = (WIDTH / 2, HEIGHT - height_graf)
T = math.sqrt((4 * math.pi ** 2 * a ** 3) / scipy.constants.G * (M1 + M2))

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


while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    #математика
    angle_F = math.atan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]))
    F_mg = (scipy.constants.G / 1000) * M1 * M2 / (distance(pos1, pos2) ** 2)
    F1 = (F_mg * math.cos(angle_F), 
          F_mg * math.sin(angle_F))

    
    F2 = (F1[0] * -1, F1[1] * -1)
    v1 = (v1[0] + F1[0] / M1 * koef, v1[1] + F1[1] / M1 * koef)    
    v2 = (v2[0] + F2[0] / M2 * koef, v2[1] + F2[1] / M2 * koef)
    pos1 = (pos1[0] + v1[0], pos1[1] + v1[1])
    pos2 = (pos2[0] + v2[0], pos2[1] + v2[1])
    
    #отрисовка
    screen.fill(BLACK)
    
    for I in range(0, int(grid / 2) + 1):   # сетка
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] + nak * HEIGHT / grid * I], [WIDTH, nol[1] + nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] - nak * HEIGHT / grid * I], [WIDTH, nol[1] - nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I, nol[1] + nol[1] * nak], [WIDTH / grid * I, nol[1] - nol[1] * nak])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I + nol[0], nol[1] + nol[1] * nak], [WIDTH / grid * I + nol[0], nol[1] - nol[1] * nak])

    #звезды
    pygame.draw.circle(screen, CLR1, [k_len * pos1[0] + nol[0], k_len * nak * pos1[1] + nol[1]], 7)
    pygame.draw.circle(screen, CLR2, [k_len * pos2[0] + nol[0], k_len * nak * pos2[1] + nol[1]], 7)
    
    #график
    time += 1 / FPS #время в секундах

    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 2 * height_graf, WIDTH, 2 * height_graf))
    pygame.draw.rect(screen, GRF_CLR, (0, HEIGHT - 2 * height_graf, WIDTH, 2 * height_graf), 5)

    for i_graf in range(0, int(nol[0]) + 1):
        y1 = k_graf * V0 * math.cos(2 * math.pi * (time + k_grafx * i_graf / FPS) / P) * math.sin(i)
        y2 = k_graf * V0 * math.cos(2 * math.pi * (time + k_grafx * (i_graf - 1) / FPS) / P) * math.sin(i)
        pygame.draw.line(screen, CLR1, (nol[0] - i_graf, HEIGHT - height_graf - y1), (nol[0] - i_graf - 1, HEIGHT - height_graf - y2))
    #остальное
    pygame.display.flip()
    clock.tick(FPS)

