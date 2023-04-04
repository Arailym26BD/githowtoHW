# Импортируем библиотеки
import pygame
# Инициализируем пайгейм
pygame.init()
# ширина,высота
WIDTH, HEIGHT = 400, 800
FPS = 20
#экран
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Music') # название

clock = pygame.time.Clock() # создать обьект,чтобы помочь отслеживать время

playlist = list()
playlist.append ("./music/konfuz.mp3" )
playlist.append ( "./music/safety net.mp3" )
playlist.append ( "./music/Nessa Barett feat jxdn - la di die.mp3" )
playlist.append ( "./music/By Индия - думать о тебе.mp3" )
playlist.append ( "./music/Скриптонит - Мистер 718.mp3" )
playlist.append ( "./music/Billie Eilish  Khalid - lovely.mp3" )
playlist.append ( "./music/Fetish.mp3" )
playlist.append ( "./music/Monster.mp3" )
playlist.append ( "./music/Shawn Mendes feat Khalid - Youth.mp3" )
playlist.append ( "./music/Billie Eilish - bad guy.mp3" )

pygame.mixer.music.load(playlist.pop()) # Получить первый трек из плейлиста
pygame.mixer.music.queue (playlist.pop()) # Очередь 2-й песни
pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Настраиваем событие конца трека
pygame.mixer.music.play() # Воспроизвести музыку

image=list()
image.append("./konfuz.jpg")
image.append("./ariana.jpg")
image.append("./la da die.jpg")
image.append("./думать о тебе.jpg")
image.append("./Мистер 718.jpg")
image.append("./lovely.jpg")
image.append("./fetish.jpg")
image.append("./monster.jpg")
image.append("./youth.jpg")
image.append("./bad guy.jpg")

          
img = pygame.image.load(image.pop())

def nextsong():
    global playlist
    playlist = playlist[1:] + [playlist[0]]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

def prevsong():
    global playlist
    playlist = [playlist[-1]] + playlist[:-1]
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()

finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finished=True
            if finished == True:
                pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pygame.mixer.music.stop()
                nextsong()
                image = image[1:] + [image[0]]
                img = pygame.image.load(image[0])
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                prevsong()
                image = [image[-1]] + image[:-1]
                img = pygame.image.load(image[0])
            if event.key==pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key==pygame.K_s:
                pygame.mixer.music.unpause()
            if event.key==pygame.K_1:
                pygame.mixer.music.set_volume(0.3)
            if event.key==pygame.K_2:
                pygame.mixer.music.set_volume(1)

        if event.type == pygame.USEREVENT:    # Трек закончился
            if len(playlist) > 0:       # Если в очереди больше дорожек
                pygame.mixer.music.queue(playlist.pop()) # Поставить в очередь следующий в списке
    screen.blit(pygame.transform.scale(img, (400, 800)), (0, 0))
    pygame.display.update()
pygame.quit()