from math import sqrt

import values as vals

# V1 = 7770 #m/s
# V1 = sqrt(v.G*MZ / (RZ + 160 * 10 ** 3))
# V2 = 11200 #m/s
class values:
    # Colors
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Window parameters
    LENGTH = 1500  # 1920
    HIGHT = 800  # 1080

    # Drawing configuration
    TEXT_SIZE = 20
    TEXT_COLOR = WHITE

    # X = (6378 * 10 ** 3) // 100  # <- earth
    # X = 1

    # X for first 3 scenes
    # X = (RZ + 160 * 10 ** 3) // 100

    # X for planets
    X = 0.5 * 10 ** 9
    MIDX = LENGTH / 2
    MIDY = HIGHT / 2

    # Buttons
    BORDER_WIDTH = 7

    # for nondimensionalization
    FOR_DISTANCE = 1 / (vals.EARTH_R * 90)
    V1 = sqrt(vals.G * vals.EARTH_M / vals.EARTH_R)
    FOR_TIME = V1 / vals.EARTH_R

    # Time difference
    dt = 5
