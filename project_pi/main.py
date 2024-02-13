import pygame
import math
import time
import random

with open("pi-1million.txt", "r") as file:
    pi = file.read()

digits = [int(digit) for digit in pi]

pygame.init()
width, height = 1200, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pi Visualization")

# colors
# red = (255, 0, 0), white = (255, 255, 255)
colors = [(255, 255, 255),(255, 0, 0)]
color_index = 0

running = True
clock = pygame.time.Clock()

counts = [0] * 10
index = 0
positions = {}