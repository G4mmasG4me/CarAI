import pygame
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Car:
    def __init__(self):
        self.width = 100
        self.height = 50
        self.x = 50
        self.y = 50
        self.speed_limit = 100
        self.image = pygame.image.load("bugatti.png")

    def move(self, xChange, yChange):
        self.x += xChange
        self.y += yChange
        gameDisplay.blit(self.image, (self.x, self.y))

class MainRun(object):
    def __init__(self, displayWidth, displayHeight, title):
        self.width = displayWidth
        self.height = displayHeight
        self.title = title
        self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.main()

    def main(self):
        clock = pygame.time.Clock()
        running = True
        car = Car()
        xChange = 0
        yChange = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            #up
            if keys[pygame.K_UP]:
                print("Up")
                yChange += 1
            #down
            elif keys[pygame.K_DOWN]:
                print("Down")
                yChange -= 1
            #left
            elif keys[pygame.K_LEFT]:
                xChange += 1
            #right
            elif keys[pygame.K_RIGHT]:
                xChange -= 1

            car.move(xChange, yChange)
            pygame.display.update()
            clock.tick()

if __name__ == "__main__":
    MainRun(800, 800, "Car Game")
