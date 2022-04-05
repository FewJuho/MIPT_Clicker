import pygame as pg
import sys
from random import randint
import time
import datetime

pg.font.init()
WHITE = (255, 255, 255)
RED = (155, 10, 10)
GREEN = (10, 155, 10)
BEST_COLOR = (69, 69, 69)
W = 595
H = 500
RUNNING = True
Buy_Auto = False
Ticket_drew = False
count_Points = 0
count_MH = 0
count_Hand = 10
Red_Price = 100
Hand_Price = 250
time_begin = 0
time_end = 0
Auto_Condition = "Disabled"
Auto_Color = RED
Video_Color = RED
Hand_Color = RED
Time_Start = time.time()
clock = pg.time.Clock()


def Print_Points():
    surf_top.fill(WHITE)
    surf_buy_button.fill(Video_Color)
    surf_buy_button2.fill(Hand_Color)
    surf_top.blit(Font_Title.render('MIPT Mining Simulator', True, (0, randint(40, 100), randint(40, 255))), (80, 20))
    surf_top.blit(Font_Title.render('Auto: ' + Auto_Condition, True, Auto_Color), (W - 300, 2))
    surf_top.blit(Font_Title.render('Hand Earn: ' + str(count_Hand), True, (0, 0, 0)), (W - 140, 2))
    surf_top.blit(Font_Title.render('Money: ' + str(count_Points), True, (0, 0, 0)), (W - 300, 20))
    surf_top.blit(Font_Title.render('Money/s: ' + str(count_MH), True, (0, 0, 0)), (W - 140, 20))
    surf_buy_button.blit(Font_Title.render('Buy ' + str(Red_Price), True, WHITE), (0, 0))
    surf_buy_button2.blit(Font_Title.render('Buy ' + str(Hand_Price), True, WHITE), (0, 0))
    sc.blit(surf_buy_button, (W - 90, 120))
    sc.blit(surf_buy_button2, (W - 90, 220))
    sc.blit(surf_top, (0, 0))
    pg.display.update()


def Buy_Video():
    global count_Points, Red_Price, count_MH
    count_Points -= Red_Price
    Red_Price *= 2
    count_MH += 10
    Print_Points()


def Buy_Hand():
    global count_Points, Hand_Price, count_Hand
    count_Points -= Hand_Price
    Hand_Price *= 3
    count_Hand *= 2
    Print_Points()


def Draw_Ticket():
    sc.blit(Font_Title.render('You can buy a ticket', True, (255, 255, 255)), (W // 2 - 87, H // 2))
    sc.blit(ticket, (W // 2 - 100, H // 2 + 50))
    pg.display.update()


def Download_Anim(count_dots):
    clock.tick(30)
    surf_download = pg.Surface((W, 40))
    surf_download.fill(WHITE)
    surf_download.blit(Font_Title.render('downloading' + '.' * count_dots, True, (55, 155, 255)), (200, 10))
    sc.blit(surf_download, (0, 0))
    pg.display.update()


def Start_Screen():
    background_surf = pg.image.load('background.jpg')
    sc.blit(background_surf, (0, 0))

    str = "Hello!  This  is  a  game  about  saving  up  money "
    count_rects = 0
    count_dots = 0

    for i in str:
        if count_dots > 3:
            count_dots = 0
        else:
            count_dots += 1
        Download_Anim(count_dots)
        letter = Font_Title.render(i, True, WHITE)
        sc.blit(letter, (100 + count_rects, H // 2 - 50))
        count_rects += pg.Surface.get_rect(letter)[2]

    str2 = 'for a one-way ticket from Dolgoprudny.'
    count_rects = 0
    count_dots = 0

    for m in str2:
        if count_dots > 3:
            count_dots = 0
        else:
            count_dots += 1
        Download_Anim(count_dots)
        letter = Font_Title.render(m, True, WHITE)
        sc.blit(letter, (100 + count_rects, H // 2 - 20))
        count_rects += pg.Surface.get_rect(letter)[2]
    sc.blit(Font_Title.render('You have to accumulate 1 Million', True, WHITE), (W // 2 - 140, H // 2 + 50))
    sc.blit(Font_Title.render('Press SPACE to start Mining', True, (0, 155, 255)), (W // 2, H // 2 + 210))
    pg.display.update()
    Start = False
    while not Start:
        for k in pg.event.get():
            if k.type == pg.KEYDOWN:
                if k.key == pg.K_SPACE:
                    Start = True
                if k.key == pg.K_ESCAPE:
                    exit()


def Winning():
    global Time_Start, RUNNING
    Final = True
    Time_End = time.time()
    sc.blit(maldives, (0, 0))
    sc.blit(Font_Title.render('Congratulations! You left Dolgopa!', True, (69, 69, 69)), (200, H // 2 - 100))
    pg.display.update()
    pg.time.wait(500)
    res = datetime.timedelta(seconds=(Time_End - Time_Start))
    sc.blit(Font_Title.render('Game Time: ' + str(res), True, BEST_COLOR), (212, H // 2))
    pg.display.update()
    while Final:
        for j in pg.event.get():
            if j.type == pg.KEYDOWN:
                if j.key == pg.K_ESCAPE:
                    Final = False


sc = pg.display.set_mode((W, H))
surf_top = pg.Surface((W, 50))
surf_buy_button = pg.Surface((90, 20))
surf_buy_button2 = pg.Surface((90, 20))
background_surf = pg.image.load('background.jpg')
red_videocard = pg.image.load('red_videocard.png')
hand = pg.image.load('hand.jpg')  # 64 100
automation = pg.image.load('autimation.png')  # 51 80
maldives = pg.image.load('maldives.jpg') #fullscreen
ticket = pg.image.load('ticket.jpg') #200 200
red_videocard.set_colorkey((255, 255, 255))
automation.set_colorkey((255, 255, 255))

Font_Title = pg.font.Font(None, 25)

Start_Screen()

pg.draw.rect(surf_top, (255, 255, 255), (0, 0, W, 50))
pg.draw.rect(surf_buy_button, Video_Color, (0, 0, 100, 30))
pg.draw.rect(surf_buy_button2, Hand_Color, (0, 0, 100, 30))

sc.blit(background_surf, (0, 0))
sc.blit(red_videocard, (W - 100, 60))
sc.blit(hand, (W - 80, 150))
sc.blit(automation, (50, 450))
sc.blit(surf_buy_button, (W - 90, 120))
sc.blit(surf_buy_button2, (W - 90, 220))

sc.blit(Font_Title.render('+ 10 Auto Money/Second ', True, (255, 255, 255)), (291, 83))
sc.blit(Font_Title.render('* 2 Hand Earn ', True, (255, 255, 255)), (375, 180))

Print_Points()

while RUNNING:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_ESCAPE:
                RUNNING = False
            if i.key == pg.K_SPACE:
                count_Points += count_Hand
                Print_Points()
                sc.blit(surf_top, (0, 0))
        elif i.type == pg.MOUSEBUTTONUP:
            if count_Points >= Red_Price and ((W >= i.pos[0] >= W - 90 and 140 >= i.pos[1] >= 120) or Buy_Auto):
                Buy_Video()
            if count_Points >= Hand_Price and ((W >= i.pos[0] >= W - 90 and 240 >= i.pos[1] >= 220) or Buy_Auto):
                Buy_Hand()
            if 150 >= i.pos[0] >= 50 and 486 >= i.pos[1] >= 450:
                if Buy_Auto:
                    Buy_Auto = False
                else:
                    Buy_Auto = True
                if Auto_Condition == "Disabled":
                    Auto_Condition = "Enable"
                    Auto_Color = GREEN
                else:
                    Auto_Condition = "Disabled"
                    Auto_Color = RED
            if Ticket_drew and (W // 2 + 100 >= i.pos[0] >= W // 2 - 100 and H // 2 + 200 >= i.pos[1] >= H // 2 + 50):
                RUNNING = False
                Winning()

            Print_Points()
    pos = pg.mouse.get_pos()
    if count_MH >= 0:
        if time_begin == 0:
            time_begin = time.time()
        time_end = time.time()
        if time_end - time_begin >= 1:
            count_Points += count_MH
            time_begin = time_end
    if count_Points >= Red_Price and Buy_Auto:
        Buy_Video()
    if count_Points >= Hand_Price and Buy_Auto:
        Buy_Hand()
    if count_Points >= Hand_Price:
        Hand_Color = GREEN
    else:
        Hand_Color = RED
    if count_Points >= Red_Price:
        Video_Color = GREEN
    else:
        Video_Color = RED
    if count_Points >= 1000000 and not Ticket_drew:
        Draw_Ticket()
        Ticket_drew = True

        # чит для быстрого фарма монет
    keys = pg.key.get_pressed()
    if keys[pg.K_m] and keys[pg.K_i] and keys[pg.K_p] and keys[pg.K_t]:
        count_Points += 50
    Print_Points()
