import pygame,sys
from pygame.locals import *
import random,time
pygame.init()
BGWHITE=(255,255,255,205)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,128,0)
RED=(255,0,0)
AQUA=(0,255,255)
FPS=2
fps=pygame.time.Clock()
def screen():
    
    ANSURF=SURF.convert_alpha()
    ANSURF.fill(BGWHITE)
    SURF.blit(ANSURF,(0,0))

def main():
    global SURF
    SURF=pygame.display.set_mode((900,600))
    pygame.display.set_caption("SORTER")
    screen()
    
    X_mar,Y_mar=20,250
    GAP=10
    left,top=GAP+X_mar,Y_mar
    global BOXSIZE
    BOXSIZE=int((900-2*X_mar)/10)-GAP
    X_step=BOXSIZE+GAP
    global NUM
    NUM=random.sample(range(1,50),10)
    show(left,top,X_step,WHITE)

    left,top=GAP+X_mar,Y_mar
        
    pygame.display.update()
    time.sleep(4)
    
    
    for j in range(1,10):
       
        screen()
        key=NUM[j]
        i=j-1
        for x in range(10):
            if x==i:
                drawrec(left,top,NUM[x],GREEN)
                left=left+X_step
            elif x==j:
                drawrec(left,top,NUM[x],RED)
                left=left+X_step
            else:
                drawrec(left,top,NUM[x],WHITE)
                left=left+X_step


        left,top=GAP+X_mar,Y_mar
        
        pygame.display.update()
        pygame.time.delay(1000)
   
       

        while i>=0 and NUM[i]>key:
         
            NUM[i+1]=NUM[i]
            left_j,top_j=left+j*X_step,top-X_step
            left_i,top_i=left+i*X_step,top
            t=0
            while(t<=6):
           
                screen()
                pygame.time.delay(2)
                drawrec(left_j,top_j,key,RED)
                drawrec(left_i,top_i,NUM[i],GREEN)
                left_i=left_i+8
                left,top=GAP+X_mar,Y_mar
                for k in range(10):
                    '''if k in range(i+1,j):
                        drawrec(left+X_step,top,NUM[k+1],WHITE)
                        #left=left+X_step
                    if(k!= i and k!=j):
                        drawrec(left,top,NUM[k],WHITE)'''
                    if(k<i):
                        drawrec(left,top,NUM[k],WHITE)
                    if((k>i) and k<9):
                        drawrec(left+X_step,top,NUM[k+1],WHITE)

                        



                    
 
                    left=left+X_step
                t=t+1
                
                pygame.display.update()
                pygame.time.delay(100)
       


            
            left,top=GAP+X_mar,Y_mar
            i=i-1
        left,top=GAP+X_mar,Y_mar
        
        while(left_j>=GAP+X_mar+(i+1)*X_step):
            left,top=GAP+X_mar,Y_mar
            screen()
            pygame.time.delay(2)
            drawrec(left_j,top_j,key,RED)
            left_j=left_j-8
            for k in range(10):
                if(k!=i+1):
                    drawrec(left,top,NUM[k],WHITE)
                left=left+X_step
            pygame.display.update()
            pygame.time.delay(20)

        
        left_j=GAP+X_mar+(i+1)*X_step
        while(top>=top_j): 
            left,top=GAP+X_mar,Y_mar
            screen()
            pygame.time.delay(10)
            drawrec(left_j,top_j,key,RED)
            top_j=top_j+8
            for k in range(10):
                if(k!=i+1):
                    drawrec(left,top,NUM[k],WHITE)
                left=left+X_step
            pygame.display.update()
            pygame.time.delay(50)

            

            




        NUM[i+1]=key
        left,top=GAP+X_mar,Y_mar
        

    
    pygame.display.update()

    while True:
        screen()
        show(left,top,X_step,AQUA)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()


def drawrec(left,top,x,COLOR):
        RECT=pygame.Rect(left,top,BOXSIZE,BOXSIZE)
        pygame.draw.rect(SURF,COLOR,pygame.Rect(left,top,BOXSIZE,BOXSIZE))
        pygame.draw.rect(SURF,BLACK,pygame.Rect(left,top,BOXSIZE,BOXSIZE),3)
        fontObj = pygame.font.Font('freesansbold.ttf', 18)
        textSurfaceObj = fontObj.render(str(x), True, BLACK)
        SURF.blit(textSurfaceObj,(RECT.centerx-5,RECT.centery-5))
        
def show(left,top,X_step,COLOR):
    for x in range(10):
        drawrec(left,top,NUM[x],COLOR)
        left=left+X_step


if __name__=="__main__":
    main()




