# Импортируем библиотеки
import pygame  
from datetime import datetime
import time
# Инициализируем пайгейм
pygame.init()

WHITE = (255, 255, 255)
FPS = 1
theFont=pygame.font.Font(None,72) # шрифт по-умолчанию

screen = pygame.display.set_mode((700, 525)) # экран
clock = pygame.time.Clock() # создать обьект,чтобы помочь отслеживать время
image = pygame.image.load('mickey.png') # импортим фотки
image_s = pygame.image.load('seconds.png') 
image_m = pygame.image.load('minutes.png') 

def blitRotate(surf, image, pos, angle):

    r_image = pygame.transform.rotate(image, angle) # Величина отрицательного угла будет вращаться по часовой стрелке.
    rect = image.get_rect(center = pos) # вернет прямоугольник, координата центра которого будет иметь значение pos.

    rot_rect = r_image.get_rect(center = rect.center) 
    surf.blit(r_image, rot_rect) 
def angle(an):
    return an * -6
sec = datetime.now().strftime('%S') 
min = datetime.now().strftime('%M')
# angle_s = int(sec) * -6
# angle_m = int(min) * -6
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill(WHITE) # заполняем фон белым
    screen.blit(image,(0, 0)) # блит фото в координате (0,0)
    blitRotate(screen, image_s, (349.4, 261.75), angle(int(sec)+2)) 
    blitRotate(screen, image_m, (349.5, 262), angle(int(min)))
    sec = datetime.now().strftime('%S')
    min = datetime.now().strftime('%M')
    angle_s = int(sec) * -6
    angle_m = int(min) * -6
    theTime=time.strftime("%H:%M:%S", time.localtime()) 
    timeText=theFont.render(str(theTime), True,(0,0,0),(255,0,0))
    screen.blit(timeText, (0,0)) # блитим время
    pygame.display.update()
pygame.quit()