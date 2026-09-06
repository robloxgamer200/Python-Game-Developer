import ctypes
try:
    ctypes.windll.schore.SetProcessDpiAwareness(1)
except:
    ctypes.windll.user32.SetProcessDPIAware()
import pgzrun
WIDTH=800
HEIGHT=550
SCALE_X=WIDTH/1000
def  X(value):
    return int(value*SCALE_X)
MAGENTA=(255,0,255)
CYAN=(255,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
def draw_rectangle(x, y, width, height, color):
     screen.draw.line((X(x), y), (X(x + width), y), color) 
     screen.draw.line((X(x), y), (X(x), y + height), color) 
     screen.draw.line((X(x + width), y), (X(x + width), y + height), color) 
     screen.draw.line((X(x), y + height), (X(x + width), y + height), color)

def draw(): 
    screen.fill(BLACK) 
    screen.draw.text( "NEON WIREFRAME CITY", center=(X(500), 50), fontsize=45, color=MAGENTA, ) 
    sun_x = 500 
    sun_y = 180 
    radius = 90 
    screen.draw.circle((X(sun_x), sun_y), int(radius * SCALE_X), MAGENTA) 
    for y in range(130, 240, 15): 
        screen.draw.line((X(420), y), (X(580), y), MAGENTA) 
    horizon_y = 420 
    screen.draw.line((X(0), horizon_y), (X(1000), horizon_y), CYAN) 
    vanish_x = 500 
    vanish_y = horizon_y 
    for x in range(0, 1001, 40): 
        screen.draw.line((X(x), HEIGHT), (X(vanish_x), vanish_y), CYAN)
    y = horizon_y + 20 
    gap = 20 
    while y < HEIGHT: 
        screen.draw.line((X(0), y), (X(1000), y), CYAN) 
        y += gap
        gap += 6

            