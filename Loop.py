class Game:
    import pygame as pg
    import sys
    from random import randint
    import time
    import datetime

    def __init__(self, difficulty_level):
        self.Winning_Goal = 1000000
        self.pg.font.init()
        self.WHITE = (255, 255, 255)
        self.RED = (155, 10, 10)
        self.GREEN = (10, 155, 10)
        self.BEST_COLOR = (69, 69, 69)
        self.W = 595
        self.H = 500
        self.count_Points = self.count_MH = self.time_begin = self.time_end = self.count_rects = self.count_dots = 0
        self.count_Hand = 10
        self.Red_Price = 100
        self.Hand_Price = 250
        self.Buy_Auto = False
        self.Auto_Color = self.Video_Color = self.Hand_Color = self.RED
        self.Time_Start = self.time.time()
        self.clock = self.pg.time.Clock()
        self.sc = self.pg.display.set_mode((self.W, self.H))
        self.surf_top = self.pg.Surface((self.W, 50))
        self.surf_buy_button = self.pg.Surface((90, 20))
        self.surf_buy_button2 = self.pg.Surface((90, 20))
        self.Font_Title = self.pg.font.Font(None, 25)

        self.background_surf = self.pg.image.load('Textures/background.jpg')
        self.red_videocard = self.pg.image.load('Textures/red_videocard.png')
        self.hand = self.pg.image.load('Textures/hand.jpg')  # 64 100
        self.automation = self.pg.image.load('Textures/autimation.png')  # 51 80
        self.maldives = self.pg.image.load('Textures/maldives.jpg')  # fullscreen
        self.ticket = self.pg.image.load('Textures/ticket.jpg')  # 200 200
        self.Auto_Condition = "Disabled"
        self.str = "Hello!  This  is  a  game  about  saving  up  money "
        self.str2 = 'for a one-way ticket from Dolgoprudny.'
        self.red_videocard.set_colorkey((255, 255, 255))
        self.automation.set_colorkey((255, 255, 255))
        self.surf_download = None

    def Buy_Video(self):
        self.count_Points -= self.Red_Price
        self.Red_Price *= 2
        self.count_MH += 10
        self.Print_Points()

    def Buy_Hand(self):
        self.count_Points -= self.Hand_Price
        self.Hand_Price *= 3
        self.count_Hand *= 2
        self.Print_Points()

    def Draw_Ticket(self):
        self.sc.blit(self.Font_Title.render('You can buy a ticket', True, (255, 255, 255)), (self.W // 2 - 87, self.H // 2))
        self.sc.blit(self.ticket, (self.W // 2 - 100, self.H // 2 + 50))
        self.pg.display.update()

    def Download_Anim(self):
        self.clock.tick(30)
        self.surf_download = self.pg.Surface((self.W, 40))
        self.surf_download.fill(self.WHITE)
        self.surf_download.blit(self.Font_Title.render('downloading' + '.' * self.count_dots, True, (55, 155, 255)), (200, 10))
        self.sc.blit(self.surf_download, (0, 0))
        self.pg.display.update()

    def Print_Points(self):
        self.surf_top.fill(self.WHITE)
        self.surf_buy_button.fill(self.Video_Color)
        self.surf_buy_button2.fill(self.Hand_Color)
        self.surf_top.blit(self.Font_Title.render('MIPT Mining Simulator', True, (0, self.randint(40, 100), self.randint(40, 255))),
                      (80, 20))
        self.surf_top.blit(self.Font_Title.render('Auto: ' + self.Auto_Condition, True, self.Auto_Color), (self.W - 300, 2))
        self.surf_top.blit(self.Font_Title.render('Hand Earn: ' + str(self.count_Hand), True, (0, 0, 0)), (self.W - 140, 2))
        self.surf_top.blit(self.Font_Title.render('Money: ' + str(self.count_Points), True, (0, 0, 0)), (self.W - 300, 20))
        self.surf_top.blit(self.Font_Title.render('Money/s: ' + str(self.count_MH), True, (0, 0, 0)), (self.W - 140, 20))
        self.surf_buy_button.blit(self.Font_Title.render('Buy ' + str(self.Red_Price), True, self.WHITE), (0, 0))
        self.surf_buy_button2.blit(self.Font_Title.render('Buy ' + str(self.Hand_Price), True, self.WHITE), (0, 0))
        self.sc.blit(self.surf_buy_button, (self.W - 90, 120))
        self.sc.blit(self.surf_buy_button2, (self.W - 90, 220))
        self.sc.blit(self.surf_top, (0, 0))
        self.pg.display.update()

    def Start_Screen(self):
        self.sc.blit(self.background_surf, (0, 0))

        for i in self.str:
            if self.count_dots > 3:
                self.count_dots = 0
            else:
                self.count_dots += 1
            self.Download_Anim()
            letter = self.Font_Title.render(i, True, self.WHITE)
            self.sc.blit(letter, (100 + self.count_rects, self.H // 2 - 50))
            self.count_rects += self.pg.Surface.get_rect(letter)[2]

        self.count_rects = 0
        self.count_dots = 0
        for m in self.str2:
            if self.count_dots > 3:
                self.count_dots = 0
            else:
                self.count_dots += 1
            self.Download_Anim()
            letter = self.Font_Title.render(m, True, self.WHITE)
            self.sc.blit(letter, (100 + self.count_rects, self.H // 2 - 20))
            self.count_rects += self.pg.Surface.get_rect(letter)[2]
        self.sc.blit(self.Font_Title.render('You have to accumulate 1 Million', True, self.WHITE), (self.W // 2 - 140, self.H // 2 + 50))
        self.sc.blit(self.Font_Title.render('Press SPACE to start Mining', True, (0, 155, 255)), (self.W // 2, self.H // 2 + 210))
        self.pg.display.update()
        Start = False
        while not Start:
            for k in self.pg.event.get():
                if k.type == self.pg.KEYDOWN:
                    if k.key == self.pg.K_SPACE:
                        Start = True
                    if k.key == self.pg.K_ESCAPE:
                        exit()

    def Winning(self):
        Final = True
        Time_End = self.time.time()
        self.sc.blit(self.maldives, (0, 0))
        self.sc.blit(self.Font_Title.render('Congratulations! You left Dolgopa!', True, (69, 69, 69)), (200, self.H // 2 - 100))
        self.pg.display.update()
        self.pg.time.wait(500)
        res = self.datetime.timedelta(seconds=(Time_End - self.Time_Start))
        self.sc.blit(self.Font_Title.render('Game Time: ' + str(res), True, self.BEST_COLOR), (212, self.H // 2))
        self.pg.display.update()
        while Final:
            for j in self.pg.event.get():
                if j.type == self.pg.KEYDOWN:
                    if j.key == self.pg.K_ESCAPE:
                        Final = False
                        self.sys.exit()

    def auto_button_logic(self):
        if self.Buy_Auto:
            self.Buy_Auto = False
        else:
            self.Buy_Auto = True
        if self.Auto_Condition == "Disabled":
            self.Auto_Condition = "Enable"
            self.Auto_Color = self.GREEN
        else:
            self.Auto_Condition = "Disabled"
            self.Auto_Color = self.RED

    def run_economy_logic(self):
        if self.count_MH >= 0:
            if self.time_begin == 0:
                self.time_begin = self.time.time()
            time_end = self.time.time()
            if time_end - self.time_begin >= 1:
                self.count_Points += self.count_MH
                self.time_begin = time_end
        if self.count_Points >= self.Red_Price and self.Buy_Auto:
            self.Buy_Video()
        if self.count_Points >= self.Hand_Price and self.Buy_Auto:
            self.Buy_Hand()
        if self.count_Points >= self.Hand_Price:
            self.Hand_Color = self.GREEN
        else:
            self.Hand_Color = self.RED
        if self.count_Points >= self.Red_Price:
            self.Video_Color = self.GREEN
        else:
            self.Video_Color = self.RED

    def clear_download_screen(self):
        self.pg.draw.rect(self.surf_top, (255, 255, 255), (0, 0, self.W, 50))
        self.pg.draw.rect(self.surf_buy_button, self.Video_Color, (0, 0, 100, 30))
        self.pg.draw.rect(self.surf_buy_button2, self.Hand_Color, (0, 0, 100, 30))

        self.sc.blit(self.background_surf, (0, 0))
        self.sc.blit(self.red_videocard, (self.W - 100, 60))
        self.sc.blit(self.hand, (self.W - 80, 150))
        self.sc.blit(self.automation, (50, 450))
        self.sc.blit(self.surf_buy_button, (self.W - 90, 120))
        self.sc.blit(self.surf_buy_button2, (self.W - 90, 220))

        self.sc.blit(self.Font_Title.render('+ 10 Auto Money/Second ', True, (255, 255, 255)), (291, 83))
        self.sc.blit(self.Font_Title.render('* 2 Hand Earn ', True, (255, 255, 255)), (375, 180))

    def run_game_loop(self):
        RUNNING = True
        Ticket_drew = False

        self.clear_download_screen()
        self.Print_Points()

        while RUNNING:
            for i in self.pg.event.get():
                if i.type == self.pg.QUIT:
                    sys.exit()
                elif i.type == self.pg.KEYDOWN:
                    if i.key == self.pg.K_ESCAPE:
                        RUNNING = False
                    if i.key == self.pg.K_SPACE:
                        self.count_Points += self.count_Hand
                        self.Print_Points()
                        self.sc.blit(self.surf_top, (0, 0))
                elif i.type == self.pg.MOUSEBUTTONUP:
                    if self.count_Points >= self.Red_Price and ((self.W >= i.pos[0] >= self.W - 90 and 140 >= i.pos[1] >= 120) or
                                                                self.Buy_Auto):
                        self.Buy_Video()

                    if self.count_Points >= self.Hand_Price and (
                            (self.W >= i.pos[0] >= self.W - 90 and 240 >= i.pos[1] >= 220) or
                            self.Buy_Auto):
                        self.Buy_Hand()

                    if 150 >= i.pos[0] >= 50 and 486 >= i.pos[1] >= 450: #Auto Button's position
                        self.auto_button_logic()

                    if Ticket_drew and (
                            self.W // 2 + 100 >= i.pos[0] >= self.W // 2 - 100 and self.H // 2 + 200 >= i.pos[1] >= self.H // 2 + 50):
                        RUNNING = False
                        self.Winning()

                    self.Print_Points()

            self.run_economy_logic()

            if self.count_Points >= self.Winning_Goal and not Ticket_drew:
                self.Draw_Ticket()
                Ticket_drew = True

                # чит для быстрого фарма монет (нажать 'c' на клавиатуре)
            keys = self.pg.key.get_pressed()
            if keys[self.pg.K_c]:
                self.count_Points += 500
            self.Print_Points()
