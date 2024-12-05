import pygame
import math
import scipy #��� ��������
from simpleeval import simple_eval

#������� ��������� ��, ���, ��

def vecsum(vect1, vect2):
    return (vect1[0] + vect2[0], vect1[1] + vect2[1])

def length(vect1):
    return math.sqrt(vect[0] ** 2 + vect[1] ** 2)

def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] + pos2[1]) ** 2)

a = int(simple_eval(input("The radius of the orbit(a.e.):"))) * 149.6 * 10 ** 6
i = int(simple_eval(input("The angle to the plane of the orbit:"))) / 57.29577951308
M1 = int(simple_eval(input("The mass of the first star(Mass of the Sun):"))) * 1.989 * 10 ** 30
M2 = int(simple_eval(input("The mass of the second star(Mass of the Sun):"))) * 1.989 * 10 ** 30

WIDTH = 800 #1 ������� = 0.2 ��
HEIGHT = 700
FPS = 30
height_graf = 50
koef = 10 ** 5
k_len = 5 / 149.6 / 10 ** 6 #���� ��� ��������� �� � �������(��)
angle_F = 1
nak = 0
grid = 20 #������

P = math.sqrt(4 * math.pi * a ** 3 / scipy.constants.G / (M1 + M2)) #�� �������
v1 = (0, math.sqrt(scipy.constants.G * M1 / a)) #�������� �������
v2 = (0, math.sqrt(scipy.constants.G * M2 / a)) #�������� �������
pos1 = (-1 * a, 10 / k_len)
pos2 = (a, -10 / k_len)
F1 = (0, 0)
F2 = (0, 0)

nol = (WIDTH / 2, HEIGHT / 2)
cen_graf = (WIDTH / 2, HEIGHT - height_graf)
T = math.sqrt((4 * math.pi ** 2 * a ** 3) / scipy.constants.G * (M1 + M2))

GRID_CLR = (0, 0, 100)
CLR1 = (253, 0, 110)
CLR2 = (25, 0, 253)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)
# ������� ���� � ����
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# ���� ����
nak = math.cos(i)
running = True
while running:
    for event in pygame.event.get():
        # ��������� �������� ����
            if event.type == pygame.QUIT:
                running = False
    #���������a
    angle_F = math.atan((pos1[0] - pos2[0]) / (pos1[1] - pos2[1]))
    F1 = (scipy.constants.G / 1000 * M1 * M2 / distance(pos1, pos2) ** 2 * math.cos(angle_F), 
          scipy.constants.G * M1 * M2 / distance(pos1, pos2) ** 2 * math.sin(angle_F))

    F2 = (F1[0] * -1, F1[1] * -1)
    v1 = (v1[0] + F1[0] / M1 * koef, v1[1] + F1[1] / M1 * koef)
    print(angle_F, pos1, pos2)
    v2 = (v2[0] + F2[0] / M2 * koef, v2[1] + F2[1] / M2 * koef)
    pos1 = (pos1[0] + v1[0], pos1[1] + v1[1])
    pos2 = (pos2[0] + v2[0], pos2[1] + v2[1])
    
    #���������
    screen.fill(BLACK)
    
    for I in range(0, int(grid / 2) + 1):   # �����
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] + nak * HEIGHT / grid * I], [WIDTH, nol[1] + nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [0, nol[1] - nak * HEIGHT / grid * I], [WIDTH, nol[1] - nak * HEIGHT / grid * I])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I, nol[1] + nol[1] * nak], [WIDTH / grid * I, nol[1] - nol[1] * nak])
        pygame.draw.line(screen, GRID_CLR, [WIDTH / grid * I + nol[0], nol[1] + nol[1] * nak], [WIDTH / grid * I + nol[0], nol[1] - nol[1] * nak])

    pygame.draw.circle(screen, CLR1, [k_len * pos1[0] + nol[0], k_len * nak * pos1[1] + nol[1]], 10)
    pygame.draw.circle(screen, CLR2, [k_len * pos2[0] + nol[0], k_len * nak * pos2[1] + nol[1]], 10)
        
    #���������
    pygame.display.flip()
    clock.tick(FPS)

