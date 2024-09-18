import pygame

class Vector:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def increase(self, a):
        self.x += a.x
        self.y += a.y

    def scalar(self, dt : int):
        return Vector(self.x * dt, self.y * dt)

class Object:
    def __init__(self, mass : int, v : Vector, x : int, y : int, image : str) -> None:
        self.mass : int = mass
        self.v : Vector = v
        self.x : int = x
        self.y : int = y
        self.image : int = image
    
    def get_mass(self) -> int:
        return self.mass
    
    def get_v(self) -> int:
        return self.v
    
    def get_xy(self) -> int:
        return (self.x, self.y)
    
    def move(self):
        self.x += self.v.x * dt
        self.y += self.v.y * dt

    def change_v(self, a : Vector) -> None:
        self.v.increase(a.scalar(dt))

class Static(Object):
    def move(self):
        pass


class Scene:






def main():
    pygame.init()
    keepGameRunning = True
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                keepGameRunning = False

if __name__ == "__main__":
    main()