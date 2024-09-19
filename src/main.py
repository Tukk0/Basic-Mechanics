from math import sqrt

import pygame

from config import dt, G, RED, LENGTH, HIGHT, X, MIDX, MIDY, MZ, V1, WHITE, GREEN


VERBOSE = 2


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def increase(self, a):
        self.x += a.x
        self.y += a.y

    def scalar(self, dt: int):
        return Vector(self.x * dt, self.y * dt)

    def len(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def normilize(self) -> None:
        k = self.len()
        if k != 0:
            self.x /= k
            self.y /= k


class Object:
    def __init__(self, mass: int, v: Vector, x: int, y: int, image: str = "sprites/empty.png",
                 size: int = 100, name : str = "") -> None:
        self.mass: int = mass
        self.v: Vector = v
        self.x: int = x
        self.y: int = y
        self.image: int = pygame.image.load(image).convert_alpha()
        self.size : int = size
        self.name : str = name
        self.image = pygame.transform.scale(self.image, (size, size))
        self.last_positions = set()

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
        self.last_positions.add((self.x, self.y))
        self.x += self.v.x * dt
        self.y += self.v.y * dt


    def change_v(self, a: Vector) -> None:
        self.v.increase(a.scalar(dt))

    def get_skin(self):
        return self.image
    
    def get_name(self) -> str:
        return self.name
    
    def get_size(self) -> int:
        return self.size
    
    def get_last_positions(self) -> set[list[int,int]]:
        return self.last_positions


class Static(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = Vector(0, 0)


    def move(self):
        pass

    def change_v(self, a: Vector) -> None:
        pass


def Func(object1, object2) -> Vector:
    view = Vector(object2.get_x() - object1.get_x(), object2.get_y() - object1.get_y())
    k = G * (object1.get_mass()) * (object2.get_mass()) / ((view.len()) ** 2)
    view.normilize()
    return view.scalar(k)


class Scene:
    def __init__(self):
        # earth
        self.obj: list[Object] = [
            Object(100, Vector(V1, 0), 0, X * 110, "sprites/sputnic.png", size=100, name = "Sputnic"),
            Static(MZ, Vector(1, 1), 0, 0, "sprites/earth.png", size=100, name = "Earth"), ]
        # self.obj: list[Object] = [
        # Object(10**12, Vector(1, 0), 0, 0, "sprites/earth.png", size=100),
        # Object(10**12,Vector(0,0), 0,100, "sprites/earth.png", size=100),
        # Object(10**12,Vector(0,0), 100,-100, "sprites/earth.png", size=100)]
        self.len = len(self.obj)

    def update(self, surface):
        a = [Vector(0, 0) for i in self.obj]

        for i in range(self.len):
            for j in range(i + 1, self.len):
                obj1 = self.obj[i]
                obj2 = self.obj[j]
                F = Func(obj1, obj2)
                a[i].increase(F.scalar(1 / obj1.get_mass()))
                a[j].increase(F.scalar(-1 / obj2.get_mass()))

        for i in range(self.len):
            self.obj[i].change_v(a[i])
            self.obj[i].move()

        self.Draw(surface)

    def Draw(self, surface):
        surface.fill((0, 0, 0))

        def draw_text(surface, text, position, align = "midleft"):
            text_skin = pygame.font.SysFont('Comic Sans MS', 24).render(text, False, RED)
            if align == "midleft":
                text_rect = text_skin.get_rect(midleft=position)
            elif align == "center":
                text_rect = text_skin.get_rect(center=position)
            surface.blit(text_skin, text_rect)

        def draw_object(surface: pygame, object, pos_x, pos_y, draw_scale=1):
            object_skin = object.get_skin()
            object_rect = object_skin.get_rect(center=(pos_x, pos_y), )
            surface.blit(object_skin, object_rect)

        image = pygame.image.load("sprites/empty.png").convert_alpha()

        for i, obj in enumerate(self.obj):

            start = (obj.get_x() / X + MIDX, obj.get_y() / X + MIDY)
            v = Vector(obj.get_v().x,obj.get_v().y)
            v.normilize()
            v = v.scalar(100)
            v.increase(Vector(start[0], start[1]))

            draw_object(surface, obj, start[0], start[1])
            draw_text(surface, f"Speed of {obj.get_name()} : {round(obj.v.len(), 0)}км/s",
                      (LENGTH - 500, (i + 1) * 50))
            draw_text(surface, f"{obj.get_name()}", (start[0], start[1] - obj.get_size() + 20), align = "center")

            if VERBOSE > 0:
                pygame.draw.line(surface, GREEN, start, [v.x,v.y])
                if VERBOSE > 1:
                    for pos in obj.get_last_positions():
                        pygame.draw.circle(surface, WHITE,  (pos[0] / X + MIDX, pos[1] / X + MIDY), 1)

        pygame.display.flip()
        pygame.display.update()


def main():
    pygame.init()
    surface: pygame.display = pygame.display.set_mode((LENGTH, HIGHT))
    scene = Scene()
    keepGameRunning = True
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGameRunning = False
        scene.update(surface)


if __name__ == "__main__":
    main()
