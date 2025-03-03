
import pygame 
import sys 
  
  
# initializing the constructor 
pygame.init() 
  
# screen resolution 
res = (1900,1080) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = 150 
  
# stores the height of the 
# screen into a variable 
height = 100
buttonSizeX = 350
buttonSizeY = 700
button2 = 1900-width

  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
  
screen.fill((60,25,60)) 
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width <= mouse[0] <= width+buttonSizeX and height <= mouse[1] <= height+buttonSizeY: 
                screen.fill((60,25,60)) 
                screen.blit(smallfont.render('Misinformation', True, color), (1700/2,50)) 
                pygame.display.update() 
            if button2 <= mouse[0] <= button2-buttonSizeX and height <= mouse[1] <= height+buttonSizeY: 
                screen.fill((60,25,60)) 
                screen.blit(smallfont.render('Correct', True, color), (1700/2,50)) 
                pygame.display.update() 


    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    if width <= mouse[0] <= width+buttonSizeX and height <= mouse[1] <= height+buttonSizeY: 
        pygame.draw.rect(screen,color_dark,[width,height,buttonSizeX,buttonSizeY]) 
          
    if button2<= mouse[0] <= button2-buttonSizeX and height <= mouse[1] <= height+buttonSizeY: 
        pygame.draw.rect(screen,color_dark,[button2-buttonSizeX,height,button2,buttonSizeY]) 
    else: 
        pygame.draw.rect(screen,color_light,[button2-buttonSizeX,height,button2,buttonSizeY]) 
        pygame.draw.rect(screen,color_light,[width,height,buttonSizeX,buttonSizeY]) 
    # superimposing the text onto our button 
    screen.blit(smallfont.render('False', True, color), (width+buttonSizeX/2,height+ buttonSizeY/2)) 
      
    # updates the frames of the game 
    pygame.display.update() 

