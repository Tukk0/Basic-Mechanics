from math import sqrt

dt = 3
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

LENGTH = 1920
HIGHT = 1080

# drawing const
# X = (6378 * 10 ** 3) // 100  # <- earth
# X = 1

X = (RZ + 160 * 10 ** 3) // 100
MIDX = LENGTH / 2
MIDY = HIGHT / 2
