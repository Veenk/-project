import pygame
import time

pygame.init()
'параметры окна'
black = (0,0,0)
red = (150,0,0)
bright_red = (255,0,0)
white = (255,255,255)
green = (0, 150, 0)
bright_green = (0,255,0)
resolution = (width, height) = (1820,900)
GameWindow = pygame.display.set_mode(resolution)
pygame.display.set_caption('fight for zachet')
clock = pygame.time.Clock()
'импорт моделей'
rmodel1 = model1 = pygame.image.load('left1.png')
rmodel1_punch1 = model1_punch1 = pygame.image.load('left3.png')
rmodel2 = model2 = pygame.image.load('right1.png')
rmodel2_punch = model2_punch = pygame.image.load('right2.png')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
'переменные для loop'
orient = rorient = str('forward')
forward = rforward = str('forward')
backward = rbackward = str('backward')
punch = rpunch = str('punch')
fpunch = rfpunch = str('fpunch')
bpunch = rbpunch =str('bpunch')
forward = orient = str('forward')
rorient = rforward
pygame.mixer.music.load('maintheme.wav')
bg = pygame.image.load('bg2.png')
bg1 = pygame.image.load('bg11.png')
l_to_win = r_to_win = 0
lhp = rhp = 100
win = -1
pause = False
          
def Lmod(lx,ly,orient,punch):
     if orient == forward:
          GameWindow.blit(model1, (lx,ly))
          if punch == fpunch:
               GameWindow.blit(bg, (0,0))
               GameWindow.blit(model1_punch1, (lx+30,ly))
          
     elif orient == backward:
          GameWindow.blit(model2, (lx,ly))
          if punch == bpunch:
               GameWindow.blit(bg, (0,0))
               GameWindow.blit(model2_punch, (lx-240,ly))

def Rmod(rx,ry,rorient,rpunch,lx,ly,orient,punch):
     if rorient == rforward:
          GameWindow.blit(rmodel2, (rx,ry))
          if rpunch == rfpunch:
               if orient == forward:
                    if punch == fpunch:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel2_punch, (rx-200,ry))
                         GameWindow.blit(model1_punch1, (lx+30,ly))
                    else:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel2_punch, (rx-200,ry))
                         GameWindow.blit(model1, (lx,ly))
               elif orient == backward:
                    if punch == bpunch:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel2_punch, (rx-240,ry))
                         GameWindow.blit(model2_punch, (lx-240,ly)) 
                    else:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel2_punch, (rx-240,ry))
                         GameWindow.blit(model2, (lx,ly))            
     else:
          rorient = rbackward
          GameWindow.blit(rmodel1, (rx,ry))
          if rpunch == rbpunch:
               if orient == forward:
                    if punch == fpunch:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel1_punch1, (rx+30,ry))
                         GameWindow.blit(model1_punch1, (lx+30,ly))
                    else:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel1_punch1, (rx+30,ry))
                         GameWindow.blit(model1, (lx,ly))
               elif orient == backward:
                    if punch == bpunch:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel1_punch1, (rx+30,ry))
                         GameWindow.blit(model2_punch, (lx-240,ly))
                    else:
                         GameWindow.blit(bg, (0,0))
                         GameWindow.blit(rmodel1_punch1, (rx+30,ry))
                         GameWindow.blit(model2, (lx,ly))    

def hp(lhp,rhp):
     font = pygame.font.SysFont(None,60)
     textl = font.render("HP: " + str(lhp), True, red)
     textr = font.render("HP: " + str(rhp), True, red)
     GameWindow.blit (bg1, (0,0))
     GameWindow.blit (textl, (0,0))
     GameWindow.blit (textr, (width - 150,0))
def compare(l_to_win, r_to_win, win, lhp, rhp):
##     while l_to_win <= 10 and r_to_win <= 10:
##          if l_to_win <= 10:
##               lhp -= 10
##          elif r_to_win <= 10:
##               rhp -= 10
     hp(lhp,rhp)
     if l_to_win == 20 and l_to_win > r_to_win:
          win = 1
     elif r_to_win == 20 and r_to_win > l_to_win:
          win = 0
     PopMessageDeath(win)
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_window(text):
    LargeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, LargeText, black)
    TextRect.center = ((width/2),(height/2))
    GameWindow.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
def PopMessageDeath(win):
     if win == 1:
         message_window('Left Player WINS')
     if win == 0:
         message_window('Right Player WINS')
         
def button(txt,x,y,w,h,accol,inaccol,do = None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x + w > mouse[0] > x and y + h > mouse[1] > y:
          pygame.draw.rect(GameWindow, accol, (x,y,w,h))
          if click[0] == 1 and do != None:
               do()
     else:
          pygame.draw.rect(GameWindow, inaccol, (x,y,w,h))
          
     SmallText = pygame.font.Font('freesansbold.ttf', 50)
     TextSurf, TextRect = text_objects(txt, SmallText, black)
     TextRect.center = ((x + (w/2)), (y + (h/2)))
     GameWindow.blit(TextSurf, TextRect)
def unpause():
     global pause
     pause = False
def paused():
     while pause:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          
          LargeText = pygame.font.Font('freesansbold.ttf', 115)
          TextSurf, TextRect = text_objects('THE GAME IS PAUSED', LargeText, black)
          TextRect.center = ((width/2),(height/2))
          GameWindow.blit(TextSurf, TextRect)
          
          button('CONTINUE',355,550,500,300,bright_green,green,unpause)
          button('EXIT',975,550,500,300,bright_red,red,Quit)
          
          pygame.display.update()
          clock.tick(5)
def Quit():
     pygame.quit()
     quit()
def game_intro():
     intro = True
     while intro:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
          GameWindow.fill(white)
          LargeText = pygame.font.Font('freesansbold.ttf', 115)
          TextSurf, TextRect = text_objects('FIGHT FOR ZACHET', LargeText, black)
          TextRect.center = ((width/2),(height/2))
          GameWindow.blit(TextSurf, TextRect)
          
          button('FIGHT',355,550,500,300,bright_green,green,game_loop)
          button('EXIT',975,550,500,300,bright_red,red,Quit)
          
          pygame.display.update()
          clock.tick(5)
          
def game_loop():
    GameWindow.blit(bg1, (0,0))
    global pause
    #pygame.mixer.music.play(-1)
    Rx = (width * 0.8)
    Ry = (height -650)
    Lx = (width * 0.2)
    Ly = (height -650)
    x_change = rx_change = 0
    orient = rorient = str('forward')
    forward = rforward = str('forward')
    backward = rbackward = str('backward')
    punch = str('forward')
    rpunch = str('backward')
    fpunch = rfpunch = str('fpunch')
    bpunch = rbpunch =str('bpunch')
    r_to_win = l_to_win = 0
    win = -1
    delta_hp = 5
    rhp = lhp = 100
    Exit = False

    while Exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                     if orient == forward:
                         punch = fpunch
                     elif orient == backward:
                         punch = bpunch
                         
                if event.key == pygame.K_a: 
                    x_change = -8
                    if orient == forward:
                         orient = backward
                    
                if event.key == pygame.K_d: 
                    x_change = 8
                    if orient == backward:
                         orient = forward
                    
                    
                if event.key == pygame.K_p:
                     if rorient == rforward:
                         rpunch = rfpunch
                     else:
                         rpunch = rbpunch
                         
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                         
                if event.key == pygame.K_RIGHT: 
                    rx_change = 8
                    if rorient == rforward:
                         rorient = rbackward
                    
                if event.key == pygame.K_LEFT: 
                    rx_change = -8
                    if rorient == rbackward:
                         rorient = rforward
                         
            if event.type == pygame.KEYUP:
                 
                  if event.key == pygame.K_d or event.key == pygame.K_a: 
                      x_change = 0
                      if event.key == pygame.K_d:
                           orient = forward
                      elif event.key == pygame.K_a:
                           orient = backward
                           
                  if event.key == pygame.K_t:
                      punch = forward
                      
                  if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                      rx_change = 0
                      
                      if event.key == pygame.K_RIGHT:
                           rorient = rbackward
                      elif event.key == pygame.K_LEFT:
                           rorient = rforward
                           
                  if event.key == pygame.K_p:
                      rpunch = str('forward')
                           
        GameWindow.blit(bg, (0,0))
        Lx += x_change
        Rx += rx_change
        if Lx < 0:
          Lx = 15
          GameWindow.blit(bg, (0,0))
          GameWindow.blit(model2, (Lx,Rx))
        elif Lx+180 > width:
          Lx = width - 195
          GameWindow.blit(bg, (0,0))
          GameWindow.blit(model2, (Lx,Rx))
        if Rx < 0:
          Rx = 15
          GameWindow.blit(bg, (0,0))
          GameWindow.blit(model1, (Lx,Rx))
        elif Rx+180 > width:
          Rx = width - 195
          GameWindow.blit(bg, (0,0))
          GameWindow.blit(model1, (Lx,Rx))

##        if rpunch == rfpunch:          
##               if orient == forward  and rorient == rforward:
##                    if punch == forward and (Rx+26 >= Lx+64 and Rx+26 <= Lx+140):
##                         r_to_win += 1
##                         lhp -= delta_hp
##                         compare(l_to_win, r_to_win, win, lhp, rhp)
##                    elif punch == fpunch and (Rx+26 >= Lx+163 and Rx+26 <= Lx+229):
##                         r_to_win += 1
##                         lhp -= delta_hp
##                         compare(l_to_win, r_to_win, win, lhp, rhp)
##               elif orient == forward and rorient == rbackward:
##                    if punch == forward and (Rx+26 >= Lx+40 and Rx+26 <= Lx+110):
##                         r_to_win += 1
##                         lhp -= delta_hp
##                         compare(l_to_win, r_to_win, win, lhp, rhp)
##                    elif punch == fpunch and (Rx+26 >= Lx+161 and Rx+26 <= Lx+231):
##                         r_to_win += 1
##                         lhp -= delta_hp
##                         compare(l_to_win, r_to_win, win, lhp, rhp)
          
        if punch == fpunch:
               if orient == forward and rorient == rforward:
                    if rpunch == backward and (Lx+381 >= Rx+40 and Lx+383 <= Rx+110):
                         l_to_win += 1
                         rhp -= delta_hp
                         compare(l_to_win, r_to_win, win, lhp, rhp)
                    elif rpunch == rfpunch and (Lx+381 >= Rx+163 and Lx+381 <= Rx+229):
                         l_to_win += 1
                         rhp -= delta_hp
                         compare(l_to_win, r_to_win, win, lhp, rhp)
               elif orient == forward and rorient == rbackward:
                    if rpunch == backward and (Lx+381 >= Rx+64 and Lx+381 <= Rx+140):
                         l_to_win += 1
                         rhp -= delta_hp
                         compare(l_to_win, r_to_win, win, lhp, rhp)
                    elif rpunch == rbpunch and (Lx+381 >= Rx+161 and Lx+381 <= Rx+231):
                         l_to_win += 1
                         rhp -= delta_hp
                         compare(l_to_win, r_to_win, win, lhp, rhp)
   

        Lmod(Lx,Ly,orient,punch)
        Rmod(Rx,Ry,rorient,rpunch,Lx,Ly,orient,punch)
        
        pygame.display.update()
        clock.tick(150)
game_intro()        
game_loop()
pygame.quit()
quit()
