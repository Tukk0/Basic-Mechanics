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

    # Add a vector to self
    def add(self, a) -> None:
        self.x += a.x
        self.y += a.y

    # Multiply a vector by a scalar
    def resize(self, n):
        return Vector(self.x * n, self.y * n)

    def square(self) -> float:
        return (self.x ** 2 + self.y ** 2)

    def length(self) -> float:
        return sqrt(self.square())

    def normalize(self) -> None:
        k = self.length()
        if k != 0:
            self.x /= k
            self.y /= k


class Object:
    def __init__(self, mass: int, velocity: Vector, x: int, y: int, image: str = "empty.png",
                 img_size: int = 100, name: str = "") -> None:
        self.mass: int = mass
        self.velocity: Vector = velocity
        self.x: int = x
        self.y: int = y
        self.name: str = name
        self.image = pygame.image.load(image).convert_alpha()
        self.img_size: int = img_size
        self.image = pygame.transform.scale(self.image, (img_size, img_size))
        self.k_energy = mass * velocity.square() / 2
        self.p_energy = 0
        self.last_positions = []

    def get_mass(self) -> int:
        return self.mass

    def get_velocity(self) -> Vector:
        return self.velocity

    def get_x(self) -> int:
        return self.x

    def get_y(self) -> int:
        return self.y

    def get_xy(self) -> list[int, int]:
        return self.x, self.y

    def move(self):
        self.last_positions.append((self.x, self.y))
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    def change_velocity(self, a: Vector) -> None:
        # The formula for updated velocity is v = v0 + a*dt
        self.velocity.add(a.resize(dt))
        # Update kinetic energy
        self.k_energy = self.mass * self.velocity.square() / 2

    def get_skin(self):
        return self.image
    
    def get_name(self) -> str:
        return self.name
    
    def get_size(self) -> int:
        return self.img_size

    # Return a list of all positions the object has been through
    def get_last_positions(self) -> list[list[int, int]]:
        return self.last_positions

    def get_energy(self) -> float:
        return self.k_energy + self.p_energy

# An object that does not move
class Static(Object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.v = Vector(0, 0)

    def move(self):
        pass

    def change_v(self, a: Vector) -> None:
        pass


def Gravitational_force(object1: Object, object2: Object) -> Vector:
    # Get the directional vector of the gravitational force between objects
    direction = Vector(object2.get_x() - object1.get_x(), object2.get_y() - object1.get_y())
    # Find the magnitude of the force
    gravitational_force = vals.G * (object1.get_mass()) * (object2.get_mass()) / ((direction.length()) ** 2)
    # Normalize the vector
    direction.normalize()
    # Return the vector with the proper magnitude
    return direction.resize(gravitational_force)


class Scene:
    def __init__(self):
        # Three objects
        """
        self.obj: list[Object] = [
            Object(v.EARTH_M, Vector(30 * 10 ** 6, 0), 0, D_ZM, "earth.png", size=100, name="1"),
            Object(SOLNCE, Vector(0, 0), 0, 0, "earth.png", size=100, name="2"),
            Object(7.36 * 10 ** 22, Vector(-1e6, 0), 0, D_ZM - 384.4 * 10 ** 6, "earth.png", size=100, name="3")]
        """
        # First cosmic speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V1, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name="Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''
        # Second cosmic speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V2, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name="Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''
        # Smth between first and second speed
        '''self.obj: list[Object] = [
            Object(83.6, Vector(V2 * 0.9, 0), 0, RZ + 160 * 10 ** 3, "sputnic.png", size=100, name = "Sputnic"),
            Static(v.EARTH_M, Vector(0, 0), 0, 0, "earth.png", size=100, name="Earth"), ]'''
        # Space objects
        self.obj: list[Object] = [
            Object(vals.SUN_M, Vector(0, 0), 0, 0, "sun.png", img_size=100, name = vals.SUN_NAME),
            #Object(vals.MERCURY_M, Vector(0, vals.MERCURY_V), vals.MERCURY_D, 0, "sputnic.png", img_size=100, name = vals.MERCURY_NAME),
            #Object(vals.VENUS_M, Vector(0, vals.VENUS_V), vals.VENUS_D, 0, "sputnic.png", img_size=100, name = vals.VENUS_NAME),
            Object(vals.EARTH_M, Vector(0, vals.EARTH_V), vals.EARTH_D, 0, "earth.png", img_size=100, name = vals.EARTH_NAME),
            Object(vals.MOON_M, Vector(0, vals.MOON_V), vals.MOON_D, 0, "moon.png", img_size=100, name = vals.MOON_NAME),
            #Object(vals.MARS_M, Vector(0, vals.MARS_V), vals.MARS_D, 0, "sputnic.png", img_size=100, name = vals.MARS_NAME),
            #Object(vals.JUPITER_M, Vector(0, vals.JUPITER_V), vals.JUPITER_D, 0, "sputnic.png", img_size=100, name = vals.JUPITER_NAME),
            #Object(vals.SATURN_M, Vector(0, vals.SATURN_V), vals.SATURN_D, 0, "sputnic.png", img_size=100, name = vals.SATURN_NAME),
            #Object(vals.URANUS_M, Vector(0, vals.URANUS_V), vals.URANUS_D, 0, "sputnic.png", img_size=100, name = vals.URANUS_NAME),
            #Object(vals.NEPTUNE_M, Vector(0, vals.NEPTUNE_V), vals.NEPTUNE_D, 0, "sputnic.png", img_size=100, name = vals.NEPTUNE_NAME),
            ]
        # The total energy of the system
        self.total_energy = sum(x.get_energy() for x in self.obj)
        self.max_energy = None
        self.min_energy = None
        # The number of objects in the system
        self.system_size = len(self.obj)
        # Current time
        self.time = time.time()

    def update(self, surface):
        # Create an acceleration vector for every object in the system
        accelerations_list = [Vector(0, 0) for i in self.obj]
        # Calculate all the accelerations of the objects in the system
        for i in range(self.system_size):
            for j in range(i + 1, self.system_size):
                obj1 = self.obj[i]
                obj2 = self.obj[j]
                F = Gravitational_force(obj1, obj2)
                # The formula for acceleration is a = F / m
                # We add vectors, since acceleration is a sum of vectors
                accelerations_list[i].add(F.resize(1/obj1.get_mass()))
                # Two interacting objects have opposingly directed forces
                accelerations_list[j].add(F.resize(-1/obj2.get_mass()))
        # Update the positions of all the objects in the system
        for i in range(self.system_size):
            # Update the velocity
            self.obj[i].change_velocity(accelerations_list[i])
            # Update the position
            self.obj[i].move()

        # Update objects` potential energies
        for obj in self.obj:
            obj.p_energy = 0
        for i in range(self.system_size):
            for j in range(i + 1, self.system_size):
                obj1 = self.obj[i]
                obj2 = self.obj[j]
                direction = Vector(obj1.get_x() - obj2.get_x(), obj1.get_y() - obj2.get_y())
                potential_energy = -vals.G * (obj1.get_mass()) * (obj2.get_mass()) / direction.length()
                obj1.p_energy += potential_energy
                obj2.p_energy += potential_energy
        # Update objects` kinetic energies
        for obj in self.obj:
            obj.k_energy = obj.get_mass() * obj.get_velocity().square() / 2
        # Update total energy
        self.total_energy = sum(x.get_energy() for x in self.obj)

        if time.time() - self.time > 0.1:
            self.time = time.time()
            self.draw(surface)

    def draw(self, surface):
        surface.fill((0, 0, 0))

        # Add textual information onto the screen
        def draw_text(surface, text, position, align = "midleft"):
            text_skin = pygame.font.SysFont('Comic Sans MS', TEXT_SIZE).render(text, False, TEXT_COLOR)
            text_rect = text_skin.get_rect(center=position)
            if align == "midleft":
                text_rect = text_skin.get_rect(midleft=position)
            surface.blit(text_skin, text_rect)

        # Add graphical information onto the screen
        def draw_object(surface: pygame, object, pos_x, pos_y, draw_scale=1):
            object_skin = object.get_skin()
            object_rect = object_skin.get_rect(center=(pos_x, pos_y), )
            surface.blit(object_skin, object_rect)

        image = pygame.image.load("empty.png").convert_alpha()

        for i, obj in enumerate(self.obj):
            start = (obj.get_x() / X + MIDX, obj.get_y() / X + MIDY)
            v = Vector(obj.get_velocity().x, obj.get_velocity().y)
            v.normalize()
            v = v.resize(100)
            v.add(Vector(start[0], start[1]))

            if VERBOSE > 0:
                draw_object(surface, obj, start[0], start[1])
                draw_text(surface, f"Speed of {obj.get_name()} : {round(obj.velocity.length(), 0)} м/s",
                      (LENGTH - 370, (i + 1) * 50))
                #draw_text(surface, f"Energy : {self.total_energy} J", (50, (LENGTH - 370, 4 * 50)))
                draw_text(surface, f"{obj.get_name()}", (start[0], start[1] - obj.get_size() + 20), align = "center")
                draw_text(surface, f"Position of the {obj.get_name()} is x : {round(obj.get_x(), 0)} m, y :"
                                   f"{round(obj.get_y(), 0)} m", (50, (i + 1) * 50))
                if i == 0:
                    draw_text(surface, f"Energy of system is : {self.total_energy} J",
                              (50, (1 + self.system_size) * 50))


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
        # print(f"{time * dt} c")
        scene.update(surface)

__name__ = str(input())
if __name__ == "main":
    main()
