import pygame

pygame.init()
WIDTH = 400
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
GRID = [[1, 0, '@', '@', 0, 0, 0, 0],
        ['@', 0, 0, 0, 0, '@', '@', 0],
        ['@', '@', '@', '@', 0, 0, '@', 0],
        ['@', '@', '@', 'T', '@', 0, '@', 0],
        ['@', '@', '@', 0, 0, 0, '@', 0],
        ['@', '@', '@', 0, '@', '@', '@', 0],
        ['@', '@', '@', 0, '@', '@', '@', 0]]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    running = True
    while running:
        draw_grid(GRID)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

def draw_grid(grid):
    grid_width = len(grid[0])
    grid_height = len(grid)
    cell_width = HEIGHT // grid_width
    cell_height = WIDTH // grid_height

    for i in range(grid_height):
        for j in range(grid_width):
            if GRID[i][j] == 1:
                color = RED
            elif GRID[i][j] == 0:
                color = WHITE
            elif GRID[i][j] == '@':
                color = BLACK
            elif GRID[i][j] == 'T':
                color = GREEN
            y = i * cell_height
            x = j * cell_width
            rect = pygame.Rect(x, y, cell_width-1, cell_height-1)
            pygame.draw.rect(SCREEN, color, rect, 0)
main()