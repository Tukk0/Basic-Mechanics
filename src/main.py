from math import sqrt
import time

import pygame

import values as vals
from config import *


VERBOSE = 2


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def increase(self, a):
        self.x += a.x
        self.y += a.y

    # Scalar multiplication of vectors
    def scalar(self, dt):
        return Vector(self.x * dt, self.y * dt)

    def len(self) -> float:
        return sqrt(self.second())

    def second(self) -> float:
        return self.x ** 2 + self.y ** 2

    def normilize(self) -> None:
        k = self.len()
        if k != 0:
            self.x /= k
            self.y /= k


class Object:
    def __init__(self, mass: int, v: Vector, x: int, y: int, image: str = "empty.png",
                 size: int = 100, name: str = "") -> None:
        self.mass: int = mass
        self.v: Vector = v
        self.x: int = x
        self.y: int = y
        self.image = pygame.image.load(image).convert_alpha()
        self.size: int = size
        self.name: str = name
        self.image = pygame.transform.scale(self.image, (size, size))
        self.k_energy = mass * v.second() / 2
        self.p_energy = 0
        self.last_positions = []

    def get_mass(self) -> int:
        return self.mass

    def get_v(self) -> Vector:
        return self.v

    def get_xy(self) -> list[int, int]:
        return self.x, self.y

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def move(self):
        self.last_positions.append((self.x, self.y))
        self.x += self.v.x * dt
        self.y += self.v.y * dt


    def change_v(self, a: Vector) -> None:
        self.v.increase(a.scalar(dt))
        #update kinetic energy
        self.k_energy = self.mass * self.v.second() / 2

    def get_skin(self):
        return self.image
    
    def get_name(self) -> str:
        return self.name
    
    def get_size(self) -> int:
        return self.size
    
    def get_last_positions(self) -> list[list[int, int]]:
        return self.last_positions

    def get_energy(self) -> float:
        return self.k_energy + self.p_energy


class Static(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = Vector(0, 0)


    def move(self):
        pass

    def change_v(self, a: Vector) -> None:
        pass


def Func(object1: Object, object2: Object, ind1: int, ind2: int) -> Vector:
    view = Vector(object2.get_x() - object1.get_x(), object2.get_y() - object1.get_y())
    k = vals.G * (object1.get_mass()) * (object2.get_mass()) / ((view.len()) ** 2)
    view.normilize()
    return view.scalar(k)


class Scene:
    def __init__(self):
        # Three objects
        """
        self.obj: list[Object] = [
            Object(v.EARTH_M, Vector(30 * 10 ** 6, 0), 0, D_ZM, "earth.png", size=100, name="1"),
            Object(SOLNCE, Vector(0, 0), 0, 0, "earth.png", size=100, name="2"),
            Object(7.36 * 10 ** 22, Vector(-1e6, 0), 0, D_ZM - 384.4 * 10 ** 6, "earth.png", size=100, name="3")]
        """

        
        # First speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V1, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name="Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''
        
        # Second speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V2, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name="Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''
        
        #Smth between first and second speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V2 * 0.9, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name = "Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''

        # SUN and other planets
        self.obj: list[Object] = [
            Object(vals.SUN_M, Vector(0, 0), 0, 0, "earth.png", size=100, name = "SUN"),
            #Object(MERKURY, Vector(0, V_MERKURY), D_MERKURY, 0, "sputnic.png", size=100, name = "Merkury"),
            #Object(VENERA, Vector(0, V_VENERA), D_VENERA, 0, "sputnic.png", size=100, name = "VENERA"),
            Object(vals.EARTH_M, Vector(0, vals.EARTH_V), vals.EARTH_D, 0, "earth.png", size=100, name = "ZEMLYA"),
            #Object(7.36 * 10 ** 22, Vector(0,V_ZM), D_ZM + 384.4 * 10 ** 6, 0, "sputnic.png", size=100, name="3"),
            #Object(MARS, Vector(0, V_MARS), D_MARS, 0, "sputnic.png", size=100, name = "MARS"),
            #Object(UPITER, Vector(0, V_UPITER), D_UPITER, 0, "sputnic.png", size=100, name = "UPITER"),
            #Object(SATURN, Vector(0, V_SATURN), D_SATURN, 0, "sputnic.png", size=100, name = "SATURN"),
            #Object(Uran, Vector(0, V_URAN), D_URAN, 0, "sputnic.png", size=100, name = "URAN"),
            Object(vals.NEPTUNE_M, Vector(0, vals.NEPTUNE_V), vals.NEPTUNE_D, 0, "sputnic.png", size=100, name = "NEPTUN"),
            ]
        self.all_energy = sum(x.get_energy() for x in self.obj)
        self.max_energy = None
        self.min_energy = None
        self.len = len(self.obj)

        self.time = time.time()

    def update(self, surface):
        a = [Vector(0, 0) for i in self.obj]

        for i in range(self.len):
            for j in range(i + 1, self.len):
                obj1 = self.obj[i]
                obj2 = self.obj[j]
                F = Func(obj1, obj2, i, j)
                a[i].increase(F.scalar(1/obj1.get_mass()))
                a[j].increase(F.scalar(-1/obj2.get_mass()))

        for i in range(self.len):
            self.obj[i].change_v(a[i])
            self.obj[i].move()

        # update energy
        view12 = Vector(self.obj[0].get_x() - self.obj[1].get_x(), self.obj[0].get_y() - self.obj[1].get_y())
        view13 = Vector(self.obj[0].get_x() - self.obj[2].get_x(), self.obj[0].get_y() - self.obj[2].get_y())
        view23 = Vector(self.obj[1].get_x() - self.obj[2].get_x(), self.obj[1].get_y() - self.obj[2].get_y())
        self.obj[0].p_energy = - vals.G * (self.obj[0].get_mass()) * (self.obj[1].get_mass()) / (view12.len())
        self.obj[1].p_energy = - vals.G * (self.obj[1].get_mass()) * (self.obj[2].get_mass()) / (view23.len())
        self.obj[2].p_energy = - vals.G * (self.obj[0].get_mass()) * (self.obj[2].get_mass()) / (view13.len())
        #v2 = Vector(self.obj[1].v.x, self.obj[1].y)
        #v2.increase(self.obj[0].v.scalar(-1))
        #v3 = Vector(self.obj[2].v.x, self.obj[2].y)
        #v3.increase(self.obj[0].v.scalar(-1))
        self.obj[0].k_energy = self.obj[0].get_mass() * (self.obj[0].get_v().second()) / 2
        self.obj[1].k_energy = self.obj[1].get_mass() * (self.obj[1].get_v().second())/2
        self.obj[2].k_energy = self.obj[2].get_mass() * (self.obj[2].get_v().second())/2
        self.all_energy = sum(x.get_energy() for x in self.obj)
        #if self.min_energy != None:
        #    self.min_energy = min(self.all_energy, self.min_energy)
        #    self.max_energy = max(self.all_energy, self.max_energy)
        #else:
        #    self.min_energy = self.all_energy
        #    self.max_energy = self.all_energy
        print(self.all_energy) #, self.min_energy, self.max_energy, self.max_energy - self.min_energy)


        if time.time() - self.time > 0.1:
            self.time = time.time() 
            self.Draw(surface)

    def Draw(self, surface):
        surface.fill((0, 0, 0))

        def draw_text(surface, text, position, align = "midleft"):
            text_skin = pygame.font.SysFont('Comic Sans MS', 24).render(text, False, RED)
            text_rect = text_skin.get_rect(center=position)
            if align == "midleft":
                text_rect = text_skin.get_rect(midleft=position)
            surface.blit(text_skin, text_rect)

        def draw_object(surface: pygame, object, pos_x, pos_y, draw_scale=1):
            object_skin = object.get_skin()
            object_rect = object_skin.get_rect(center=(pos_x, pos_y), )
            surface.blit(object_skin, object_rect)

        image = pygame.image.load("empty.png").convert_alpha()

        for i, obj in enumerate(self.obj):

            start = (obj.get_x() / X + MIDX, obj.get_y() / X + MIDY)
            v = Vector(obj.get_v().x, obj.get_v().y)
            v.normilize()
            v = v.scalar(100)
            v.increase(Vector(start[0], start[1]))

            if VERBOSE > 0:
                draw_object(surface, obj, start[0], start[1])
                draw_text(surface, f"Speed of {obj.get_name()} : {round(obj.v.len(), 0)} м/s",
                      (LENGTH - 370, (i + 1) * 50))
                #draw_text(surface, f"Energy : {self.all_energy} J", (50, (LENGTH - 370, 4 * 50)))
                draw_text(surface, f"{obj.get_name()}", (start[0], start[1] - obj.get_size() + 20), align = "center")
                draw_text(surface, f"Position of the {obj.get_name()} is x : {round(obj.get_x(), 0)} m, y :"
                                   f"{round(obj.get_y(), 0)} m", (50, (i + 1) * 50))
                if i == 0:
                    draw_text(surface, f"Energy of system is : {self.all_energy} J", (50, (i + 4) * 50))


            if VERBOSE > 0:
                pygame.draw.line(surface, GREEN, start, [v.x, v.y])

            if VERBOSE > 1:
                for pos in obj.get_last_positions()[::20]:
                    pygame.draw.circle(surface, WHITE,  (pos[0] / X + MIDX, pos[1] / X + MIDY), 1)
            if VERBOSE > 0:
                pass


        pygame.display.flip()
        pygame.display.update()


def main():
    pygame.init()
    surface: pygame.display = pygame.display.set_mode((LENGTH, HIGHT))
    scene = Scene()
    keepGameRunning = True
    time = 0
    while keepGameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGameRunning = False
        time +=1
        print(f"{time * dt} c")
        scene.update(surface)

__name__ = str(input())
if __name__ == "main":
    main()
