# Pygame ������ - ������ ��� ������ ������� Pygame
pip install pygame
import pygame
import random

WIDTH = 360  # ������ �������� ����
HEIGHT = 480 # ������ �������� ����
FPS = 30 # ������� ������ � �������e

# ������� ���� � ����
pygame.init()
pygame.mixer.init()  # ��� �����
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()