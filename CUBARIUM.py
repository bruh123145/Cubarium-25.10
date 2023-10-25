import pygame
from random import *
import time
pygame.init()
fon = (204, 255, 255)
mw = pygame.display.set_mode((750, 750))
mw.fill(fon)
clock = pygame.time.Clock()
R = randint(10, 740)
R2 = randint(10, 740)
R3 = randint(10, 740)
R4 = randint(10, 740)
# змінні для робити програми. Мабуть, вони вже не потрібні
counti = 0
counti2 = 0
run = True
RIGHT = False
LEFT = False
RIGHT_S = False
LEFT_S = False
JUMP = False
JUMP_S = False
jumpCount1 = 12
jumpCount2 = 12
x = 50
GAMEOVER = False
c = False
bx1 = 10
bx2 = 10
def home_title():
    # Встановлення початкового виду гри
    global bull
    bull = False
    lst = [hp1, hp2, coins_txt_katka, stuck, coins_txt, coins_bg, select_ch, select_ch2, select_ch3, select_ch4, select_ch5, shop_agentka, shop_pegion, shop_cube1, shop_cube2, shop_kot1, shop_kot2, shop_minecube1, shop_minecube2, shop_pegion, shop_agentka, shop_mrcube1, shop_mrcube2, selected_ch, selected_ch, num_25, num_50, num_100, num_130, characters, wallpapers, next_goods, back_goods, back, mahazina, start, continue_game, game_over, game_over_text, game_over_points, game_over_total, game_over_text_time, bullet, bullet2, bullet3, bullet4, cube, cube_s]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    home.rect.x = 0
    home.rect.y = 0
    exit.rect.x = 312
    exit.rect.y = 660
    shop.rect.x = 550
    shop.rect.y = 500
    ok.rect.x = 300
    ok.rect.y = 560
def instruct():
    # Інструкція щодо гри
    lst = [mahazina, shop, exit, home]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    ok.rect.y = 640
    start.rect.x = 0
    start.rect.y = 0
def game():
    # Запуск самої гри
    global bull
    bull = True
    lst = [coins_txt_katka, stuck, coins_txt, coins_bg, game_over, game_over_text, game_over_total, game_over_points, continue_game, exit, mahazina, ok, start]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    bullet.rect.x = R
    bullet.rect.y = 105
    bullet2.rect.x = R2
    bullet2.rect.y = 105
    bullet3.rect.x = R3
    bullet3.rect.y = 105
    bullet4.rect.x = R4
    bullet4.rect.y = 105
    cube.rect.x = 300
    cube.rect.y = 500
    cube_s.rect.x = 50
    cube_s.rect.y = 500
    hp1.rect.x = 0
    hp1.rect.y = 0
    hp2.rect.x = 600
    hp2.rect.y = 0
def game_over_title():
    global bull
    bull = False
    # Встановлення вікна програшу
    lst = [hp1, hp2, stuck, coins_txt, coins_bg, characters, wallpapers, mahazina, start, bullet, bullet2, bullet3, bullet4, cube, cube_s, exit]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    continue_game.rect.x = 200
    continue_game.rect.y = 650
    game_over_text.rect.x = 100
    game_over_text.rect.y = 650
    game_over.rect.x = 0
    game_over.rect.y = -1
    game_over_text_time.rect.x = 400
    game_over_text_time.rect.y = 280
    game_over_total.rect.x = 400
    game_over_total.rect.y = 550
    game_over_points.rect.x = 400
    game_over_points.rect.y = 370
    coins_txt_katka.rect.x = 400
    coins_txt_katka.rect.y = 450
    continue_game.rect.x = 250
    continue_game.rect.y = 650
def characters_m():
    # Відображення вікна з персонажами в магазині
    coins_bg.rect.x = 490
    coins_bg.rect.y = 30
    coins_txt.rect.x = 500
    coins_txt.rect.y = 50
    coins_txt.set_text(f"{coins}", 36, (255, 255, 255))
    stuck.rect.x = 630
    stuck.rect.y = 30
    next_goods.rect.x = 550
    next_goods.rect.y = 250
    characters.rect.x = -999
    characters.rect.y = -999
    wallpapers.rect.x = -999
    wallpapers.rect.y = -999

    # Встановлення дефолт скіна
    if df_skin:
        if st_skin == 1:
            select_ch.rect.x = -99999
            select_ch.rect.y = -99999
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        elif bought_dfskin == True:
            select_ch.rect.x = 275
            select_ch.rect.y = 550
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

        lst = [num_25, num_50, num_100, num_130]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        back_goods.rect.x = -99999
        back_goods.rect.y = -99999
        lst = [shop_kot1, shop_kot2, shop_minecube1, shop_minecube2, shop_pegion, shop_agentka, shop_mrcube1, shop_mrcube2]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        shop_cube1.rect.x = 275
        shop_cube1.rect.y = 50
        shop_cube2.rect.x = 275
        shop_cube2.rect.y = 300

    # Встановлення скіна з кицьками
    if cats:
        if st_skin == 2:
            num_25.rect.x = -9999
            num_25.rect.y = -9999
            select_ch2.rect.x = -99999
            select_ch2.rect.y = -99999
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        elif bought_cats == True:
            select_ch2.rect.x = 275
            select_ch2.rect.y = 550
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999
            num_25.rect.x = -9999
            num_25.rect.y = -9999
        else:
            selected_ch.rect.x = -999
            selected_ch.rect.y = -9999
            select_ch2.rect.x = -99999
            select_ch2.rect.y = -99999
            num_25.rect.x = 275
            num_25.rect.y = 550

        lst = [num_130, num_50, num_100]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        if n25:
            num_25.rect.x = 275
            num_25.rect.y = 550
        else:
            num_25.rect.x = -999
            num_25.rect.y = -999
        lst = [shop_cube1, shop_cube2, shop_minecube1, shop_minecube2, shop_pegion, shop_agentka, shop_mrcube1, shop_mrcube2]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        shop_kot1.rect.x = 275
        shop_kot1.rect.y = 50
        shop_kot2.rect.x = 275
        shop_kot2.rect.y = 300

    # Встановлення скіна за стилем майнкрафту
    if mincr:
        if st_skin == 3:
            num_50.rect.x = -9999
            num_50.rect.y = -9999
            select_ch3.rect.x = -99999
            select_ch3.rect.y = -99999
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        elif bought_mine == True:
            select_ch3.rect.x = 275
            select_ch3.rect.y = 550
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999
            num_50.rect.x = -9999
            num_50.rect.y = -9999
        else:
            selected_ch.rect.x = -999
            selected_ch.rect.y = -9999
            select_ch3.rect.x = -99999
            select_ch3.rect.y = -99999
            num_50.rect.x = 275
            num_50.rect.y = 550
        lst = [num_25, num_130, num_100]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        if n50:
            num_50.rect.x = 275
            num_50.rect.y = 550
        else:
            num_50.rect.x = -9999
            num_50.rect.y = -9999

        lst = [shop_cube1, shop_cube2, shop_kot1, shop_kot2, shop_pegion, shop_agentka, shop_mrcube1, shop_mrcube2]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        shop_minecube1.rect.x = 275
        shop_minecube1.rect.y = 50
        shop_minecube2.rect.x = 275
        shop_minecube2.rect.y = 300

    # Встановлення скінів від імені автора
    if our_sk:
        if st_skin == 4:
            num_100.rect.x = -9999
            num_100.rect.y = -9999
            select_ch4.rect.x = -99999
            select_ch4.rect.y = -99999
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        elif bought_our == True:
            select_ch4.rect.x = 275
            select_ch4.rect.y = 550
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999
            num_100.rect.x = -9999
            num_100.rect.y = -9999
        else:
            selected_ch.rect.x = -999
            selected_ch.rect.y = -9999
            select_ch4.rect.x = -99999
            select_ch4.rect.y = -99999
            num_100.rect.x = 275
            num_100.rect.y = 550

        lst = [num_25, num_50, num_130]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        if n100:
            num_100.rect.x = 275
            num_100.rect.y = 550
        else:
            num_100.rect.x = -9999
            num_100.rect.y = -9999
        lst = [shop_cube1, shop_cube2, shop_kot1, shop_kot2, shop_minecube1, shop_minecube2, shop_mrcube1, shop_mrcube2]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        shop_pegion.rect.x = 275
        shop_pegion.rect.y = 50
        shop_agentka.rect.x = 275
        shop_agentka.rect.y = 300

    # Встановлення скінів сенйьорів
    if mr:
        next_goods.rect.x = -9999
        next_goods.rect.y = -9999
        if st_skin == 5:
            num_130.rect.x = -9999
            num_130.rect.y = -9999
            select_ch5.rect.x = -99999
            select_ch5.rect.y = -99999
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        elif bought_mr == True:
            select_ch5.rect.x = 275
            select_ch5.rect.y = 550
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999
            num_130.rect.x = -9999
            num_130.rect.y = -9999
        else:
            selected_ch.rect.x = -999
            selected_ch.rect.y = -9999
            select_ch5.rect.x = -99999
            select_ch5.rect.y = -99999
            num_130.rect.x = 275
            num_130.rect.y = 550

        lst = [num_25, num_50, num_100]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        num_130.rect.x = 275
        num_130.rect.y = 550
        lst = [shop_cube1, shop_cube2, shop_kot1, shop_kot2, shop_minecube1, shop_minecube2, shop_pegion, shop_agentka]
        for i in lst:
            i.rect.x = -9999
            i.rect.y = -9999
        shop_mrcube1.rect.x = 275
        shop_mrcube1.rect.y = 50
        shop_mrcube2.rect.x = 275
        shop_mrcube2.rect.y = 300

def shop_menu():
    # Встановлення менюшки для магазину
    lst = [shop, ok, exit, start, home]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    mahazina.rect.x = 0
    mahazina.rect.y = 0
    characters.rect.x = 50
    characters.rect.y = 225
    wallpapers.rect.x = 400
    wallpapers.rect.y = 225
    back.rect.x = 0
    back.rect.y = 0

# Потрібні класи (для ініцалізування, обробки подій та зміни картинок)
class Area():
    def __init__(self, x=0, y=0, width=0, height=0, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = fon
        if color:
            self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
    def change_image(self, new_image_path):
        self.image = pygame.image.load(new_image_path)

class Text(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont("Verdana", fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

# Встановлення початквої позиції пулькам
hp1 = Area(0, 0, 100, 50, (29, 143, 39))
hp2 = Area(600, 0, 100, 50, (29, 143, 39))
height = -205
height1 = -250
height3 = -232
height4 = -302
coins_bg = Picture('coins_bg.png', 490, 30, 250, 100)
# Необхідні для роботи картинки/спрайти
stuck = Picture('stuck_of_coins.com.png', 490, 30, 50, 50)
next_goods = Picture('Right.png', 550, 225, 300, 300)
back_goods = Picture('Left.png', 0, 225, 300, 300)
characters = Picture('cubes_shop.png', 50, 225, 300, 300)
wallpapers = Picture('wallpaper_shop.png', 400, 225, 300, 300)
mahazina = Picture('mahazina.png', 0, 0, 750, 750)
select_ch = Picture('select.png', 275, 550, 250, 150)
select_ch2 = Picture('select.png', 275, 550, 250, 150)
select_ch3 = Picture('select.png', 275, 550, 250, 150)
select_ch4 = Picture('select.png', 275, 550, 250, 150)
select_ch5 = Picture('select.png', 275, 550, 250, 150)
selected_ch = Picture('selected.png', 275, 550, 250, 150)
num_25 = Picture('25.png', 275, 550, 250, 150)
num_50 = Picture('50.png', 275, 550, 250, 150)
num_100 = Picture('100.png', 275, 550, 250, 150)
num_130 = Picture('130.png', 275, 550, 250, 150)
home = Picture("home.png", 0, 0, 750, 750)
back = Picture('back.png', 0, 0, 100, 100)
start = Picture("Start_mw.png", 0, 0, 750, 750)
ok = Text(300, 560, 120, 64, (29, 71, 39))
coins_txt = Text(450, 50, 25, 10, (17, 134, 9))
exit = Text(312, 660, 100, 64, (232, 0, 0))
continue_game = Text(250, 600, 220, 50, (51, 204, 51))
game_over_text = Text(100, 600, 120, 50, (232, 0, 0))
game_over = Picture("Game_Over.png", 0, 0, 750, 750)
shop = Picture("shop.png", 550, 500, 150, 150)
shop_cube1 = Picture('shop_cube1.png', 275, 50, 200, 200)
shop_cube2 = Picture('shop_cube_2.png', 275, 300, 200, 200)
shop_kot1 = Picture('shop_kot_1.png', 950, 50, 200, 200)
shop_kot2 = Picture('shop_kot_2.png', 950, 300, 200, 200)
shop_minecube1 = Picture('shop_minecraft_block_1.png', 2850, 50, 200, 300)
shop_minecube2 = Picture('shop_minecraft_block_2.png', 2850, 300, 200, 200)
shop_pegion = Picture('Shop_Pegion.png', 3800, 50, 200, 200)
shop_agentka = Picture('Shop_agentka.png', 3800, 300, 200, 200)
shop_mrcube1 = Picture('Shop_Mr. cube1.png', 1900, 50, 200, 200)
shop_mrcube2 = Picture('Shop_Mr. cube2.png', 1900, 300, 200, 200)
cube = Picture('../Logika шкуль/Pygame/cube_1.png', 300, 500, 100, 100)
cube_s = Picture('cube_2.png', 50, 500, 100, 100)
bullet = Picture("bullet.png", R, 105, 50, 100)
bullet2 = Picture("bullet.png", R2, 105, 50, 100)
bullet3 = Picture("bullet.png", R3, 105, 50,  100)
bullet4 = Picture("bullet.png", R4, 105, 50, 100)
game_over_text_time = Text(400, 280, 80, 50, (29, 71, 39))
game_over_points = Text(400, 370, 80, 50, (29, 71, 39))
game_over_total = Text(400, 460, 80, 50, (29, 143, 39))
coins_txt_katka = Text(400, 510, 80, 50, (29, 71, 39))
coins_in_catka = 0

# Ще трішки флажків
df_skin = True
cats = False
mincr = False
our_sk = False
mr = False

n25 = True
n50 = True
n100 = True
n130 = True

select_sk_change1 = cube
select_sk_change2 = cube_s

seleckted_skin_1 = True
seleckted_skin_2 = False
seleckted_skin_3 = False
seleckted_skin_4 = False
seleckted_skin_5 = False

buy = False
coins = 130

finish_time = 0
points = 0
total = 0

st_skin = 1
removed_st_skin = 0

bull = False

bought_dfskin = True
bought_cats = False
bought_mine = False
bought_our = False
bought_mr = False

start_time = time.time()
o = True
con = True
u = False
st = True
ev = False
urb = True
menu = False
point_num = 0
num = 0
home_fl = True
shop_num = 1
cash = 0
num1 = True
num2 = False
num3 = False
num4 = False

num1_r = False
num2_r = False
num3_r = False
num4_r = False
while run:
    # Рисування самих спрайтів
    bil = True
    home.fill()
    mahazina.fill()
    back.fill()
    characters.fill()
    wallpapers.fill()
    shop.fill()
    shop_pegion.fill()
    shop_agentka.fill()
    shop_mrcube1.fill()
    shop_minecube2.fill()
    hp1.fill()
    hp2.fill()
    shop_cube1.fill()
    shop_cube2.fill()
    shop_minecube1.fill()
    shop_mrcube2.fill()
    shop_kot1.fill()
    shop_kot2.fill()
    coins_bg.fill()
    stuck.fill()
    next_goods.fill()
    back_goods.fill()
    select_ch.fill()
    select_ch2.fill()
    select_ch3.fill()
    select_ch4.fill()
    select_ch5.fill()
    selected_ch.fill()
    start.fill()
    cube.fill()
    cube_s.fill()
    bullet.fill()
    bullet2.fill()
    bullet3.fill()
    bullet4.fill()
    num_25.fill()
    num_50.fill()
    num_100.fill()
    num_130.fill()
    game_over.fill()
    # Глобалізація змінних.?
    def g():
        global finish_time
        global points
        global total

    g()
    if home_fl:
        home_title()
        home_fl = False
    coins_txt.set_text(f"{coins}", 36, (255, 255, 255))
    ok.set_text("Start", 36, (255, 255, 255))
    exit.set_text("Quit", 36, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Визначення чи користувач натиснув на картинку/спрайт
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            # Показати інструкцію якщо користувач нажав на картинку з ок і змінна нам == 0
            if ok.collidepoint(x, y) and num == 0:
                instruct()
                num = 1

            # Показати меню магазину якщо кор. натиснув на спрайт магазину
            elif shop.collidepoint(x, y):
                shop_menu()

            # Показати меню гри якщо кор. натиснув на кнопку "назад" в магазині
            elif back.collidepoint(x, y):
                home_title()

            # Вийти з гри якщо користувач тицьув на вихід з гри
            elif exit.collidepoint(x, y):
                pygame.quit()

            # Почати гру якщо кор. натиснув на спрайт "ок" та нам == 1
            elif ok.collidepoint(x, y) and num == 1:
                hearts = 6
                game()
                num = 0

            # Почати гру знову якщо кор. натиснув на спрайт грати знову
            elif continue_game.collidepoint(x, y):
                hearts = 6
                game()
                num = 0

            # Вийти в меню якщо кор. нажав на "меню" в геймовері)
            elif game_over_text.collidepoint(x, y):
                home_title()

            elif num_25.collidepoint(x, y) and coins >= 25:
                n25 = False
                coins = coins - 25
                num_25.rect.x = -99999
                num_25.rect.y = -99999
                select_ch2.rect.x = 275
                select_ch2.rect.y = 550
                bought_cats = True
                bought_mr = False
                bought_mine = False
                bought_our = False
                bought_dfskin = False
                print(coins)

            elif select_ch2.collidepoint(x, y):
                st_skin = 2
                cats = True
                characters_m()
                select_ch2.rect.x = -99999
                select_ch2.rect.y = -99999
                selected_ch.rect.x = 275
                selected_ch.rect.y = 550
                cats = False
                select_sk_change1.change_image('kot_1.png')
                select_sk_change2.change_image('kot_2.png')

            elif num_50.collidepoint(x, y) and coins >= 50:
                n50 = False
                coins = coins - 50
                num_50.rect.x = -99999
                num_50.rect.y = -99999
                select_ch3.rect.x = 275
                select_ch3.rect.y = 550
                bought_mine = True
                bought_mr = False
                bought_cats = False
                bought_our = False
                bought_dfskin = False
                print(coins)

            elif select_ch3.collidepoint(x, y):
                st_skin = 3
                mincr = True
                characters_m()
                select_ch3.rect.x = -99999
                select_ch3.rect.y = -99999
                selected_ch.rect.x = 275
                selected_ch.rect.y = 550
                mincr = False
                select_sk_change1.change_image('minecraft_block_1.png')
                select_sk_change2.change_image('minecraft_block_2.png')

            elif num_100.collidepoint(x, y) and coins >= 100:
                n100 = False
                coins = coins - 100
                num_100.rect.x = -99999
                num_100.rect.y = -99999
                select_ch4.rect.x = 275
                select_ch4.rect.y = 550
                bought_our = True
                bought_mr = False
                bought_mine = False
                bought_cats = False
                bought_dfskin = False
                print(coins)

            elif select_ch4.collidepoint(x, y):
                st_skin = 4
                our_sk = True
                characters_m()
                select_ch4.rect.x = -99999
                select_ch4.rect.y = -99999
                selected_ch.rect.x = 275
                selected_ch.rect.y = 550
                our_sk = False
                select_sk_change1.change_image('Pegion.png')
                select_sk_change2.change_image('agentka.png')


            elif num_130.collidepoint(x, y) and coins >= 130:
                n130 = False
                coins = coins - 130
                num_130.rect.x = -99999
                num_130.rect.y = -99999
                select_ch5.rect.x = 275
                select_ch5.rect.y = 550
                bought_mr = True
                bought_cats = False
                bought_mine = False
                bought_our = False
                bought_dfskin = False
                print(coins)

            elif select_ch5.collidepoint(x, y):
                st_skin = 5
                mr = True
                characters_m()
                select_ch5.rect.x = -99999
                select_ch5.rect.y = -99999
                selected_ch.rect.x = 275
                selected_ch.rect.y = 550
                mr = False
                next_goods.rect.x = -9999
                next_goods.rect.y = -9999
                select_sk_change1.change_image('Mr. cube1.png')
                select_sk_change2.change_image('Mr. cube2.png')






            elif select_ch.collidepoint(x, y):
                st_skin = 1
                df_skin = True
                characters_m()
                select_ch.rect.x = -9999
                select_ch.rect.y = -9999
                selected_ch.rect.x = 275
                selected_ch.rect.y = 550
                df_skin = False
                select_sk_change1.change_image('cube_1.png')
                select_sk_change2.change_image('cube_2.png')


            elif characters.collidepoint(x, y):
                if st_skin == 1:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550
                    seleckted_skin_1 = True
                    mincr = False
                    cats = False
                    our_sk = False
                    mr = False
                    df_skin = True
                    next_goods.rect.x = 550
                    next_goods.rect.y = 225
                    characters_m()
                    num1_r = False
                    num1 = True
                elif st_skin == 2:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550
                    seleckted_skin_2 = True
                    df_skin = False
                    mincr = False
                    our_sk = False
                    mr = False
                    cats = True
                    back_goods.rect.x = 0
                    back_goods.rect.y = 225
                    next_goods.rect.x = 550
                    next_goods.rect.y = 225
                    characters_m()
                    num1_r = True
                    num1 = False
                    num2 = True
                elif st_skin == 3:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550
                    seleckted_skin_3 = True
                    our_sk = False
                    mr = False
                    df_skin = False
                    cats = False
                    mincr = True
                    back_goods.rect.x = 0
                    back_goods.rect.y = 225
                    next_goods.rect.x = 550
                    next_goods.rect.y = 225
                    characters_m()
                    num2_r = True
                    num1_r = False
                    num2 = False
                    num3 = True
                elif st_skin == 4:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550
                    seleckted_skin_4 = True
                    mr = False
                    cats = False
                    df_skin = False
                    mincr = False
                    our_sk = True
                    back_goods.rect.x = 0
                    back_goods.rect.y = 225
                    next_goods.rect.x = 550
                    next_goods.rect.y = 225
                    characters_m()
                    num3_r = True
                    num2_r = False
                    num3 = False
                    num4 = True
                elif st_skin == 5:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550
                    seleckted_skin_5 = True
                    cats = False
                    mincr = False
                    df_skin = False
                    our_sk = False
                    mr = True
                    next_goods.rect.x = -9999
                    next_goods.rect.y = -9999
                    back_goods.rect.x = 0
                    back_goods.rect.y = 225
                    characters_m()
                    num4_r = True

            # Показати наступний скін з котами якщо нам1 == Тру
            elif next_goods.collidepoint(x, y) and num1 == True:
                df_skin = False
                cats = True
                characters_m()
                back_goods.rect.x = 0
                back_goods.rect.y = 225
                num1_r = True
                num1 = False
                num2 = True
                if st_skin == 1 or st_skin == 3 or st_skin == 4 or st_skin == 5:
                    if bought_cats == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch2.rect.x = 275
                        select_ch2.rect.y = 550
                    elif bought_cats == False:
                        num_25.rect.x = 275
                        num_25.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 2:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550

            # Показати наступний скін з майнкрафтом якщо нам2 == Тру
            elif next_goods.collidepoint(x, y) and num2 == True:
                cats = False
                mincr = True
                characters_m()
                num2_r = True
                num1_r = False
                num2 = False
                num3 = True
                if st_skin == 2 or st_skin == 1 or st_skin == 4 or st_skin == 5:
                    if bought_mine == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch3.rect.x = 275
                        select_ch3.rect.y = 550
                    elif bought_mine == False:
                        num_50.rect.x = 275
                        num_50.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 3:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550

            # Показати наступний скін від автора якщо нам3 == Тру
            elif next_goods.collidepoint(x, y) and num3 == True:
                mincr = False
                our_sk = True
                characters_m()
                num3_r = True
                num2_r = False
                num3 = False
                num4 = True
                if st_skin == 2 or st_skin == 3 or st_skin == 1 or st_skin == 5:
                    if bought_our == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch4.rect.x = 275
                        select_ch4.rect.y = 550
                    elif bought_our == False:
                        num_100.rect.x = 275
                        num_100.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 4:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550



            # Показти наступний скін з містерами якщо нам4 == Тру
            elif next_goods.collidepoint(x, y) and num4 == True:
                our_sk = False
                mr = True
                characters_m()
                next_goods.rect.x = -9999
                next_goods.rect.y = -9999
                num4 = False
                num4_r = True
                if st_skin == 2 or st_skin == 3 or st_skin == 4 or st_skin == 1:
                    if bought_mr == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch5.rect.x = 275
                        select_ch5.rect.y = 550
                    elif bought_mr == False:
                        num_130.rect.x = 275
                        num_130.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 5:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550








            # Показати попередній скін від автора
            elif back_goods.collidepoint(x, y) and num4_r == True:
                next_goods.rect.x = 550
                next_goods.rect.y = 225
                mr = False
                our_sk = True
                characters_m()
                num4 = True
                num4_r = False
                num3_r = True
                if st_skin == 2 or st_skin == 3 or st_skin == 1 or st_skin == 5:
                    if bought_our == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch4.rect.x = 275
                        select_ch4.rect.y = 550
                    elif bought_our == False:
                        num_100.rect.x = 275
                        num_100.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 4:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550


            elif back_goods.collidepoint(x, y) and num3_r == True:
                our_sk = False
                mincr = True
                characters_m()
                num3 = True
                num3_r = False
                num2_r = True
                if st_skin == 2 or st_skin == 1 or st_skin == 4 or st_skin == 5:
                    if bought_mine == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch3.rect.x = 275
                        select_ch3.rect.y = 550
                    elif bought_mine == False:
                        num_50.rect.x = 275
                        num_50.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 3:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550


            elif back_goods.collidepoint(x, y) and num2_r == True:
                mincr = False
                cats = True
                characters_m()
                num2 = True
                num1_r = True
                num2_r = False
                if st_skin == 1 or st_skin == 3 or st_skin == 4 or st_skin == 5:
                    if bought_cats == True:
                        selected_ch.rect.x = -9999
                        selected_ch.rect.y = -9999
                        select_ch2.rect.x = 275
                        select_ch2.rect.y = 550
                    elif bought_cats == False:
                        num_25.rect.x = 275
                        num_25.rect.y = 550
                        selected_ch.rect.x = -99999
                        selected_ch.rect.y = -99999
                        lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5]
                        for i in lst:
                            i.rect.x = -9999
                            i.rect.y = -9999
                elif st_skin == 2:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550

            elif back_goods.collidepoint(x, y) and num1_r == True:
                cats = False
                df_skin = True
                characters_m()
                num1_r = False
                num1 = True

                if st_skin == 2 or st_skin == 3 or st_skin == 4 or st_skin == 5:
                    selected_ch.rect.x = -9999
                    selected_ch.rect.y = -9999
                    select_ch.rect.x = 275
                    select_ch.rect.y = 550
                elif st_skin == 1:
                    selected_ch.rect.x = 275
                    selected_ch.rect.y = 550






        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                RIGHT = True
            if event.key == pygame.K_LEFT:
                LEFT = True
            if event.key == pygame.K_d:
                RIGHT_S = True
            if event.key == pygame.K_a:
                LEFT_S = True
            if event.key == pygame.K_UP:
                JUMP = True
            if event.key == pygame.K_w:
                JUMP_S = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                RIGHT = False
            if event.key == pygame.K_LEFT:
                LEFT = False
            if event.key == pygame.K_d:
                RIGHT_S = False
            if event.key == pygame.K_a:
                LEFT_S = False
    R = randint(10, 740)
    R2 = randint(10, 740)
    R3 = randint(10, 740)
    R4 = randint(10, 740)
    if bullet.rect.colliderect(bullet2.rect) or bullet2.rect.colliderect(bullet3.rect) or bullet3.rect.colliderect(bullet4.rect) and bil == True:
        bil = False
        bullet.rect.x = R
        bullet.rect.y = height
        bullet2.rect.x = R2
        bullet2.rect.y = height1
        bullet3.rect.x = R3
        bullet3.rect.y = height3
        bullet4.rect.x = R4
        bullet4.rect.y = height4
    if bull:
        for i in range(1, 5):
            bullet.rect.y += 2
    if bullet.rect.y >= 750:
        point_num += 2
        bullet.rect.x = R
        bullet.rect.y = height
    if bullet2.rect.y >= 750:
        point_num += 2
        bullet2.rect.x = R2
        bullet2.rect.y = height1
    if bullet3.rect.y >= 750:
        point_num += 2
        bullet3.rect.x = R3
        bullet3.rect.y = height3
    if bullet4.rect.y >= 750:
        point_num += 2
        bullet4.rect.x = R4
        bullet4.rect.y = height4
    if bull:
        for i in range(1, 5):
            bullet2.rect.y += 2
    if bull:
        for i in range(1, 5):
            bullet3.rect.y += 2
    if bull:
        for i in range(1, 5):
            bullet4.rect.y += 2
    if cube.rect.x > 645:
        RIGHT = False
    if cube.rect.x <= 0:
        LEFT = False
    if cube_s.rect.x > 645:
        RIGHT_S = False
    if cube_s.rect.x <= 0:
        LEFT_S = False
    if RIGHT and cube.rect.x != 645:
        cube.rect.x += bx1
        bx1 = 10
    if LEFT and cube.rect.x != 5:
        cube.rect.x -= bx2
        bx2 = 10
    if RIGHT_S and cube_s.rect.x != 645:
        cube_s.rect.x += bx1
        bx1 = 10
    if LEFT_S and cube_s.rect.x != 5:
        cube_s.rect.x -= bx2
        bx2 = 10
    if JUMP:
        if jumpCount1 >= -12:
            if jumpCount1 < 0:
                cube.rect.y += (jumpCount1 ** 2) / 2
            else:
                cube.rect.y -= (jumpCount1 ** 2) / 2
            jumpCount1 -= 2
        else:
            JUMP = False
            jumpCount1 = 12
    if JUMP_S:
        if jumpCount2 >= -12:
            if jumpCount2 < 0:
                cube_s.rect.y += (jumpCount2 ** 2) / 2
            else:
                cube_s.rect.y -= (jumpCount2 ** 2) / 2
            jumpCount2 -= 2
        else:
            JUMP_S = False
            jumpCount2 = 12
    if cube.rect.colliderect(bullet.rect):
        bullet.rect.x = R
        bullet.rect.y = height
        hp1.rect.width -= 10

    if cube.rect.colliderect(bullet2.rect):
        bullet2.rect.x = R2
        bullet2.rect.y = height1
        hp1.rect.width -= 10

    if cube.rect.colliderect(bullet3.rect):
        bullet3.rect.x = R3
        bullet3.rect.y = height3
        hp1.rect.width-=10

    if cube.rect.colliderect(bullet4.rect):
        bullet4.rect.x = R4
        bullet4.rect.y = height4
        hp1.rect.width -= 10





    if cube_s.colliderect(bullet.rect):
        bullet.rect.x = R
        bullet.rect.y = height
        hp2.rect.width -= 10

    if cube_s.colliderect(bullet2.rect):
        bullet2.rect.x = R2
        bullet2.rect.y = height1
        hp2.rect.width -= 10

    if cube_s.colliderect(bullet3.rect):
        bullet3.rect.x = R3
        bullet3.rect.y = height3
        hp2.rect.width -= 10

    if cube_s.rect.colliderect(bullet4.rect):
        bullet4.rect.x = R4
        bullet4.rect.y = height4
        hp2.rect.width -= 10




    bullet.draw()
    bullet2.draw()
    bullet3.draw()
    bullet4.draw()
    cube.draw()
    cube_s.draw()
    if hp1.rect.width <= 0 and hp2.rect.width <= 0:
        game_over_title()
        game_over.draw()
        game_over_text.set_text("В меню", 21, (0, 0, 0))
        game_over_text.draw(20, 10)
        continue_game.set_text("Почати спочатку", 21, (0, 0, 0))
        continue_game.draw(20, 10)
        finish_time = int(time.time() - start_time)
        points = point_num
        points = str(points)
        finish_time = str(finish_time)
        total = int(finish_time) + int(points)
        total = str(total)

        game_over_text_time.set_text(finish_time, 21, (255, 255, 255))
        game_over_text_time.draw(20, 10)
        game_over_points.set_text(points, 21, (255, 255, 255))
        game_over_points.draw(20, 10)
        coins_txt_katka.set_text(str(coins_in_catka), 21, (255, 255, 255))
        coins_txt_katka.draw(20, 10)
        game_over_total.set_text(total, 21, (255, 255, 255))
        game_over_total.draw(20, 10)
    start.draw()
    home.draw()
    mahazina.draw()
    back.draw()
    shop.draw()
    characters.draw()
    wallpapers.draw()
    shop_mrcube1.draw()
    shop_minecube2.draw()
    shop_pegion.draw()
    shop_agentka.draw()
    shop_cube1.draw()
    shop_cube2.draw()
    shop_minecube1.draw()
    shop_mrcube2.draw()
    shop_kot1.draw()
    shop_kot2.draw()
    next_goods.draw()
    back_goods.draw()
    coins_bg.draw()
    coins_txt.draw(15, 10)
    stuck.draw()
    num_25.draw()
    num_50.draw()
    num_100.draw()
    num_130.draw()
    select_ch.draw()
    select_ch2.draw()
    select_ch3.draw()
    select_ch4.draw()
    select_ch5.draw()
    selected_ch.draw()
    ok.draw(15, 10)
    exit.draw(15, 10)


    pygame.display.flip()
    clock.tick(40)
