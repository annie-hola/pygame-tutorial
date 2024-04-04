# 1. Import 
import pygame

# 2. Initialize
pygame.init()

# 3. Create Window
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello My First Game')

# 4. Initialize Clock for FPS
# represents the desired frames per second (FPS) 
fps = 30
clock = pygame.time.Clock()

# Main loop
start = True
while start: 
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    
    #Apply logic
    window.fill((255, 0, 255))
    
    # Update display
    pygame.display.update()
    
    # Set FPS
    clock.tick(fps)
