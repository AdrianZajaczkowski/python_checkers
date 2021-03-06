import pygame 


WIDTH, HEIGHT = 488, 488

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)
WHITE =(255,255,255)
BLACK = (0,0,0)
BLUE=(0,0,255)
GREY = (128,128,128)

COLORS = {
    'RED'  : (255, 0, 0),
    'WHITE': (255,255,255),
    'BLACK': (0,0,0),
    'BLUE' : (0,0,255),
    'GREY' : (58,58,58), 
    'L_GREEN' : (127,255,127)
}
x = int(SQUARE_SIZE / 4 )
y = int(SQUARE_SIZE / 4 )

CROWN = pygame.transform.scale(pygame.image.load('python_checkers/include/scripts/assets/crown.png'),(x,y))

