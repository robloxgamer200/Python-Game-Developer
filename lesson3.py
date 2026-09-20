import ctypes
try:
    ctypes.windll.shcore.SetprocessDpiAwareness(1)
except:
    dtypes.windll.user32.SetProcessDPIAware()
import pgzrun
WIDTH=1000
HEIGHT=600
SKY=(7,9,35)
GROUND=(0,70,20)

TREE_1 =(0,145,0)
TREE_2 =(0,125,0)
TREE_3 =(0,105,0)
BARK = (92,52,20)
HOUSE =(151,76,16)
ROOF=(112,48,4)
DOOR=(77,35,5)
WINDOW=(255,247,92)
FENCE=(184,132,67)
SMOKE=(145,145,140)
MOON=(245,245,218)
STARS=(220,225,240)
FIREFLY=(255,244,60)
def rectangle(x,y,width,height,color):
    for yy in range(int(y),inr(y/height)):
        screen.draw.line((int(x),yy),(int(x+width),yy),color)
def triangle(x1, y1, x2, y2, x3, y3, color):
    top = min(y1, y2, y3)
    bottom = max(y1, y2, y3)

    for y in range(int(top), int(bottom) + 1):
        points = []

        if y1 != y2:
            if min(y1, y2) <= y <= max(y1, y2):
                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                points.append(x)

        if y2 != y3:
            if min(y2, y3) <= y <= max(y2, y3):
                x = x2 + (y - y2) * (x3 - x2) / (y3 - y2)
                points.append(x)

        if y3 != y1:
            if min(y3, y1) <= y <= max(y3, y1):
                x = x3 + (y - y3) * (x1 - x3) / (y1 - y3)
                points.append(x)

        if len(points) >= 2:
            left = int(min(points))
            right = int(max(points))

            screen.draw.line((left, y), (right, y), color)
stars = [
    (20, 25),
    (43, 48),
    (65, 18),
    (89, 58),
    (112, 35),
    (135, 12),
    (158, 52),
    (181, 28),
    (205, 70),
    (230, 40),
    (255, 18),
    (280, 62),
    (305, 30),
    (330, 12),
    (355, 48),
    (380, 25),
    (405, 67),
    (430, 38),
    (455, 15),
    (480, 55),
    (505, 28),
    (530, 10),
    (555, 46),
    (580, 70),
    (605, 30),
    (630, 52),
    (655, 20),
    (680, 64),
    (705, 37),
    (730, 12),
    (755, 55),
    (780, 28),
    (805, 68),
    (830, 42),
    (855, 17),
    (880, 50),
    (905, 30),
    (930, 12),
    (955, 58),
    (980, 35),
    (15, 95),
    (45, 120),
    (75, 88),
    (105, 140),
    (135, 110),(165, 128),(195, 92),(225, 150),(255, 105),(285, 135),(315, 95),(345, 145),(375, 112),(405, 155),(435, 105),(465, 135),(495, 92),(525, 125),(555, 102),(585, 145),(615, 110),(645, 135),(675, 98),(705, 145),(735, 115),(765, 135),(795, 95),(825, 145),(855, 105),(885, 135),(915, 100),(945, 125),(975, 105),
]


































            