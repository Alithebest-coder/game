import  pygame
pygame.init()

screen=pygame.display.set_mode ((800,600))
pygame.display.set_caption("space invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
running=True

while running:
    screen.fill((255,192,203))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()