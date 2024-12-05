# Pygame шаблон - скелет для нового проекта Pygame
pip install pygame
import pygame
import random

WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секундуe

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()