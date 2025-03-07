import pygame 
import sys 

pygame.init() 

# Screen resolution 
res = (1900, 1080) 
screen = pygame.display.set_mode(res) 

# Colors 
color = (255, 255, 255) 
color_light = (170, 170, 170) 
color_dark = (100, 100, 100) 

# Button sizes & positions
width = 150
height = 100
buttonSizeX = 350
buttonSizeY = 700
button2 = 1900 - width  # Right button position

# Font
smallfont = pygame.font.SysFont('Corbel', 35) 

screen.fill((60, 25, 60)) 

dato = open("scenarier/dato.txt","r")
datostr = dato.read()
print(datostr)
while True: 
    mouse = pygame.mouse.get_pos()  # Move this here!

    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()

        # check if the mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if width <= mouse[0] <= width + buttonSizeX and height <= mouse[1] <= height + buttonSizeY: 
                screen.fill((60, 25, 60)) 
                wrongtext = smallfont.render('Wrong', True, color)
                screen.blit(wrongtext, ((res[0] - wrongtext.get_width()) // 2, 50)) 
                pygame.display.update() 


            if button2 - buttonSizeX <= mouse[0] <= button2 and height <= mouse[1] <= height + buttonSizeY: 
                screen.fill((60, 25, 60)) 
                correcttext = smallfont.render('Correct', True, color)
                screen.blit(correcttext, ((res[0] - correcttext.get_width()) // 2, 50))
                pygame.display.update() 

    # Draw buttons with hover effect
    if width <= mouse[0] <= width + buttonSizeX and height <= mouse[1] <= height + buttonSizeY: 
        pygame.draw.rect(screen, color_dark, [width, height, buttonSizeX, buttonSizeY])  
    else:
        pygame.draw.rect(screen, color_light, [width, height, buttonSizeX, buttonSizeY])  

    if button2 - buttonSizeX <= mouse[0] <= button2 and height <= mouse[1] <= height + buttonSizeY: 
        pygame.draw.rect(screen, color_dark, [button2 - buttonSizeX, height, buttonSizeX, buttonSizeY])  
    else:  
        pygame.draw.rect(screen, color_light, [button2 - buttonSizeX, height, buttonSizeX, buttonSizeY])  

    # Add text labels to buttons
    screen.blit(smallfont.render('False', True, color), (width + buttonSizeX / 2 - 30, height + buttonSizeY / 2))  
    screen.blit(smallfont.render('True', True, color), (button2 - buttonSizeX / 2 - 30, height + buttonSizeY / 2))  

    screen.blit(smallfont.render(datostr, True, color), (550,100))

    pygame.display.update()  

