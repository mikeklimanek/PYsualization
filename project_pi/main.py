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

scaling_factor = 3


font = pygame.font.Font(None, 36)

def get_offset_angle(angle, offset):
    return angle + offset

def get_offset_coordinates(x, y, offset, angle):
    new_x = x + offset * scaling_factor * math.cos(angle)
    new_y = y + offset * scaling_factor * math.sin(angle)
    return new_x, new_y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    rotation_angle_radians = math.radians(90)
    pygame.draw.circle(screen, (255, 255, 255), (width // 2, height // 2), 605, 5)

    current_digit = digits[index]
    index += 1
    counts[current_digit] += 1





    pygame.quit()