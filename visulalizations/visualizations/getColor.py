import colorsys
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

color_palette = [RED, GREEN, BLUE, (255, 255, 0), (255, 165, 0), (128, 0, 128)]

def get_gradient_color(value, min_value, max_value):
    ratio = (value - min_value) / (max_value - min_value)
    red = int(255 * ratio)
    blue = int(255 * (1 - ratio))
    return (red, 0, blue)

def get_rainbow_color(i, total):
    hue = i / total
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_palette_color(i):
    return color_palette[i % len(color_palette)]