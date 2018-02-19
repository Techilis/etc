import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
#(800,600) as a tuple hence it understands it as one perimeter

pygame.display.set_caption('Car Race')
#Change title of window

clock = pygame.time.Clock()
#Keep track of time

crashed = False
#Variable to see if game ends

while not crashed:
    for event in pygame.event.get():
        #get any events, keys pressed etc
        if event.type == pygame.QUIT:
            #pygame.QUIT appear when user clicks on X on window
            #Can ask 'Are you sure you want to quit?'
            crashed = True
        print(event)
    pygame.display.update()
    clock.tick(60) #Number = frames per second

pygame.quit()
quit()
            


