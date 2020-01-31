import pygame
import time

running = True

car = pygame.image.load('bugatti.png')
car = pygame.transform.scale(car, (50, 100))
carClean = car.copy()

def carupdate(angle, car):
    center = car.get_rect().center
    car = pygame.transform.rotate(car, angle)
    carRect = car.get_rect(center = center).move(400, 400)
    display.blit(car, carRect)

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Car')
angle = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    display.fill((255,255,255))
    angle += 1
    angle = angle % 360
    print(angle)
    carupdate(angle, car)
    pygame.display.update()
    clock.tick(60)
