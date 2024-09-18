import pygame

from math import sqrt

from src.config import dt, G, RED, LENGTH, HIGHT, X, MIDX, MIDY

class Vector:
    def __init__(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def increase(self, a):
        self.x += a.x
        self.y += a.y

    def scalar(self, dt : int):
        return Vector(self.x * dt, self.y * dt)
    
    def len(self) -> float:
        return sqrt(self.x**2 + self.y**2)
    
    def normilize(self) -> None:
        k = self.len()
        if k != 0:
            self.x /= k
            self.y /= k


class Object:
    def __init__(self, mass : int, v : Vector, x : int, y : int, image : str = "sprites/empty.png") -> None:
        self.mass : int = mass
        self.v : Vector = v
        self.x : int = x
        self.y : int = y
        self.image : int = pygame.image.load(image).convert_alpha()
    
    def get_mass(self) -> int:
        return self.mass
    
    def get_v(self) -> int:
        return self.v
    
    def get_xy(self) -> list[int, int]:
        return (self.x, self.y)
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def move(self):
        self.x += self.v.x * dt
        self.y += self.v.y * dt

    def change_v(self, a : Vector) -> None:
        self.v.increase(a.scalar(dt))

    def get_skin(self):
        return self.image


class Static(Object):
    def move(self):
        pass

def F(object1, object2) -> Vector:
    view = Vector(object2.get_x() - object1.get_x(), object2.get_y() - object1.get_y())
    k = G*(object1.get_mass()) * (object2.get_mass) / ((view.len())**2)
    view.normilize()
    return view.scalar(k)
    



class Scene:
    def _init_(self):
        self.obj : list[Object]= [Object(1,Vector(1,1), 0,0), Static(1,Vector(1,1), 0,100)]
        self.len = len(self.obj)

    def update(self, surface):
        a = [Vector(0,0) for i in self.obj]

        for i in range(self.len):
            for j in range(i+1,self.len):
                obj1 = self.obj[i]
                obj2 = self.obj[j]
                F = F(obj1, obj2)
                a[i].increase(F.scalar(1/obj1.get_mass()))
                a[j].increase(F.scalar(-1/obj2.get_mass()))
        
        for i in range(self.len):
            self.obj[i].change_v(a[i])
            self.obj[i].move()

        self.Draw(surface)

    def Draw(self, surface):

        def draw_text(self, surface, text, position):
            text_skin = self.my_font.render(text, False, RED)
            text_rect = text_skin.get_rect(
                center=position,
                width=self.scale)
            surface.blit(text_skin, text_rect)

        def draw_object(self, surface: pygame, object, pos_x, pos_y, draw_scale=1):
            object_skin = self.get_image(object.get_skin())
            object_skin = pygame.transform.scale(object_skin,
                                                (draw_scale * self.scale, draw_scale * self.scale))
            object_rect = object_skin.get_rect(
                center=(pos_x + MIDX, pos_y + MIDY),
                width=self.scale)
            surface.blit(object_skin, object_rect)

        image = pygame.image.load("sprites/empty.png").convert_alpha()

        for obj in self.obj:
            self.draw_object(surface, obj, obj.get_x() / X, obj.get_y() / X)

        pygame.display.update()









def main():
    pygame.init()
    surface: pygame.display = pygame.display.set_mode((LENGTH, HIGHT))
    keepGameRunning = True
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                keepGameRunning = False

if __name__ == "__main__":
    main()