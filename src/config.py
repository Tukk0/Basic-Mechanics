from math import sqrt

#FIrst 3 scenes
dt = 2


#PLANETS
#dt = 10000
G = 6.674 * 10 ** (-11)
MZ = 5_972_200_000_000_000_000_000_000 # kg
RZ = 6378 * 10 ** 3 #m

#V1 = 7770 #m/s
V1 = sqrt(G*MZ / (RZ + 160 * 10 ** 3))
V2 = 11200 #m/s

# colors
RED = (255, 0, 0)
WHITE = (255,255,255)
GREEN = (0,255,0)

# Window params

LENGTH = 1300
HIGHT = 800

# drawing const
# X = (6378 * 10 ** 3) // 100  # <- earth
# X = 1

#X for first 3 scenes
X = (RZ + 160 * 10 ** 3) // 100

#X for planets
#X = 0.25 * 10 ** 9
MIDX = LENGTH / 2
MIDY = HIGHT / 2


#Masses of planets
MERKURY = 3.26*10**23
VENERA = 4.88 * 10**24
MARS = 6.43*10**23
UPITER = 1.90 * 10**27
SATURN = 5.69 * 10 ** 26
Uran = 8.69 * 10 ** 25
NEPTUN = 1.04 * 10 ** 26

SOLNCE = 1983 * 10 ** 27

#Distance between planets
D_MERKURY = 58 * 10 ** 9
D_VENERA = 108 * 10 ** 9
D_ZM = 149 * 10 ** 9
D_MARS = 228 * 10 ** 9
D_UPITER = 778 * 10 ** 9
D_SATURN = 1426 * 10 ** 9
D_URAN = 2871 * 10 ** 9
D_NEPTUN = 4496 * 10 ** 9
D_PLUTON = 5929 * 10 ** 9

#SPEEDS of planets

V_MERKURY = 47.8 * 10 ** 3 #m/s
V_VENERA = 35 * 10 ** 3
V_ZM = 29.8 * 10 ** 3
V_MARS = 24.1 * 10 ** 3
V_UPITER = 13.0 * 10 ** 3
V_SATURN = 9.6 * 10 ** 3
V_URAN = 6.8 * 10 ** 3
V_NEPTUN = 5.4 * 10 ** 3
V_PLUTON = 4.7 * 10 ** 3

#Buttons
BORDER_WIDTH = 7