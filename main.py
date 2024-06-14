#importing and initializing pygame
import pygame
import random
pygame.init()

# Defining variables
COLOR1=(94,21,11)
COLOR2=(115,149,82)
COLOR3=(236,194,148)
TILE_SIZE=20
FPS=60

# Get grid size from user
GRID_WIDTH = int(input("Enter grid width: "))
GRID_HEIGHT = int(input("Enter grid height: "))
WIDTH, HEIGHT = GRID_WIDTH * TILE_SIZE, GRID_HEIGHT * TILE_SIZE

#setting the screen of simulation
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()

#function to return a positions set generated randomly
def gen(num):
    return set([(random.randrange(0,GRID_HEIGHT),random.randrange(0,GRID_WIDTH)) for _ in range(num)])

#function to draw the grid
def draw_grid(positions):
    for position in positions:
        col,row=position
        top_left=(col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen, COLOR2, (*top_left,TILE_SIZE,TILE_SIZE), width=0)

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, COLOR1, (0,row*TILE_SIZE), (WIDTH,row*TILE_SIZE))
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, COLOR1, (col*TILE_SIZE,0), (col*TILE_SIZE,HEIGHT))

#making a new positions set for the next generation of simulation
def adjust_grid(positions):
    all_neighbors=set()
    new_positions=set()
    for position in positions:
        neighbors=get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors=list(filter(lambda x:x in positions, neighbors))
        if len(neighbors) in [2,3]:
            new_positions.add(position)
    
    for position in all_neighbors:
        neighbors=get_neighbors(position)
        neighbors=list(filter(lambda x:x in positions, neighbors))
        if len(neighbors) == 3:
            new_positions.add(position)
    return new_positions

#function to get all the 8 neighbors of a position
def get_neighbors(position):
    x,y=position
    neighbors=[]
    for dx in [-1,0,1]:
        if x+dx<0 or x+dx>GRID_WIDTH:
            continue
        for dy in [-1,0,1]:
            if y+dy<0 or y+dy>GRID_WIDTH:
                continue
            if dx==0 and dy==0:
                continue
            neighbors.append((x+dx,y+dy))
    return neighbors

#function to load predefined patterns
def load_pattern(positions, pattern):
    if pattern == "glider":
        glider = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
        positions.update(glider)
    elif pattern == "blinker":
        blinker = {(2, 1), (2, 2), (2, 3)}
        positions.update(blinker)
    elif pattern == "beacon":
        beacon = {(1, 1), (2, 1), (1, 2), (4, 3), (3, 4), (4, 4)}
        positions.update(beacon)
    elif pattern == "pulsar":
        pulsar =  {(3, 1), (4, 1), (5, 1), (9, 1), (10, 1), (11, 1), (1, 3), (1, 4), (1, 5),
         (6, 3), (6, 4), (6, 5), (8, 3), (8, 4), (8, 5), (13, 3), (13, 4), (13, 5), (3, 6),
          (4, 6), (5, 6), (9, 6), (10, 6), (11, 6), (3, 8), (4, 8), (5, 8), (9, 8), (10, 8),
           (11, 8), (1, 9), (1, 10), (1, 11), (6, 9), (6, 10), (6, 11), (8, 9), (8, 10), (8, 11),
            (13, 9), (13, 10), (13, 11), (3, 13), (4, 13), (5, 13), (9, 13), (10, 13), (11, 13)}
        positions.update(pulsar)
    elif pattern == "block":
        block = {(1, 1), (1, 2), (2, 1), (2, 2)}
        positions.update(block)
    elif pattern == "beehive":
        beehive = {(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 3)}
        positions.update(beehive)
    elif pattern == "loaf":
        loaf = {(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 3)}
        positions.update(loaf)
    elif pattern == "rangoli":
        rangoli = {(5,5),(7,5),(6,6),(6,7)}
        positions.update(rangoli)
    elif pattern == "spaceship":
        spaceship = {(0, 1), (0, 2), (1, 0), (1, 3), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 4)}
        positions.update(spaceship)
    elif pattern == "gayab":
        gayab = {(6,6),(4,6),(3,6),(2,6),(8,6),(9,6),(10,6),(6,4),(6,3),(6,2),(6,8),(6,9),(6,10)}
        positions.update(gayab)


def main():
    running=True
    playing=False
    count=0
    generation = 0
    update_freq=30
    positions=set()

    #what to do when the simulation is running
    while running:
        clock.tick(FPS)
        if playing:
            count+=1
        if count>=update_freq:
            count=0
            positions=adjust_grid(positions)
            generation += 1

        pygame.display.set_caption(f"PLAYING - Generation: {generation}" if playing else f"PAUSED - Generation: {generation}")

        #exit the simulation
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

            #Cell alive/dead by mouse-click
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                col=x//TILE_SIZE
                row=y//TILE_SIZE
                pos=(col,row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            #Actions on pressing keys
            if event.type==pygame.KEYDOWN:
                #Pause and Play
                if event.key==pygame.K_SPACE:
                    if len(positions)==0:
                        load_pattern(positions, "glider")
                        playing=False
                    playing=not playing
                
                #Clear the grid
                if event.key==pygame.K_DELETE:
                    positions=set()
                    playing=False
                    count=0
                    generation = 0

                #Generate a Random pattern
                if event.key==pygame.K_r:
                    positions=gen(random.randrange(4,10)*GRID_WIDTH)

                #Step by step control
                if event.key == pygame.K_TAB: 
                    positions = adjust_grid(positions)
                    generation += 1
                
                #Load pre-defined patternes
                if event.key == pygame.K_1: 
                    load_pattern(positions, "glider")
                if event.key == pygame.K_2: 
                    load_pattern(positions, "blinker")
                if event.key == pygame.K_3: 
                    load_pattern(positions, "beacon")
                if event.key == pygame.K_4: 
                    load_pattern(positions, "pulsar")
                if event.key == pygame.K_5: 
                    load_pattern(positions, "block")
                if event.key == pygame.K_6: 
                    load_pattern(positions, "beehive")
                if event.key == pygame.K_7: 
                    load_pattern(positions, "loaf")
                if event.key == pygame.K_8: 
                    load_pattern(positions, "rangoli")
                if event.key == pygame.K_9: 
                    load_pattern(positions, "spaceship")
                if event.key == pygame.K_0: 
                    load_pattern(positions, "gayab")

        screen.fill(COLOR3)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__=="__main__":
    main()