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
    lst = [select_ch, select_ch2, select_ch3, select_ch4, select_ch5, shop_agentka, shop_pegion, shop_cube1, shop_cube2, shop_kot1, shop_kot2, shop_minecube1, shop_minecube2, shop_pegion, shop_agentka, shop_mrcube1, shop_mrcube2, selected_ch, selected_ch, num_25, num_50, num_100, num_130, characters, wallpapers, next_goods, back_goods, back, mahazina, heart, start, continue_game, game_over, game_over_text, game_over_points, game_over_total, game_over_text_time, number_1, number_2, number_3, number_4, number_5, number_6, bullet, bullet2, bullet3, bullet4, cube, cube_s]
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
    lst = [game_over, game_over_text, game_over_total, game_over_points, continue_game, exit, mahazina, ok, start]
    lst0 = [number_1, number_2, number_3, number_4, number_5, number_6]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    for n in lst0:
        n.rect.x = 0
        n.rect.y = 0
    heart.rect.x = 50
    heart.rect.y = 0
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
def game_over_title():
    global bull
    bull = False
    # Встановлення вікна програшу
    lst = [heart, characters, wallpapers, mahazina, start, number_1, number_2, number_3, number_4, number_5, number_6, bullet, bullet2, bullet3, bullet4, cube, cube_s, exit]
    for i in lst:
        i.rect.x = -9999
        i.rect.y = -9999
    continue_game.rect.x = 200
    continue_game.rect.y = 650
    game_over_text.rect.x = 100
    game_over_text.rect.y = 600
    game_over.rect.x = 0
    game_over.rect.y = -1
    game_over_text_time.rect.x = 400
    game_over_text_time.rect.y = 280
    game_over_total.rect.x = 400
    game_over_total.rect.y = 460
    game_over_points.rect.x = 400
    game_over_points.rect.y = 370
    continue_game.rect.x = 250
    continue_game.rect.y = 600
def characters_m():
    # Відображення вікна з персонажами в магазині
    next_goods.rect.x = 550
    next_goods.rect.y = 250
    characters.rect.x = -999
    characters.rect.y = -999
    wallpapers.rect.x = -999
    wallpapers.rect.y = -999

    # Встановлення дефолт скіна
    if df_skin:
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
        if seleckted_skin_1:
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        else:
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

    # Встановлення скіна з кицьками
    if cats:
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
        if seleckted_skin_2:
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        else:
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

    # Встановлення скіна за стилем майнкрафту
    if mincr:
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
        if seleckted_skin_3:
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        else:
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

    # Встановлення скінів від імені автора
    if our_sk:
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
        if seleckted_skin_4:
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        else:
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

    # Встановлення скінів сенйьорів
    if mr:
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
        if seleckted_skin_5:
            selected_ch.rect.x = 275
            selected_ch.rect.y = 550
        else:
            selected_ch.rect.x = -9999
            selected_ch.rect.y = -9999

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
height = -205
height1 = -250
height3 = -232
height4 = -302
hearts = 6

# Необхідні для роботи картинки/спрайти
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
exit = Text(312, 660, 100, 64, (232, 0, 0))
continue_game = Text(250, 600, 220, 50, (51, 204, 51))
game_over_text = Text(100, 600, 120, 50, (232, 0, 0))
game_over = Picture("Game_Over.png", 0, 0, 750, 750)
shop = Picture("shop.png", 550, 500, 150, 150)
heart = Picture("heart.png", 50, 0, 50, 50)
number_6 = Picture("6.6.png", 0, 0, 50, 40)
number_5 = Picture("5.5.png", 0, 0, 50, 40)
number_4 = Picture("4.4.png", 0, 0, 50, 40)
number_3 = Picture("3.3.png", 0, 0, 50, 40)
number_2 = Picture("2.2.png", 0, 0, 50, 40)
number_1 = Picture("1.1.png", 0, 0, 50, 40)
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
game_over_total = Text(400, 460, 80, 50, (29, 71, 39))

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
    shop_cube1.fill()
    shop_cube2.fill()
    shop_minecube1.fill()
    shop_mrcube2.fill()
    shop_kot1.fill()
    shop_kot2.fill()
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
    number_6.fill()
    number_5.fill()
    number_4.fill()
    number_3.fill()
    number_2.fill()
    number_1.fill()
    heart.fill()
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
    ok.set_text("Start", 36, (255, 255, 255))
    exit.set_text("Quit", 36, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Визначення чи користувач натиснув на картинку/спрайт
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            if ok.collidepoint(x, y) and num == 0:
                instruct()
                num = 1

            # Показати меню магазину якщо кор. натиснув на спрайт магазину
            if shop.collidepoint(x, y):
                shop_menu()

            # Показати меню гри якщо кор. натиснув на кнопку "назад" в магазині
            if back.collidepoint(x, y):
                home_title()

            # Вийти з гри якщо користувач тицьув на вихід з гри
            if exit.collidepoint(x, y):
                pygame.quit()

            # Почати гру якщо кор. натиснув на спрайт "ок" та нам == 1
            if ok.collidepoint(x, y) and num == 1:
                hearts = 6
                game()
                num = 0

            # Почати гру знову якщо кор. натиснув на спрайт грати знову
            if continue_game.collidepoint(x, y):
                hearts = 6
                game()
                num = 0

            # Вийти в меню якщо кор. нажав на "меню" в геймовері)
            if game_over_text.collidepoint(x, y):
                home_title()
        if event.type == pygame.QUIT:
            run = False
            # Показати інструкцію якщо користувач нажав на картинку з ок і змінна нам == 0
            if ok.collidepoint(x, y) and num == 0:
                instruct()
                num = 1

            # Показати меню магазину якщо кор. натиснув на спрайт магазину
            if shop.collidepoint(x, y):
                shop_menu()

            # Показати меню гри якщо кор. натиснув на кнопку "назад" в магазині
            if back.collidepoint(x, y):
                home_title()

            # Вийти з гри якщо користувач тицьув на вихід з гри
            if exit.collidepoint(x, y):
                pygame.quit()

            # Почати гру якщо кор. натиснув на спрайт "ок" та нам == 1
            if ok.collidepoint(x, y) and num == 1:
                hearts = 6
                game()
                num = 0

            # Почати гру знову якщо кор. натиснув на спрайт грати знову
            if continue_game.collidepoint(x, y):
                hearts = 6
                game()
                num = 0

            # Вийти в меню якщо кор. нажав на "меню" в геймовері)
            if game_over_text.collidepoint(x, y):
                home_title()


            elif characters.collidepoint(x, y):
                if st_skin == 1:
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
                elif not bought_cats:
                    select_ch2.rect.x = -99999
                    select_ch2.rect.y = -99999
                    selected_ch.rect.x = -9999
                    selected_ch.rect.y = -9999
                    num_25.rect.x = 275
                    num_25.rect.y = 550
                elif not bought_mine:
                    select_ch3.rect.x = -99999
                    select_ch3.rect.y = -99999
                    selected_ch.rect.x = -9999
                    selected_ch.rect.y = -9999
                    num_50.rect.x = 275
                    num_50.rect.y = 550
                elif not bought_our:
                    select_ch4.rect.x = -99999
                    select_ch4.rect.y = -99999
                    selected_ch.rect.x = -9999
                    selected_ch.rect.y = -9999
                    num_100.rect.x = 275
                    num_100.rect.y = 550
                elif not bought_mr:
                    select_ch5.rect.x = -99999
                    select_ch5.rect.y = -99999
                    selected_ch.rect.x = -9999
                    selected_ch.rect.y = -9999
                    num_130.rect.x = 275
                    num_130.rect.y = 550


            # Показати наступний скін з котами якщо нам1 == Тру
            if next_goods.collidepoint(x, y) and num1 == True:
                df_skin = False
                cats = True
                characters_m()
                back_goods.rect.x = 0
                back_goods.rect.y = 225
                num1_r = True
                num1 = False
                num2 = True

            # Показати наступний скін з майнкрафтом якщо нам2 == Тру
            elif next_goods.collidepoint(x, y) and num2 == True:
                cats = False
                mincr = True
                characters_m()
                num2_r = True
                num1_r = False
                num2 = False
                num3 = True

            # Показати наступний скін від автора якщо нам3 == Тру
            elif next_goods.collidepoint(x, y) and num3 == True:
                mincr = False
                our_sk = True
                characters_m()
                num3_r = True
                num2_r = False
                num3 = False
                num4 = True


            # Показти наступний скін з містерами якщо нам4 == Тру
            elif next_goods.collidepoint(x, y) and num4 == True:
                our_sk = False
                mr = True
                characters_m()
                next_goods.rect.x = -9999
                next_goods.rect.y = -9999
                num4_r = True


            # Показати попередній скін від автора
            if back_goods.collidepoint(x, y) and num4_r == True:
                next_goods.rect.x = 550
                next_goods.rect.y = 225
                our_sk = True
                characters_m()
                num4 = True
                num4_r = False
                num3_r = True
            elif back_goods.collidepoint(x, y) and num3_r == True:
                our_sk = False
                mincr = True
                characters_m()
                num3 = True
                num3_r = False
                num2_r = True
            elif back_goods.collidepoint(x, y) and num2_r == True:
                mincr = False
                cats = True
                characters_m()
                num2 = True
                num1_r = True
                num2_r = False
            elif back_goods.collidepoint(x, y) and num1_r == True:
                cats = False
                df_skin = True
                characters_m()
                num1_r = False

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
    heart.draw()
    ok.draw(15, 10)
    exit.draw(15, 10)
    pygame.display.update()
    clock.tick(40)