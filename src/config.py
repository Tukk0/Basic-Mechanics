from math import sqrt

#FIrst 3 scenes
# Time difference
dt = 200

#V1 = 7770 #m/s
#V1 = sqrt(v.G*MZ / (RZ + 160 * 10 ** 3))
#V2 = 11200 #m/s

# Colors
RED = (255, 0, 0)
WHITE = (255,255,255)
GREEN = (0,255,0)

# Window parameters
LENGTH = 1500 # 1920
HIGHT = 800 # 1080

# drawing const
# X = (6378 * 10 ** 3) // 100  # <- earth
# X = 1

#X for first 3 scenes
#X = (RZ + 160 * 10 ** 3) // 100

#X for planets
X = 0.25 * 10 ** 9
MIDX = LENGTH / 2
MIDY = HIGHT / 2

#Buttons
BORDER_WIDTH = 7