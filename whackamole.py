import pygame
import random


def main():
    molex, moley = 0, 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if int(molex/32) == int(event.pos[0]/32) and int(moley/32) == int(event.pos[1]/32):
                        molex = random.randrange(0, 640, 32)
                        moley = random.randrange(0, 512, 32)
            screen.fill("light green")
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(molex,moley)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
