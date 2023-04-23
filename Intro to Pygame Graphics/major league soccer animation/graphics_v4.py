# Imports
import pygame
import math
import random
from draw_graphics import *

# Initialize game engine
pygame.init()

# Draws clouds
def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))

# Config
lights_on = True

stars = []
for n in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 200)
    r = random.randrange(1, 2)
    stars.append([x, y, r, r])

clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0, 150)
    clouds.append([x, y])
    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)

    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])

    '''fence'''
    draw_fence(sky_color)
    
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))   

    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)

    #goal
    pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #left lights
    draw_left_lights(light_color)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #right lights
    draw_right_lights(light_color)

    #net
    draw_net()

    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])
  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    #people
    
    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()