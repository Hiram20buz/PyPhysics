import math
import pygame

black = (0, 0, 0)
white = (255, 255, 255)

class Pendulum:
    def __init__(self, pivot_x=0, pivot_y=0, m=1, l=200, a=math.pi/2, g=1, color='red'):
        self.pivot = (pivot_x, pivot_y)
        self.m = m
        self.l = l
        self.a = a
        self.g = g
        self.clr = color

        self.x = 0
        self.y = 0

        self.av = 0
        self.trajectory = []

    def step(self):
        acc = (- self.g / self.l) * math.sin(self.a)
        self.av += acc
        self.av *= 0.99

        self.a += self.av
        self.x = self.pivot[0] + self.l * math.sin(self.a)
        self.y = self.pivot[1] + self.l * math.cos(self.a)

    def draw(self, surface):
        pygame.draw.line(surface, white, self.pivot, (self.x, self.y))
        pygame.draw.circle(surface, self.clr, (self.x, self.y), 15)


def init_surface(size, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    surface = pygame.display.set_mode()
    clock = pygame.time.Clock()
    return surface, clock

def run():
    width, height = 800, 800
    fps = 60
    surface, clock = init_surface((width, height), 'Simple Pendulum')
    lengths = [200 + 30 * i for i in range(7)]
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'white', 'orange']
    pend_list = [Pendulum(pivot_x=width//2, pivot_y=height//2, l=l, color=c) for l, c in zip(lengths, colors)]
    #pendulum = Pendulum(width//2, height//2)
    stop = False

    while not stop:
        clock.tick(fps)
        surface.fill(black)

        for event in pygame.event.get():
            stop = event.type == pygame.QUIT

        for i in range(len(pend_list)-1, -1, -1):
            pend_list[i].step()
            pend_list[i].draw(surface)
        '''
        pendulum.step()
        pendulum.draw(surface)
        '''

        pygame.display.flip()
    pygame.quit()

run()
