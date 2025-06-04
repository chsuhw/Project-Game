import pygame
import time
import sys
import json
# Инициализация Pygame и Mixer
pygame.init()
pygame.mixer.init()
# Создание окна
screen = pygame.display.set_mode((1920, 1080))
# Шрифты для работы с текстом
font = pygame.font.Font(None, 80)
font1 = pygame.font.Font(None, 60)
lvl, elapsed_time, score, isWin, collected, isCollected, player_x, player_y, isNew, ela_time = 0, 0, 0, 0, 0, [0, 0, 0], 0, 0, 1, 0
def main_menu():
    # Расположение кнопок в пространстве
    button1_x, button1_y, button1_w, button1_h = 660, 450, 500, 120
    button2_x, button2_y, button2_w, button2_h = 660, 600, 500, 120
    button3_x, button3_y, button3_w, button3_h = 660, 750, 500, 120
    button4_x, button4_y, button4_w, button4_h = 660, 900, 500, 120
    global font, font1, lvl, score, collected, isCollected, player_x, player_y, isNew, ela_time
    pygame.mixer.music.load("music/main.mp3")
    pygame.mixer.music.play(-1, 0)
    pygame.mixer.music.set_volume(0.2)
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Действия при клике на различные кнопки
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button1_x <= x <= button1_x + button1_w and button1_y <= y <= button1_y + button1_h:
                    lvl, score, collected, isCollected, player_x, player_y, isNew, ela_time = 1, 0, 0, [0, 0, 0], 0, 0, 1, 0
                    play()
                if button2_x <= x <= button2_x + button2_w and button2_y <= y <= button2_y + button2_h:
                    # if lvl > 7: statistics()
                    # with open("userdata.txt", "r") as file: lvl, score, collected, isCollected, player_x, player_y, ela_time = json.load(file)
                    # isNew = 0
                    # play()
                    select_lvl()
                if button3_x <= x <= button3_x + button3_w and button3_y <= y <= button3_y + button3_h:
                    statistics()
                if button4_x <= x <= button4_x + button4_w and button4_y <= y <= button4_y + button4_h:
                    pygame.quit()
                    sys.exit()
        # Работа с фоном и текстом
        pygame.display.set_caption("Лабиринт: Главное меню")
        background = pygame.image.load("pic/back.png")
        background = pygame.transform.scale(background, (1920, 1080))
        # Вывод на экран пользователя
        screen.blit(background, (0, 0))
        screen.blit(font.render("Новая игра", True, (255, 255, 255)), (750, 485))
        screen.blit(font.render("Продолжить", True, (255, 255, 255)), (730, 635))
        screen.blit(font.render("Статистика", True, (255, 255, 255)), (755, 785))
        screen.blit(font.render("Выход из игры", True, (255, 255, 255)), (700, 935))
        pygame.display.update()
def win_lose():
    global lvl, score, elapsed_time, isWin, font, font1, collected, isCollected, player_x, player_y, isNew, ela_time
    if isWin == 0:
        pygame.mixer.music.load("music/defeat.mp3")
        pygame.mixer.music.play(0, 0)
        pygame.mixer.music.set_volume(0.2)
    # Расположение кнопок в пространстве
    button1_x, button1_y, button1_w, button1_h = 770, 500, 365, 40
    button2_x, button2_y, button2_w, button2_h = 800, 600, 300, 40
    button3_x, button3_y, button3_w, button3_h = 720, 700, 465, 40
    isRunning = True
    while isRunning:
        # Шрифт для текста
        gfont = pygame.font.Font(None, 120)
        if isWin == 0:
            lvlCaption, backImage, tMessage = "Лабиринт: ПОРАЖЕНИЕ!", "pic/lose.png", "ПОРАЖЕНИЕ!"
            color = (220, 48, 48)
            text_pos = (700, 40)
        if isWin == 1:
            lvlCaption, backImage, tMessage = "Лабиринт: ПОБЕДА!", "pic/win.png", "ПОБЕДА!"
            color = (115, 220, 48)
            text_pos = (760, 40)
        # Работа с фоном и текстом
        pygame.display.set_caption(lvlCaption)
        background = pygame.image.load(backImage)
        background = pygame.transform.scale(background, (1920, 1080))
        # Вывод на экран пользователя
        screen.blit(background, (0, 0))
        if isWin == 1:
            # Расчёт статистики пройденного уровня
            minutes = elapsed_time // 60
            seconds = elapsed_time - minutes * 60
            if seconds < 10:
                screen.blit(font.render(f"Время: {minutes}:0{seconds}", True, (255, 255, 255)), (793, 300))
            else:
                screen.blit(font.render(f"Время: {minutes}:{seconds}", True, (255, 255, 255)), (793, 300))
            screen.blit(font.render(f"Счёт: {score}", True, (255, 255, 255)), (825, 400))
        screen.blit(gfont.render(tMessage, True, color), text_pos)
        screen.blit(font1.render("Продолжить игру", True, (255, 255, 255)), (770, 500))
        screen.blit(font1.render("Пройти заново", True, (255, 255, 255)), (800, 600))
        screen.blit(font1.render("Выйти в главное меню", True, (255, 255, 255)), (720, 700))
        pygame.display.update()
        # Выход в главное меню или продолжение игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                isRunning = False
                remaining_time, elapsed_time, score, collected, isCollected, player_x, player_y, isNew, ela_time = 0, 0, 0, 0, [0, 0, 0], 0, 0, 1, 0
                with open("userdata.txt", "w") as file: json.dump([lvl, score, collected, isCollected, player_x, player_y, ela_time], file)
                pygame.mixer.music.pause()
                if button1_x <= x <= button1_x + button1_w and button1_y <= y <= button1_y + button1_h:
                    if lvl > 7: statistics()
                    isWin = 0
                    play()
                if button2_x <= x <= button2_x + button2_w and button2_y <= y <= button2_y + button2_h:
                    if isWin == 1:
                        lvl -= 1
                        isWin = 0
                    play()
                if button3_x <= x <= button3_x + button3_w and button3_y <= y <= button3_y + button3_h: main_menu()
def play():
    global screen, lvl, elapsed_time, score, isWin, font, collected, isCollected, player_x, player_y, isNew, ela_time
    if lvl == 0:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 60, 60, 6, 1540, 960, 60, 310, 1200, 120, 30, 30
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/1.mp3", "Уровень 0", "Лабиринт: Уровень 0", "pic/lvl1.png", "pic/model.png", "pic/object.png"
        color = (255, 255, 255)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 60, 960
        # генерация конструкции уровня (карта мира)
        obstacles = [
            pygame.Rect(0, 900, 1760, 40), pygame.Rect(1880, 200, 40, 840), pygame.Rect(1880, 0, 40, 100), pygame.Rect(0, 0, 40, 1040), pygame.Rect(0, 1040, 1920, 40), pygame.Rect(160, 760, 1920, 40),
            pygame.Rect(0, 620, 1760, 40), pygame.Rect(160, 480, 1920, 40), pygame.Rect(0, 340, 1760, 40), pygame.Rect(160, 200, 1920, 40), pygame.Rect(0, 60, 1920, 40)
        ]
    if lvl == 1:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 60, 30, 6, 1540, 960, 60, 320, 1200, 120, 50, 50
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl1.mp3", "Уровень 1", "Лабиринт: Уровень 1", "pic/lvl1.png", "pic/model1.png", "pic/object1.png"
        color = (220, 182, 208)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 70, 130
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(1880, 0, 40, 920), pygame.Rect(0, 0, 40, 1040), pygame.Rect(160, 220, 40, 160), pygame.Rect(440, 100, 40, 280), pygame.Rect(320, 400, 40, 180), pygame.Rect(600, 400, 40, 160),
            pygame.Rect(480, 540, 40, 160), pygame.Rect(620, 740, 40, 320), pygame.Rect(760, 220, 40, 160), pygame.Rect(760, 580, 40, 160), pygame.Rect(920, 380, 40, 200), pygame.Rect(1040, 540, 40, 160),
            pygame.Rect(920, 80, 40, 180), pygame.Rect(1080, 240, 40, 180), pygame.Rect(1240, 240, 40, 680), pygame.Rect(1400, 400, 40, 700), pygame.Rect(1560, 560, 40, 320), pygame.Rect(1700, 400, 40, 360),
            # Строки
            pygame.Rect(1440, 400, 300, 40), pygame.Rect(1280, 700, 160, 40), pygame.Rect(1560, 880, 320, 40), pygame.Rect(1560, 240, 320, 40), pygame.Rect(1080, 240, 360, 40), pygame.Rect(760, 880, 480, 40),
            pygame.Rect(920, 540, 320, 40), pygame.Rect(760, 700, 320, 40), pygame.Rect(760, 380, 160, 40), pygame.Rect(640, 220, 160, 40), pygame.Rect(180, 880, 440, 40), pygame.Rect(180, 700, 340, 40),
            pygame.Rect(480, 540, 160, 40), pygame.Rect(40, 540, 140, 40), pygame.Rect(160, 380, 480, 40), pygame.Rect(160, 220, 160, 40), pygame.Rect(0, 1040, 1920, 40), pygame.Rect(0, 60, 1920, 40)
        ]
    if lvl == 2:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 60, 60, 6, 220, 420, 520, 920, 1490, 720, 40, 40
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl2.mp3", "Уровень 2", "Лабиринт: Уровень 2", "pic/lvl2.png", "pic/model2.png", "pic/object2.png"
        color = (0, 255, 150)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 60, 100
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(0, 60, 20, 1020), pygame.Rect(1900, 60, 20, 920), pygame.Rect(480, 160, 20, 220), pygame.Rect(360, 360, 20, 200), pygame.Rect(600, 60, 20, 400), pygame.Rect(720, 160, 20, 200),
            pygame.Rect(840, 60, 20, 200), pygame.Rect(1340, 160, 20, 320), pygame.Rect(1540, 160, 20, 100), pygame.Rect(1780, 160, 20, 100), pygame.Rect(960, 360, 20, 300), pygame.Rect(840, 460, 20, 500),
            pygame.Rect(120, 260, 20, 200), pygame.Rect(480, 560, 20, 100), pygame.Rect(480, 760, 20, 200), pygame.Rect(740, 660, 20, 220), pygame.Rect(620, 760, 20, 200), pygame.Rect(1250, 960, 20, 100),
            pygame.Rect(1420, 660, 20, 300), pygame.Rect(1780, 660, 20, 200), pygame.Rect(1660, 760, 20, 200), pygame.Rect(1540, 660, 20, 200),
            # Строки
            pygame.Rect(720, 360, 640, 20), pygame.Rect(1460, 260, 340, 20), pygame.Rect(840, 260, 400, 20), pygame.Rect(960, 160, 600, 20), pygame.Rect(120, 460, 740, 20), pygame.Rect(0, 160, 500, 20),
            pygame.Rect(0, 60, 1920, 20), pygame.Rect(860, 860, 410, 20), pygame.Rect(960, 760, 480, 20), pygame.Rect(960, 660, 840, 20), pygame.Rect(1080, 560, 820, 20), pygame.Rect(1080, 460, 720, 20),
            pygame.Rect(1460, 360, 460, 20), pygame.Rect(20, 660, 740, 20), pygame.Rect(480, 560, 280, 20), pygame.Rect(120, 260, 260, 20), pygame.Rect(1540, 960, 360, 20), pygame.Rect(1270, 960, 170, 20),
            pygame.Rect(120, 960, 1030, 20), pygame.Rect(120, 560, 260, 20), pygame.Rect(120, 760, 380, 20), pygame.Rect(20, 860, 360, 20), pygame.Rect(0, 1060, 1920, 20)
        ]
    if lvl == 3:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 60, 75, 6, 1050, 225, 1840, 415, 1450, 910, 50, 50
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl3.mp3", "Уровень 3", "Лабиринт: Уровень 3", "pic/lvl3.png", "pic/model3.png", "pic/object3.png"
        color = (130, 117, 100)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 60, 500
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(1390, 370, 30, 200), pygame.Rect(1390, 660, 30, 200), pygame.Rect(1520, 470, 30, 100), pygame.Rect(1520, 860, 30, 100), pygame.Rect(1640, 370, 30, 610), pygame.Rect(1770, 270, 30, 510), pygame.Rect(1770, 960, 30, 100), 
            pygame.Rect(890, 470, 30, 300), pygame.Rect(1010, 560, 30, 120), pygame.Rect(1140, 170, 30, 120), pygame.Rect(1140, 370, 30, 300), pygame.Rect(1140, 860, 30, 200), pygame.Rect(1260, 170, 30, 500), pygame.Rect(1260, 760, 40, 200), 
            pygame.Rect(260, 660, 20, 120), pygame.Rect(260, 860, 20, 120), pygame.Rect(380, 560, 30, 200), pygame.Rect(510, 270, 30, 500), pygame.Rect(510, 960, 30, 100), pygame.Rect(630, 370, 30, 600), pygame.Rect(760, 560, 30, 120), 
            pygame.Rect(130, 960, 20, 200), pygame.Rect(130, 660, 20, 200), pygame.Rect(390, 270, 20, 200), pygame.Rect(130, 370, 20, 200), pygame.Rect(0, 70, 20, 1010), pygame.Rect(1900, 70, 20, 420), pygame.Rect(1900, 560, 20, 500), 
            # Строки
            pygame.Rect(1640, 860, 260, 20), 
            pygame.Rect(1260, 170, 540, 20), pygame.Rect(1260, 960, 290, 20), pygame.Rect(1390, 370, 280, 20), pygame.Rect(1390, 560, 160, 20), pygame.Rect(1390, 860, 160, 20), pygame.Rect(1510, 760, 160, 20), pygame.Rect(1770, 470, 160, 20), 
            pygame.Rect(630, 960, 410, 20), pygame.Rect(760, 860, 410, 20), pygame.Rect(630, 560, 160, 20), pygame.Rect(760, 470, 280, 20), pygame.Rect(1010, 660, 160, 20), pygame.Rect(1260, 660, 290, 20), pygame.Rect(1260, 270, 540, 20), 
            pygame.Rect(130, 860, 530, 20), pygame.Rect(250, 470, 160, 20), pygame.Rect(380, 760, 160, 20), pygame.Rect(380, 960, 160, 20), pygame.Rect(510, 270, 660, 20), pygame.Rect(630, 370, 540, 20), pygame.Rect(630, 760, 670, 20), 
            pygame.Rect(130, 660, 150, 20), pygame.Rect(130, 370, 150, 20), pygame.Rect(20, 560, 390, 20), pygame.Rect(20, 270, 390, 20), pygame.Rect(130, 170, 1040, 20), pygame.Rect(0, 70, 1920, 20), pygame.Rect(0, 1060, 1920, 20)
        ]
    if lvl == 4:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 60, 60, 6, 1510, 770, 1168, 476, 1684, 314, 40, 40
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl4.mp3", "Уровень 4", "Лабиринт: Уровень 4", "pic/lvl4.png", "pic/model4.png", "pic/object4.png"
        color = (237, 242, 123)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 40, 860
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(0, 60, 40, 1020), pygame.Rect(170, 170, 20, 90), pygame.Rect(170, 330, 20, 640), pygame.Rect(360, 260, 20, 160), pygame.Rect(420, 60, 20, 120), pygame.Rect(360, 490, 20, 260), pygame.Rect(360, 820, 20, 60),
            pygame.Rect(510, 370, 20, 400), pygame.Rect(680, 460, 20, 240), pygame.Rect(1230, 460, 20, 240), pygame.Rect(850, 550, 20, 60), pygame.Rect(1400, 370, 20, 300), pygame.Rect(1300, 170, 20, 100), pygame.Rect(1760, 60, 20, 910),
            pygame.Rect(600, 950, 20, 100), pygame.Rect(860, 860, 20, 90), pygame.Rect(1570, 260, 20, 310), pygame.Rect(1570, 640, 20, 240), pygame.Rect(1880, 170, 40, 870),
            # Строки
            pygame.Rect(490, 950, 670, 20), pygame.Rect(1270, 950, 490, 20), 
            pygame.Rect(1400, 460, 190, 20), pygame.Rect(1380, 750, 210, 20), pygame.Rect(510, 770, 910, 20), pygame.Rect(680, 440, 570, 20), pygame.Rect(850, 530, 230, 20), pygame.Rect(850, 680, 400, 20), 
            pygame.Rect(360, 670, 150, 20), pygame.Rect(360, 860, 1210, 20), pygame.Rect(510, 350, 400, 20), pygame.Rect(1020, 350, 400, 20), pygame.Rect(1180, 170, 580, 20), pygame.Rect(1480, 260, 280, 20), 
            pygame.Rect(360, 260, 1020, 20), pygame.Rect(170, 400, 210, 20), pygame.Rect(170, 950, 210, 20), pygame.Rect(170, 170, 910, 20), pygame.Rect(170, 170, 910, 20), pygame.Rect(0, 1040, 1920, 40), pygame.Rect(0, 60, 1920, 40)
        ]
    if lvl == 5:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 35, 105, 6, 1644, 822, 144, 822, 1632, 90, 40, 40
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl5.mp3", "Уровень 5", "Лабиринт: Уровень 5", "pic/lvl5.png", "pic/model5.png", "pic/object5.png"
        color = (255, 179, 4)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 150, 90
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(1690, 230, 20, 60), pygame.Rect(1690, 340, 20, 210), pygame.Rect(1790, 230, 20, 370), pygame.Rect(1790, 760, 20, 160), pygame.Rect(1200, 1010, 20, 60), 
            pygame.Rect(1490, 710, 20, 210), pygame.Rect(1500, 130, 20, 60), pygame.Rect(1600, 80, 20, 60), pygame.Rect(1600, 180, 20, 60), pygame.Rect(1590, 390, 20, 120), pygame.Rect(1590, 760, 20, 110), pygame.Rect(1700, 810, 20, 60), 
            pygame.Rect(1300, 130, 20, 110), pygame.Rect(1300, 390, 20, 110), pygame.Rect(1300, 600, 20, 60), pygame.Rect(1300, 760, 20, 260), pygame.Rect(1400, 650, 20, 310), pygame.Rect(1400, 340, 20, 210), pygame.Rect(1490, 290, 20, 260), 
            pygame.Rect(1000, 290, 20, 360), pygame.Rect(1100, 130, 20, 260), pygame.Rect(1100, 440, 20, 210), pygame.Rect(1100, 860, 20, 60), pygame.Rect(1200, 810, 20, 110), pygame.Rect(1200, 500, 20, 110), pygame.Rect(1200, 80, 20, 360), 
            pygame.Rect(800, 340, 20, 110), pygame.Rect(800, 500, 20, 60), pygame.Rect(800, 650, 20, 60), pygame.Rect(800, 910, 20, 110), pygame.Rect(900, 390, 20, 210), pygame.Rect(900, 860, 20, 160), pygame.Rect(1000, 810, 20, 160), 
            pygame.Rect(600, 710, 20, 60), pygame.Rect(600, 810, 20, 160), pygame.Rect(700, 710, 20, 60), pygame.Rect(700, 860, 20, 60), pygame.Rect(700, 960, 20, 60), pygame.Rect(700, 390, 20, 60), pygame.Rect(800, 240, 20, 60), 
            pygame.Rect(400, 810, 20, 160), pygame.Rect(500, 810, 20, 160), pygame.Rect(500, 600, 20, 110), pygame.Rect(500, 130, 20, 60), pygame.Rect(600, 80, 20, 60), pygame.Rect(500, 390, 20, 120), pygame.Rect(600, 340, 20, 160), 
            pygame.Rect(300, 390, 20, 210), pygame.Rect(300, 130, 20, 210), pygame.Rect(200, 500, 20, 60), pygame.Rect(200, 650, 20, 160), pygame.Rect(300, 760, 20, 160), pygame.Rect(400, 130, 20, 160), pygame.Rect(400, 390, 20, 160), 
            pygame.Rect(200, 180, 20, 160), pygame.Rect(100, 960, 20, 60), pygame.Rect(100, 810, 20, 60), pygame.Rect(100, 600, 20, 160), pygame.Rect(100, 130, 20, 310), pygame.Rect(0, 80, 20, 1000), pygame.Rect(1900, 80, 20, 1000), 
            # Строки
            pygame.Rect(1690, 230, 120, 10), pygame.Rect(1490, 550, 220, 10), pygame.Rect(1490, 700, 420, 10), pygame.Rect(1490, 910, 320, 10), pygame.Rect(1400, 960, 510, 10), pygame.Rect(1600, 760, 210, 10), pygame.Rect(1600, 860, 110, 10),
            pygame.Rect(1300, 1010, 510, 10), pygame.Rect(1400, 650, 410, 10), pygame.Rect(1400, 180, 120, 10), pygame.Rect(1600, 130, 220, 10), pygame.Rect(1600, 180, 320, 10), pygame.Rect(1590, 340, 120, 10), pygame.Rect(1590, 390, 120, 10),
            pygame.Rect(1200, 340, 220, 10), pygame.Rect(1200, 550, 220, 10), pygame.Rect(1200, 500, 120, 10), pygame.Rect(1300, 130, 220, 10), pygame.Rect(1300, 230, 320, 10), pygame.Rect(1300, 280, 410, 10), pygame.Rect(1300, 600, 510, 10),
            pygame.Rect(900, 230, 220, 10), pygame.Rect(900, 1010, 320, 10), pygame.Rect(800, 700, 620, 10), pygame.Rect(1000, 960, 320, 10), pygame.Rect(1100, 910, 120, 10), pygame.Rect(1100, 440, 120, 10), pygame.Rect(1100, 650, 220, 10), 
            pygame.Rect(600, 500, 220, 10), pygame.Rect(600, 810, 620, 10), pygame.Rect(600, 960, 120, 10), pygame.Rect(700, 440, 120, 10), pygame.Rect(700, 760, 620, 10), pygame.Rect(700, 860, 220, 10), pygame.Rect(700, 910, 120, 10), 
            pygame.Rect(400, 810, 120, 10), pygame.Rect(400, 390, 120, 10), pygame.Rect(400, 550, 420, 10), pygame.Rect(500, 180, 620, 10), pygame.Rect(500, 230, 320, 10), pygame.Rect(600, 130, 410, 10), pygame.Rect(600, 650, 420, 10), 
            pygame.Rect(10, 910, 310, 10), pygame.Rect(200, 340, 820, 10), pygame.Rect(200, 650, 200, 10), pygame.Rect(300, 700, 220, 10), pygame.Rect(300, 760, 320, 10), pygame.Rect(400, 290, 620, 10), pygame.Rect(400, 130, 120, 10), 
            pygame.Rect(100, 600, 820, 10), pygame.Rect(100, 810, 120, 10), pygame.Rect(100, 860, 220, 10), pygame.Rect(100, 960, 320, 10), pygame.Rect(100, 1010, 620, 10), pygame.Rect(10, 500, 210, 10), pygame.Rect(10, 760, 110, 10), 
            pygame.Rect(100, 550, 120, 10), pygame.Rect(100, 440, 120, 10), pygame.Rect(100, 390, 220, 10), pygame.Rect(100, 130, 120, 10), pygame.Rect(1810, 1070, 110, 10), pygame.Rect(0, 1070, 1700, 10), pygame.Rect(0, 80, 1920, 10)
        ]
    if lvl == 6:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 40, 90, 6, 620, 568, 814, 568, 838, 862, 30, 30
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl6.mp3", "Уровень 6", "Лабиринт: Уровень 6", "pic/lvl6.png", "pic/model6.png", "pic/object6.png"
        color = (225, 225, 225)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 940, 70
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(1780, 320, 30, 60), pygame.Rect(1780, 440, 30, 160), pygame.Rect(1780, 660, 30, 120), pygame.Rect(1780, 900, 30, 120), 
            pygame.Rect(1550, 960, 30, 60), pygame.Rect(1680, 440, 30, 110), pygame.Rect(1680, 660, 30, 120), pygame.Rect(1680, 840, 30, 180), pygame.Rect(1780, 60, 30, 90), pygame.Rect(1780, 200, 30, 60), 
            pygame.Rect(1440, 320, 30, 170), pygame.Rect(1440, 730, 30, 110), pygame.Rect(1550, 60, 30, 90), pygame.Rect(1550, 200, 30, 60), pygame.Rect(1550, 320, 30, 230), pygame.Rect(1550, 610, 30, 240), 
            pygame.Rect(1220, 610, 30, 400), pygame.Rect(1330, 140, 30, 120), pygame.Rect(1330, 440, 30, 230), pygame.Rect(1330, 780, 30, 120), pygame.Rect(1330, 950, 30, 70), pygame.Rect(1440, 140, 30, 120),
            pygame.Rect(1000, 800, 30, 100), pygame.Rect(1000, 960, 30, 60), pygame.Rect(1110, 850, 30, 40), pygame.Rect(1110, 1010, 30, 60), pygame.Rect(1220, 320, 30, 60), pygame.Rect(1220, 440, 30, 60), 
            pygame.Rect(890, 390, 30, 50), pygame.Rect(890, 550, 30, 60), pygame.Rect(890, 850, 30, 40), pygame.Rect(890, 950, 30, 120), pygame.Rect(1000, 60, 30, 80), pygame.Rect(1000, 560, 30, 170), 
            pygame.Rect(670, 260, 30, 240), pygame.Rect(670, 730, 30, 290), pygame.Rect(780, 380, 30, 240), pygame.Rect(780, 680, 30, 50), pygame.Rect(780, 850, 30, 170), pygame.Rect(890, 260, 30, 60), 
            pygame.Rect(440, 960, 30, 60), pygame.Rect(550, 140, 30, 60), pygame.Rect(550, 260, 30, 50), pygame.Rect(550, 560, 30, 60), pygame.Rect(550, 670, 30, 70), pygame.Rect(550, 790, 30, 120), 
            pygame.Rect(330, 550, 30, 120), pygame.Rect(330, 850, 30, 50), pygame.Rect(330, 950, 30, 60), pygame.Rect(440, 60, 30, 250), pygame.Rect(440, 440, 30, 50), pygame.Rect(440, 610, 30, 120), 
            pygame.Rect(220, 140, 30, 230), pygame.Rect(220, 440, 30, 50), pygame.Rect(220, 550, 30, 120), pygame.Rect(220, 730, 30, 50), pygame.Rect(330, 140, 30, 120), pygame.Rect(330, 320, 30, 50), 
            pygame.Rect(0, 60, 20, 1020), pygame.Rect(1900, 60, 20, 1020), pygame.Rect(110, 140, 30, 120), pygame.Rect(110, 370, 30, 240), pygame.Rect(110, 850, 30, 50), pygame.Rect(110, 960, 30, 1010),
            # Строки
            pygame.Rect(1680, 435, 130, 10), pygame.Rect(1680, 540, 130, 10), pygame.Rect(1800, 720, 130, 10), pygame.Rect(1800, 840, 130, 10), 
            pygame.Rect(1560, 720, 130, 10), pygame.Rect(1560, 840, 130, 10), pygame.Rect(1560, 890, 130, 10), pygame.Rect(1450, 1010, 360, 10), pygame.Rect(1680, 140, 130, 10), pygame.Rect(1680, 380, 230, 10), 
            pygame.Rect(1340, 600, 470, 10), pygame.Rect(1340, 950, 240, 10), pygame.Rect(1450, 430, 130, 10), pygame.Rect(1450, 540, 130, 10), pygame.Rect(1560, 200, 250, 10), pygame.Rect(1560, 320, 250, 10), 
            pygame.Rect(1230, 260, 470, 10), pygame.Rect(1230, 780, 240, 10), pygame.Rect(1340, 380, 130, 10), pygame.Rect(1340, 660, 130, 10), pygame.Rect(1340, 720, 130, 10), pygame.Rect(1340, 890, 130, 10), 
            pygame.Rect(1000, 550, 250, 10), pygame.Rect(1000, 660, 250, 10), pygame.Rect(1000, 1010, 250, 10), pygame.Rect(1000, 950, 140, 10), pygame.Rect(1120, 435, 240, 10), pygame.Rect(1120, 140, 240, 10), 
            pygame.Rect(780, 730, 360, 10), pygame.Rect(780, 850, 130, 10), pygame.Rect(780, 950, 130, 10), pygame.Rect(890, 890, 250, 10), pygame.Rect(890, 435, 140, 10), pygame.Rect(1000, 380, 250, 10), 
            pygame.Rect(790, 140, 240, 10), pygame.Rect(780, 320, 690, 10), pygame.Rect(780, 380, 140, 10), pygame.Rect(780, 490, 470, 10), pygame.Rect(1020, 1070, 900, 10), pygame.Rect(780, 790, 360, 10), 
            pygame.Rect(560, 610, 360, 10), pygame.Rect(560, 670, 360, 10), pygame.Rect(560, 730, 130, 10), pygame.Rect(560, 840, 130, 10), pygame.Rect(560, 1010, 130, 10), pygame.Rect(670, 260, 470, 10), 
            pygame.Rect(330, 550, 370, 10), pygame.Rect(330, 490, 370, 10), pygame.Rect(330, 610, 140, 10), pygame.Rect(440, 200, 900, 10), pygame.Rect(440, 950, 240, 10), pygame.Rect(560, 140, 130, 10), 
            pygame.Rect(220, 140, 140, 10), pygame.Rect(220, 430, 360, 10), pygame.Rect(220, 900, 360, 10), pygame.Rect(220, 720,  250, 10), pygame.Rect(330, 310, 250, 10), pygame.Rect(330, 370, 250, 10), 
            pygame.Rect(110, 1010, 250, 10), pygame.Rect(110, 950, 140, 10), pygame.Rect(110, 660, 140, 10), pygame.Rect(110, 550, 140, 10), pygame.Rect(110, 490, 140, 10), pygame.Rect(110, 370, 140, 10), 
            pygame.Rect(110, 840, 360, 10), pygame.Rect(20, 780, 450, 10), pygame.Rect(20, 720, 120, 10), pygame.Rect(20, 310, 120, 10), pygame.Rect(20, 200, 120, 10), pygame.Rect(0, 60, 1920, 10), pygame.Rect(0, 1070, 920, 10)
        ]
    if lvl == 7:
        # Константы
        PLAYER_SIZE, initial_time, SPEED, obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj_w, obj_h = 20, 300, 6, 574, 664, 850, 526, 1075, 934, 30, 20
        loadMusic, lvlName, lvlCaption, backImage, modelImage, objectImage = "music/lvl7.mp3", "Уровень 7", "Лабиринт: Уровень 7", "pic/lvl7.png", "pic/model7.png", "pic/object7.png"
        color = (112, 200, 173)
        # Координаты игрока
        if player_x == 0 and player_y == 0:
            player_x, player_y = 10, 520
        # генерация конструкции уровня (карта мира)
        obstacles = [
            # Столбцы
            pygame.Rect(1670, 545, 10, 80), pygame.Rect(1715, 360, 10, 190), pygame.Rect(1715, 580, 10, 40), pygame.Rect(1765, 580, 15, 40), pygame.Rect(1765, 400, 10, 115), pygame.Rect(1810, 470, 10, 45), pygame.Rect(1860, 470, 10, 195),
            pygame.Rect(1485, 580, 10, 75), pygame.Rect(1530, 430, 10, 120), pygame.Rect(1530, 620, 10, 110), pygame.Rect(1580, 655, 10, 275), pygame.Rect(1580, 360, 10, 40), pygame.Rect(1580, 505, 10, 40), pygame.Rect(1625, 585, 10, 110),
            pygame.Rect(1300, 400, 10, 70), pygame.Rect(1300, 545, 10, 85), pygame.Rect(1300, 810, 10, 120), pygame.Rect(1350, 430, 10, 35), pygame.Rect(1350, 545, 10, 115), pygame.Rect(1350, 880, 10, 75), pygame.Rect(1485, 430, 10, 110), 
            pygame.Rect(1160, 545, 10, 190), pygame.Rect(1205, 360, 15, 40), pygame.Rect(1210, 545, 10, 120), pygame.Rect(1210, 705, 10, 35), pygame.Rect(1210, 855, 10, 70), pygame.Rect(1255, 855, 10, 40), pygame.Rect(1255, 505, 10, 160), 
            pygame.Rect(1070, 350, 10, 50), pygame.Rect(1070, 470, 10, 200), pygame.Rect(1070, 770, 10, 45), pygame.Rect(1070, 700, 10, 40), pygame.Rect(1115, 400, 10, 40), pygame.Rect(1115, 505, 10, 350), pygame.Rect(1115, 920, 10, 45),
            pygame.Rect(930, 550, 10, 80), pygame.Rect(930, 700, 10, 40), pygame.Rect(980, 550, 10, 115), pygame.Rect(1020, 550, 10, 145), pygame.Rect(980, 740, 10, 70), pygame.Rect(1020, 360, 10, 40), pygame.Rect(1020, 470, 10, 50),
            pygame.Rect(790, 655, 10, 50), pygame.Rect(840, 350, 10, 40), pygame.Rect(835, 510, 10, 270), pygame.Rect(835, 845, 10, 160), pygame.Rect(885, 350, 10, 120), pygame.Rect(885, 510, 10, 120), pygame.Rect(880, 695, 10, 80), 
            pygame.Rect(700, 580, 10, 80), pygame.Rect(695, 740, 10, 150), pygame.Rect(740, 350, 10, 125), pygame.Rect(740, 880, 10, 125), pygame.Rect(740, 780, 10, 75), pygame.Rect(790, 815, 10, 150), pygame.Rect(790, 580, 10, 50), 
            pygame.Rect(560, 540, 10, 165), pygame.Rect(555, 440, 10, 35), pygame.Rect(560, 740, 10, 35), pygame.Rect(605, 505, 10, 310), pygame.Rect(650, 440, 10, 415), pygame.Rect(650, 360, 10, 40), pygame.Rect(700, 280, 10, 270), 
            pygame.Rect(420, 780, 10, 35), pygame.Rect(420, 850, 10, 80), pygame.Rect(465, 550, 10, 150), pygame.Rect(460, 880, 10, 50), pygame.Rect(510, 880, 10, 50), pygame.Rect(515, 465, 10, 40), pygame.Rect(510, 540, 10, 190), 
            pygame.Rect(280, 660, 10, 225), pygame.Rect(325, 620, 10, 195), pygame.Rect(325, 470, 10, 40), pygame.Rect(375, 620, 10, 45), pygame.Rect(370, 740, 10, 75), pygame.Rect(420, 440, 10, 75), pygame.Rect(420, 630, 10, 35), 
            pygame.Rect(140, 660, 10, 120), pygame.Rect(185, 740, 10, 75), pygame.Rect(235, 740, 10, 40), pygame.Rect(230, 540, 10, 40), pygame.Rect(235, 880, 10, 50), pygame.Rect(280, 465, 10, 40), pygame.Rect(280, 920, 10, 40), 
            pygame.Rect(50, 655, 10, 115), pygame.Rect(50, 805, 10, 40), pygame.Rect(50, 885, 10, 120), pygame.Rect(95, 550, 10, 40), pygame.Rect(95, 390, 15, 40), pygame.Rect(90, 660, 10, 195), pygame.Rect(90, 880, 10, 85), 
            pygame.Rect(1115, 315, 10, 50), pygame.Rect(235, 315, 10, 160), pygame.Rect(325, 315, 10, 85), pygame.Rect(375, 350, 10, 90), pygame.Rect(185, 350, 10, 160), pygame.Rect(45, 425, 10, 50), pygame.Rect(50, 550, 10, 40), 
            pygame.Rect(1440, 205, 10, 35), pygame.Rect(1810, 205, 10, 160), pygame.Rect(1860, 165, 10, 120), pygame.Rect(1860, 315, 10, 80), pygame.Rect(1675, 315, 10, 200), pygame.Rect(1440, 315, 10, 385), pygame.Rect(1395, 355, 10, 385), 
            pygame.Rect(1765, 90, 10, 200), pygame.Rect(1805, 90, 10, 80), pygame.Rect(1860, 90, 10, 50), pygame.Rect(1625, 60, 10, 40), pygame.Rect(1625, 140, 10, 400), pygame.Rect(1715, 130, 10, 120), pygame.Rect(1675, 165, 10, 80), 
            pygame.Rect(1345, 90, 10, 80), pygame.Rect(1345, 205, 10, 120), pygame.Rect(1385, 205, 10, 120), pygame.Rect(1395, 90, 10, 45), pygame.Rect(1440, 60, 10, 115), pygame.Rect(1490, 100, 10, 115), pygame.Rect(1580, 100, 10, 145), 
            pygame.Rect(1070, 100, 10, 40), pygame.Rect(1070, 170, 10, 80), pygame.Rect(1160, 170, 10, 120), pygame.Rect(1115, 205, 10, 85), pygame.Rect(1210, 130, 10, 80), pygame.Rect(1210, 240, 10, 80), pygame.Rect(1300, 60, 10, 300),
            pygame.Rect(785, 165, 10, 85), pygame.Rect(885, 130, 10, 190), pygame.Rect(925, 240, 15, 230), pygame.Rect(975, 320, 15, 190), pygame.Rect(975, 100, 10, 110), pygame.Rect(1020, 100, 10, 140), pygame.Rect(1255, 100, 10, 340), 
            pygame.Rect(190, 205, 10, 80), pygame.Rect(230, 240, 10, 40), pygame.Rect(280, 240, 10, 200), pygame.Rect(370, 240, 10, 50), pygame.Rect(650, 290, 10, 35), pygame.Rect(835, 290, 10, 35), pygame.Rect(835, 140, 10, 100), 
            pygame.Rect(555, 165, 10, 85), pygame.Rect(655, 165, 10, 50), pygame.Rect(695, 90, 10, 150), pygame.Rect(745, 130, 10, 150), pygame.Rect(465, 165, 10, 150), pygame.Rect(840, 60, 10, 40), pygame.Rect(930, 60, 10, 150), 
            pygame.Rect(45, 90, 10, 40), pygame.Rect(325, 60, 10, 115), pygame.Rect(375, 90, 10, 125), pygame.Rect(465, 90, 10, 50), pygame.Rect(655, 90, 10, 50), pygame.Rect(515, 60, 10, 190), pygame.Rect(555, 60, 10, 80), 
            pygame.Rect(1490, 1040, 10, 40), pygame.Rect(1070, 1040, 10, 40), pygame.Rect(790, 1040, 10, 40), pygame.Rect(230, 995, 10, 85), pygame.Rect(0, 60, 10, 1070), pygame.Rect(1910, 50, 10, 455), pygame.Rect(1910, 540, 10, 540),
            pygame.Rect(95, 995, 10, 40), pygame.Rect(185, 995, 10, 40), pygame.Rect(375, 995, 10, 40), pygame.Rect(420, 955, 10, 90), pygame.Rect(650, 955, 10, 90), pygame.Rect(695, 925, 10, 120), pygame.Rect(975, 880, 10, 125), 
            pygame.Rect(885, 845, 10, 200), pygame.Rect(930, 845, 10, 200), pygame.Rect(1020, 880, 10, 85), pygame.Rect(1160, 880, 10, 115), pygame.Rect(1300, 995, 10, 50), pygame.Rect(1345, 995, 10, 50), pygame.Rect(1390, 955, 10, 90),
            pygame.Rect(1440, 995, 10, 50), pygame.Rect(1625, 995, 10, 50), pygame.Rect(1810, 995, 10, 50), pygame.Rect(1860, 995, 10, 50), pygame.Rect(1860, 845, 10, 120), pygame.Rect(1810, 805, 10, 85), pygame.Rect(1860, 730, 10, 40),
            pygame.Rect(1810, 925, 10, 40), pygame.Rect(1765, 730, 10, 270), pygame.Rect(1720, 775, 10, 190), pygame.Rect(1625, 775, 10, 190), pygame.Rect(1535, 770, 10, 160), pygame.Rect(420, 130, 10, 190), pygame.Rect(100, 210, 10, 80), 
            pygame.Rect(1490, 770, 10, 80), pygame.Rect(1440, 770, 10, 40), pygame.Rect(1490, 960, 10, 45), pygame.Rect(1675, 920, 10, 45), pygame.Rect(1675, 805, 10, 85), pygame.Rect(50, 240, 10, 110), pygame.Rect(140, 170, 10, 150),
            pygame.Rect(1810, 585, 10, 80), 
            # Строки
            pygame.Rect(1445, 1035, 55, 10), pygame.Rect(1530, 1035, 290, 10), pygame.Rect(10, 1035, 185, 10), pygame.Rect(275, 1035, 110, 10), pygame.Rect(430, 1035, 230, 10), pygame.Rect(700, 1035, 195, 10), pygame.Rect(935, 1035, 100, 10),
            pygame.Rect(1070, 1035, 200, 10), pygame.Rect(1345, 1035, 45, 10), pygame.Rect(230, 995, 150, 10), pygame.Rect(460, 995, 150, 10), pygame.Rect(790, 995, 50, 10), pygame.Rect(980, 995, 370, 10), pygame.Rect(1440, 995, 50, 10),
            pygame.Rect(1530, 995, 100, 10), pygame.Rect(1670, 995, 150, 10), pygame.Rect(1025, 955, 100, 10), pygame.Rect(1165, 955, 195, 10), pygame.Rect(1165, 955, 195, 10), pygame.Rect(1440, 955, 195, 10), pygame.Rect(1860, 955, 50, 10),
            pygame.Rect(1860, 995, 50, 10), pygame.Rect(140, 995, 50, 10), pygame.Rect(135, 920, 105, 10), pygame.Rect(280, 920, 140, 10), pygame.Rect(460, 920, 245, 10), pygame.Rect(1070, 920, 55, 10), pygame.Rect(1210, 920, 100, 10),
            pygame.Rect(1350, 920, 230, 10), pygame.Rect(95, 955, 520, 10), pygame.Rect(280, 880, 150, 10), pygame.Rect(510, 880, 240, 10), pygame.Rect(1020, 880, 150, 10), pygame.Rect(1350, 880, 150, 10), pygame.Rect(1680, 880, 50, 10),
            pygame.Rect(1625, 920, 50, 10), pygame.Rect(1775, 920, 45, 10), pygame.Rect(320, 845, 335, 10), pygame.Rect(695, 845, 50, 10), pygame.Rect(790, 845, 50, 10), pygame.Rect(885, 845, 380, 10), pygame.Rect(1300, 845, 200, 10),
            pygame.Rect(10, 880, 50, 10), pygame.Rect(95, 880, 150, 10), pygame.Rect(605, 805, 50, 10), pygame.Rect(790, 805, 280, 10), pygame.Rect(1160, 805, 150, 10), pygame.Rect(1345, 805, 105, 10), pygame.Rect(1810, 805, 100, 10),
            pygame.Rect(10, 845, 50, 10), pygame.Rect(95, 845, 190, 10), pygame.Rect(1120, 770, 320, 10), pygame.Rect(1625, 770, 105, 10), pygame.Rect(1770, 770, 100, 10), pygame.Rect(95, 805, 55, 10), pygame.Rect(185, 805, 100, 10),
            pygame.Rect(325, 805, 50, 10), pygame.Rect(420, 805, 150, 10), pygame.Rect(1160, 730, 610, 10), pygame.Rect(1810, 730, 50, 10), pygame.Rect(10, 770, 50, 10), pygame.Rect(420, 770, 150, 10), pygame.Rect(740, 770, 60, 10),
            pygame.Rect(880, 770, 60, 10), pygame.Rect(1020, 770, 60, 10), pygame.Rect(325, 695, 150, 10), pygame.Rect(185, 695, 100, 10), pygame.Rect(185, 730, 60, 10), pygame.Rect(370, 730, 200, 10), pygame.Rect(695, 730, 150, 10),
            pygame.Rect(980, 730, 100, 10), pygame.Rect(980, 730, 100, 10), pygame.Rect(835, 655, 150, 10), pygame.Rect(1260, 655, 100, 10), pygame.Rect(1440, 655, 55, 10), pygame.Rect(1440, 695, 55, 10), pygame.Rect(1625, 695, 285, 10),
            pygame.Rect(1210, 695, 150, 10), pygame.Rect(650, 695, 150, 10), pygame.Rect(610, 620, 50, 10), pygame.Rect(740, 620, 50, 10), pygame.Rect(1540, 620, 50, 10), pygame.Rect(1670, 620, 110, 10), pygame.Rect(1670, 655, 200, 10),
            pygame.Rect(90, 655, 200, 10), pygame.Rect(700, 655, 100, 10), pygame.Rect(230, 580, 245, 10), pygame.Rect(700, 580, 100, 10), pygame.Rect(1490, 580, 190, 10), pygame.Rect(1770, 580, 50, 10), pygame.Rect(10, 620, 190, 10),
            pygame.Rect(235, 620, 150, 10), pygame.Rect(420, 620, 50, 10), pygame.Rect(1020, 540, 60, 10), pygame.Rect(1160, 540, 60, 10), pygame.Rect(1300, 540, 60, 10), pygame.Rect(1440, 540, 55, 10), pygame.Rect(1580, 540, 55, 10),
            pygame.Rect(1720, 540, 150, 10), pygame.Rect(95, 580, 100, 10), pygame.Rect(1770, 505, 50, 10), pygame.Rect(10, 540, 50, 10), pygame.Rect(95, 540, 195, 10), pygame.Rect(325, 540, 150, 10), pygame.Rect(510, 540, 60, 10),
            pygame.Rect(700, 540, 100, 10), pygame.Rect(930, 540, 60, 10), pygame.Rect(10, 505, 140, 10), pygame.Rect(185, 505, 105, 10), pygame.Rect(325, 505, 200, 10), pygame.Rect(555, 505, 60, 10), pygame.Rect(700, 505, 290, 10),
            pygame.Rect(1115, 505, 245, 10), pygame.Rect(1675, 505, 50, 10), pygame.Rect(45, 465, 150, 10), pygame.Rect(280, 465, 100, 10), pygame.Rect(465, 465, 60, 10), pygame.Rect(555, 465, 60, 10), pygame.Rect(790, 465, 150, 10),
            pygame.Rect(1020, 465, 385, 10), pygame.Rect(1535, 465, 55, 10), pygame.Rect(95, 430, 55, 10), pygame.Rect(280, 430, 100, 10), pygame.Rect(420, 430, 240, 10), pygame.Rect(740, 430, 155, 10), pygame.Rect(980, 430, 280, 10),
            pygame.Rect(1530, 430, 100, 10), pygame.Rect(1765, 430, 150, 10), pygame.Rect(790, 390, 60, 10), pygame.Rect(790, 390, 60, 10), pygame.Rect(1070, 390, 105, 10), pygame.Rect(1205, 390, 60, 10), pygame.Rect(1300, 390, 60, 10),
            pygame.Rect(1440, 390, 150, 10), pygame.Rect(1765, 390, 105, 10), pygame.Rect(1160, 350, 60, 10), pygame.Rect(1300, 350, 105, 10), pygame.Rect(1485, 350, 105, 10), pygame.Rect(1715, 350, 60, 10), pygame.Rect(10, 390, 100, 10),
            pygame.Rect(140, 390, 50, 10), pygame.Rect(420, 390, 240, 10), pygame.Rect(975, 315, 245, 10), pygame.Rect(1390, 315, 200, 10), pygame.Rect(1675, 315, 140, 10), pygame.Rect(50, 350, 145, 10), pygame.Rect(375, 350, 325, 10),
            pygame.Rect(745, 350, 150, 10), pygame.Rect(1020, 350, 55, 10), pygame.Rect(790, 240, 55, 10), pygame.Rect(980, 240, 50, 10), pygame.Rect(1440, 240, 150, 10), pygame.Rect(10, 315, 50, 10), pygame.Rect(95, 315, 150, 10),
            pygame.Rect(330, 315, 330, 10), pygame.Rect(740, 315, 100, 10), pygame.Rect(475, 280, 140, 10), pygame.Rect(650, 280, 195, 10), pygame.Rect(925, 280, 195, 10), pygame.Rect(1440, 280, 335, 10), pygame.Rect(1860, 280, 50, 10),
            pygame.Rect(280, 240, 100, 10), pygame.Rect(560, 240, 145, 10), pygame.Rect(1070, 205, 55, 10), pygame.Rect(1210, 205, 55, 10), pygame.Rect(1350, 205, 100, 10), pygame.Rect(1490, 205, 100, 10), pygame.Rect(190, 280, 50, 10),
            pygame.Rect(190, 280, 50, 10), pygame.Rect(325, 280, 50, 10), pygame.Rect(560, 165, 100, 10), pygame.Rect(1070, 165, 100, 10), pygame.Rect(1345, 165, 100, 10), pygame.Rect(10, 205, 100, 10), pygame.Rect(190, 205, 190, 10),
            pygame.Rect(600, 205, 60, 10), pygame.Rect(885, 205, 55, 10), pygame.Rect(420, 130, 50, 10), pygame.Rect(560, 130, 100, 10), pygame.Rect(745, 130, 100, 10), pygame.Rect(1120, 130, 100, 10), pygame.Rect(1625, 130, 100, 10),
            pygame.Rect(10, 165, 140, 10), pygame.Rect(190, 165, 140, 10), pygame.Rect(885, 90, 50, 10), pygame.Rect(975, 90, 290, 10), pygame.Rect(1345, 90, 60, 10), pygame.Rect(1490, 90, 100, 10), pygame.Rect(1675, 90, 100, 10),
            pygame.Rect(1770, 165, 100, 10), pygame.Rect(1810, 90, 60, 10), pygame.Rect(695, 90, 150, 10), pygame.Rect(605, 90, 55, 10), pygame.Rect(375, 90, 100, 10), pygame.Rect(45, 90, 290, 10), pygame.Rect(45, 130, 245, 10),
            pygame.Rect(1675, 245, 50, 10), pygame.Rect(0, 50, 1920, 10), pygame.Rect(0, 1070, 1920, 10), pygame.Rect(885, 315, 50, 10), pygame.Rect(880, 695, 200, 10)
        ]
    # Загрузка и воспроизведение музыки
    pygame.mixer.music.load(loadMusic)
    pygame.mixer.music.play(0, ela_time, 0)
    pygame.mixer.music.set_volume(0.2)
    # Смена названия окна
    pygame.display.set_caption(lvlCaption)
    # Таймер
    start_time = time.time()
    # Загрузка фона уровня, модели игрока, модели приза
    background = pygame.image.load(backImage)
    player_model = pygame.image.load(modelImage)
    background = pygame.transform.scale(background, (1920, 1080))
    player_model = pygame.transform.scale(player_model, (PLAYER_SIZE, PLAYER_SIZE))
    obj = pygame.image.load(objectImage)
    obj = pygame.transform.scale(obj, (obj_w, obj_h))
    # Координаты объектов
    obj_positions = [(obj1_x, obj1_y), (obj2_x, obj2_y), (obj3_x, obj3_y)]
    # Игровой цикл
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Работа таймера
        elapsed_time = int(time.time() - start_time)
        if isNew == 0: elapsed_time += ela_time
        remaining_time = initial_time - elapsed_time
        minutes = remaining_time // 60
        seconds = remaining_time - minutes * 60
        # Получение нажатых клавиш
        keys = pygame.key.get_pressed()
        new_x, new_y = player_x, player_y
        if keys[pygame.K_w] or keys[pygame.K_UP]: new_y -= SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: new_y += SPEED
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: new_x -= SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: new_x += SPEED
        if keys[pygame.K_r]:
            remaining_time, elapsed_time, score, collected, isCollected, player_x, player_y, isNew, ela_time = 0, 0, 0, 0, [0, 0, 0], 0, 0, 1, 0
            play()
        if keys[pygame.K_ESCAPE]:
            isRunning = False
            pygame.mixer.music.pause()
            isNew = 0
            ela_time = elapsed_time
            with open("userdata.txt", "w") as file: json.dump([lvl, score, collected, isCollected, player_x, player_y, ela_time], file)
            main_menu()
        # Проверка на столкновение с препятствиями
        player_rect = pygame.Rect(new_x, new_y, PLAYER_SIZE, PLAYER_SIZE)
        if not any(player_rect.colliderect(obstacle) for obstacle in obstacles):
            player_x, player_y = new_x, new_y
        # Проверка на столкновение с объектами
        for i, (obj_x, obj_y) in enumerate(obj_positions):
            obj_rect = pygame.Rect(obj_x, obj_y, obj_w, obj_h)
            if player_rect.colliderect(obj_rect) and not isCollected[i]:
                isCollected[i] = 1
                collected += 1
                score += 100
        # Обновление экрана
        screen.blit(background, (0, 0))
        screen.blit(font.render(lvlName, True, (255, 255, 255)), (840, 2))
        for i, (obj_x, obj_y) in enumerate(obj_positions):
            if not isCollected[i]:
                screen.blit(obj, (obj_x, obj_y))
        screen.blit(player_model, (player_x, player_y))
        if seconds < 10: screen.blit(font.render(f"Время: {minutes}:0{seconds}", True, (255, 255, 255)), (1500, 2))
        else: screen.blit(font.render(f"Время: {minutes}:{seconds}", True, (255, 255, 255)), (1500, 2))
        screen.blit(font.render(f"Счёт: {score}", True, (255, 255, 255)), (60, 2))
        for obstacle in obstacles:
            pygame.draw.rect(screen, color, obstacle)
        pygame.display.update()
        # Условие поражения
        if remaining_time == 0:
            isRunning = False
            pygame.mixer.music.pause()
            win_lose()
        # Условие победы
        if (player_x > 1921 and lvl in {1, 2, 3, 4, 7}) or (player_y > 1081 and lvl in {5, 6}):
            isRunning = False
            score += remaining_time * 10
            isWin = 1
            with open("stats.txt", "r") as file: lvl_score, lvl_time = json.load(file)
            if lvl_score[lvl] < score: lvl_score[lvl] = score
            if lvl_time[lvl] > elapsed_time or lvl_time[lvl] == 0: lvl_time[lvl] = elapsed_time
            with open("stats.txt", "w") as file: json.dump([lvl_score, lvl_time], file)
            lvl +=1
            win_lose()
def statistics():
    button_x, button_y, button_w, button_h = 660, 900, 500, 120
    minutes, seconds = [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
    global font, font1
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Действия при клике на кнопкy
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button_x <= x <= button_x + button_w and button_y <= y <= button_y + button_h: main_menu()
                else: statistics()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isRunning = False
            main_menu()
        pygame.display.set_caption("Лабиринт: Статистика")
        background = pygame.image.load("pic/stats.png")
        background = pygame.transform.scale(background, (1920, 1080))
        with open("stats.txt", "r") as file: lvl_score, lvl_time = json.load(file)
        for i in range (8):
            minutes[i] = lvl_time[i] // 60
            seconds[i] = lvl_time[i] - minutes[i] * 60
        screen.blit(background, (0, 0))
        screen.blit(font.render("Статистика", True, (255, 255, 255)), (750, 60))
        for i in range (8):
            if seconds[i] < 10: screen.blit(font1.render(f"Статистика {i} уровня: Максимум очков: {lvl_score[i]}. Лучшее время: {minutes[i]}:0{seconds[i]}", True, (255, 255, 255)), (300, 300+i*60))
            else: screen.blit(font1.render(f"Статистика {i} уровня: Максимум очков: {lvl_score[i]}. Лучшее время: {minutes[i]}:{seconds[i]}", True, (255, 255, 255)), (300, 300+i*60))
        screen.blit(font1.render("Выход в главное меню", True, (255, 255, 255)), (button_x+10, button_y+40))
        pygame.display.update()
def select_lvl():
    button1_x, button1_y, button1_w, button1_h = 660, 750, 500, 120
    button2_x, button2_y, button2_w, button2_h = 660, 900, 500, 120
    global font, font1, lvl, score, collected, isCollected, player_x, player_y, isNew, ela_time
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if button1_x <= x <= button1_x + button1_w and button1_y <= y <= button1_y + button1_h:
                    if lvl > 7: statistics()
                    with open("userdata.txt", "r") as file: lvl, score, collected, isCollected, player_x, player_y, ela_time = json.load(file)
                    isNew = 0
                    play()
                if button2_x <= x <= button2_x + button2_w and button2_y <= y <= button2_y + button2_h:
                    main_menu()
                if 270 <= y <= 270 + 200:
                    score, collected, isCollected, player_x, player_y, isNew, ela_time = 0, 0, [0, 0, 0], 0, 0, 1, 0
                    if 160 <= x <= 160 + 350:
                        lvl = 1
                    if 570 <= x <= 570 + 350:
                        lvl = 2
                    if 980 <= x <= 980 + 350:
                        lvl = 3
                    if 1390 <= x <= 1390 + 350:
                        lvl = 4
                    play()
                if 530 <= y <= 530 + 200:
                    score, collected, isCollected, player_x, player_y, isNew, ela_time = 0, 0, [0, 0, 0], 0, 0, 1, 0
                    if 160 <= x <= 160 + 350:
                        lvl = 5
                    if 570 <= x <= 570 + 350:
                        lvl = 6
                    if 980 <= x <= 980 + 350:
                        lvl = 7
                    play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            isRunning = False
            main_menu()
        pygame.display.set_caption("Лабиринт: Выбор уровня")
        background = pygame.image.load("pic/select.png")
        lvl1 = pygame.image.load("pic/lvl1.png")
        lvl2 = pygame.image.load("pic/lvl2.png")
        lvl3 = pygame.image.load("pic/lvl3.png")
        lvl4 = pygame.image.load("pic/lvl4.png")
        lvl5 = pygame.image.load("pic/lvl5.png")
        lvl6 = pygame.image.load("pic/lvl6.png")
        lvl7 = pygame.image.load("pic/lvl7.png")
        background = pygame.transform.scale(background, (1920, 1080))
        lvl1 = pygame.transform.scale(lvl1, (350, 200))
        lvl2 = pygame.transform.scale(lvl2, (350, 200))
        lvl3 = pygame.transform.scale(lvl3, (350, 200))
        lvl4 = pygame.transform.scale(lvl4, (350, 200))
        lvl5 = pygame.transform.scale(lvl5, (350, 200))
        lvl6 = pygame.transform.scale(lvl6, (350, 200))
        lvl7 = pygame.transform.scale(lvl7, (350, 200))
        screen.blit(background, (0, 0))
        screen.blit(lvl1, (160, 270))
        screen.blit(lvl2, (570, 270))
        screen.blit(lvl3, (980, 270))
        screen.blit(lvl4, (1390, 270))
        screen.blit(lvl5, (160, 530))
        screen.blit(lvl6, (570, 530))
        screen.blit(lvl7, (980, 530))
        screen.blit(font.render("Выберите уровень", True, (255, 255, 255)), (665, 80))
        screen.blit(font1.render("Последнее сохранение", True, (255, 255, 255)), (670, 790))
        screen.blit(font1.render("Выход в главное меню", True, (255, 255, 255)), (670, 940))
        pygame.display.update()
main_menu()
