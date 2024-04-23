import os
import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1600, 900
DELTA = {#こうかトン移動用辞書
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5,0),
    pg.K_RIGHT: (+5,0),
}
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def check(any_rct):
    """
    動く物体の画面外判定
    横，縦
    """
    yoko, tate=True, True
    if any_rct.left <= 0 or WIDTH <= any_rct.right:
        yoko=False
    if any_rct.up <= 0 or HEIGHT <= any_rct.dottom:
        tate=False
    return yoko,tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()
    tmr = 0
    bomb_img = pg.Surface((20,20))
    pg.draw.circle(bomb_img, (255, 0, 0), (10, 10), 10)
    bomb_img.set_colorkey((0, 0, 0))
    bb_rect = bomb_img.get_rect()
    bb_rect.center = random.randint(0,WIDTH), random.randint(0,HEIGHT)
    vx = +5
    vy = +5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k, v in DELTA.items():#こうかトン移動用
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)
        bb_rect.move_ip(vx, vy)
        screen.blit(kk_img, kk_rct)
        screen.blit(bomb_img, bb_rect)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
