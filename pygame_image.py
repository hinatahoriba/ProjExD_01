import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs =[bg_img,pg.transform.flip(bg_img, True, False)]
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs =[pg.transform.rotozoom(kk_img, i,1.0) for i in [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 1600
        if int(tmr/1600)%2 == 0:
            bg_num1 = 0
            bg_num2 = 1
        else:
            bg_num1 = 1
            bg_num2 = 0
        screen.blit(bg_imgs[bg_num1], [-x, 0])
        screen.blit(bg_imgs[bg_num2],[1600-x,0])
        screen.blit(kk_imgs[tmr%20], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()