# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# for y in range(100, 301, 100):
#     for x in range(100, 1001, 100):
#         point = sd.get_point(x, y)
#         bubble(point=point, step=5)

for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)

sd.pause()


