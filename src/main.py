import pygame

class Vector:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y




def main():
    pygame.init()
    keepGameRunning = True
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                keepGameRunning = False

if __name__ == "__main__":
    main()