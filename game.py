import pygame, sys, time, random
from pygame.math import Vector2


pygame.init()
pygame.mixer.init()
class Stats():
    def __init__(self):
        self.upgradeslist = []
        self.upgradecodelist = []
        with open("asset/Upgrades.txt", "r") as upgradetext:
            line = upgradetext.readlines()
            for i in line:
                i = i.replace("\n", "")
                splittext = i.split(":")
                self.upgradeslist.append(splittext[1])
        with open("asset/Upgradecode.txt", "r") as upgradecode:
            linecode = upgradecode.readlines()
            for j in linecode:
                j = j.replace("\n", "")
                splitcode = j.split(":")
                self.upgradecodelist.append(splitcode[1])
        with open("asset/Coin.txt", "r") as Coin:
            self.Coins = Coin.readline()
class Snake1():
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10)]
        self.direction = Vector2(1, 0)
        self.new = False
        self.headup = pygame.image.load("asset/Snake head up.png")
        self.headright = pygame.image.load("asset/Snake head right.png")
        self.headleft = pygame.image.load("asset/Snake head left.png")
        self.headdown = pygame.image.load("asset/Snake head down.png")
        self.bodyy = pygame.image.load("asset/Snake body y.png")
        self.bodyx = pygame.image.load("asset/Snake body x.png")
        self.tailup = pygame.image.load("asset/Snake tail up.png")
        self.tailright = pygame.image.load("asset/Snake tail right.png")
        self.tailleft = pygame.image.load("asset/Snake tail left.png")
        self.taildown = pygame.image.load("asset/Snake tail down.png")
        self.connectleftup = pygame.image.load("asset/Snake body connect left up.png")
        self.connectupright = pygame.image.load("asset/Snake body connect up right.png")
        self.connectrightdown = pygame.image.load("asset/Snake body connect right down.png")
        self.connectdownleft = pygame.image.load("asset/Snake body connect down left.png")
    def drawbody(self):
        self.headimage()
        self.tailimage()
        for index,block in enumerate(self.body):
            posx = int(block.x*size)
            posy = int(block.y*size)
            body_rect = pygame.Rect(posx,posy, size, size)
            if index == 0:
                screen.blit(self.head, body_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, body_rect)
            else:
                previous = self.body[index+1] - block
                nextblock = self.body[index-1] - block
                if previous.x == nextblock.x:
                    screen.blit(self.bodyx, body_rect)
                elif previous.y == nextblock.y:
                    screen.blit(self.bodyy, body_rect)
                else:
                    if previous.x == -1 and nextblock.y == -1 or previous.y == -1 and nextblock.x == -1:
                        screen.blit(self.connectleftup, body_rect)
                    elif previous.y == -1 and nextblock.x == 1 or previous.x == 1 and nextblock.y == -1:
                        screen.blit(self.connectupright, body_rect)
                    elif previous.x == 1 and nextblock.y == 1 or previous.y == 1 and nextblock.x == 1:
                        screen.blit(self.connectrightdown, body_rect)
                    elif previous.y == 1 and nextblock.x == -1 or previous.x == -1 and nextblock.y == 1:
                        screen.blit(self.connectdownleft, body_rect)
    def movesnake(self):
        if self.new and self.length > 2:
            copy = self.body[:]
            copy.insert(0,copy[0] + self.direction)
            self.body = copy[:]
            self.new = False
        else:
            copy = self.body[:-1]
            copy.insert(0,copy[0] + self.direction)
            self.body = copy[:]
    def addbody(self):
        self.new = True
    def lengthlimit(self):
        self.length = 0
    def headimage(self):
        headvector = self.body[1] - self.body[0]
        if headvector == Vector2(1,0):
            self.head = self.headleft
        elif headvector == Vector2(-1,0):
            self.head = self.headright
        elif headvector == Vector2(0,1):
            self.head = self.headup
        elif headvector == Vector2(0,-1):
            self.head = self.headdown
    def tailimage(self):
        tailvector = self.body[-2] - self.body[-1]
        if tailvector == Vector2(1,0):
            self.tail = self.tailright
        elif tailvector == Vector2(-1,0):
            self.tail = self.tailleft
        elif tailvector == Vector2(0,1):
            self.tail = self.taildown
        elif tailvector == Vector2(0,-1):
            self.tail = self.tailup
class Snake2():
    def __init__(self):
        self.body = [Vector2(15, 10), Vector2(16, 10)]
        self.direction = Vector2(-1, 0)
        self.new = False
        self.headup = pygame.image.load("asset/Snake head up.png")
        self.headright = pygame.image.load("asset/Snake head right.png")
        self.headleft = pygame.image.load("asset/Snake head left.png")
        self.headdown = pygame.image.load("asset/Snake head down.png")
        self.bodyy = pygame.image.load("asset/Snake body y.png")
        self.bodyx = pygame.image.load("asset/Snake body x.png")
        self.tailup = pygame.image.load("asset/Snake tail up.png")
        self.tailright = pygame.image.load("asset/Snake tail right.png")
        self.tailleft = pygame.image.load("asset/Snake tail left.png")
        self.taildown = pygame.image.load("asset/Snake tail down.png")
        self.connectleftup = pygame.image.load("asset/Snake body connect left up.png")
        self.connectupright = pygame.image.load("asset/Snake body connect up right.png")
        self.connectrightdown = pygame.image.load("asset/Snake body connect right down.png")
        self.connectdownleft = pygame.image.load("asset/Snake body connect down left.png")
    def drawbody(self):
        self.headimage()
        self.tailimage()
        for index,block in enumerate(self.body):
            posx = int(block.x*size)
            posy = int(block.y*size)
            body_rect = pygame.Rect(posx,posy, size, size)
            if index == 0:
                screen.blit(self.head, body_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, body_rect)
            else:
                previous = self.body[index+1] - block
                nextblock = self.body[index-1] - block
                if previous.x == nextblock.x:
                    screen.blit(self.bodyx, body_rect)
                elif previous.y == nextblock.y:
                    screen.blit(self.bodyy, body_rect)
                else:
                    if previous.x == -1 and nextblock.y == -1 or previous.y == -1 and nextblock.x == -1:
                        screen.blit(self.connectleftup, body_rect)
                    elif previous.y == -1 and nextblock.x == 1 or previous.x == 1 and nextblock.y == -1:
                        screen.blit(self.connectupright, body_rect)
                    elif previous.x == 1 and nextblock.y == 1 or previous.y == 1 and nextblock.x == 1:
                        screen.blit(self.connectrightdown, body_rect)
                    elif previous.y == 1 and nextblock.x == -1 or previous.x == -1 and nextblock.y == 1:
                        screen.blit(self.connectdownleft, body_rect)
    def movesnake(self):
        if self.new and self.length > 2:
            copy = self.body[:]
            copy.insert(0,copy[0] + self.direction)
            self.body = copy[:]
            self.new = False
        else:
            copy = self.body[:-1]
            copy.insert(0,copy[0] + self.direction)
            self.body = copy[:]
    def addbody(self):
        self.new = True
    def lengthlimit(self):
        self.length = 0
    def headimage(self):
        headvector = self.body[1] - self.body[0]
        if headvector == Vector2(1,0):
            self.head = self.headleft
        elif headvector == Vector2(-1,0):
            self.head = self.headright
        elif headvector == Vector2(0,1):
            self.head = self.headup
        elif headvector == Vector2(0,-1):
            self.head = self.headdown
    def tailimage(self):
        tailvector = self.body[-2] - self.body[-1]
        if tailvector == Vector2(1,0):
            self.tail = self.tailright
        elif tailvector == Vector2(-1,0):
            self.tail = self.tailleft
        elif tailvector == Vector2(0,1):
            self.tail = self.taildown
        elif tailvector == Vector2(0,-1):
            self.tail = self.tailup
class Timer():
    def __init__(self):
        self.time = 120
    def countdown(self):
        self.time -= 1
class Word():
    def __init__(self):
        self.x = random.randint(0, number)
        self.y = random.randint(0, number)
        self.pos = Vector2(self.x, self.y)
        posword.append(self.pos)
    def drawword(self):
        word_rect = pygame.Rect(int(self.pos.x * size),int(self.pos.y * size),size,size)
        word_list.append(word_rect)
        chancevowelalpha = random.randint(1, 2)
        if chancevowelalpha == 1:
            letters = {1:"A", 2:"E", 3:"O", 4:"U", 5:"I"}
            self.letter = letters[random.randint(1, 5)]
        elif chancevowelalpha == 2:
            chancealpha = random.randint(1,15)
            if chancealpha in [1,2,3,4,5]:
                letters = {1:"L", 2:"N", 3:"R", 4:"S", 5:"T"}
                self.letter = letters[random.randint(1, 5)]
            elif chancealpha in [6,7,8,9]:
                letters = {1:"B", 2:"D", 3:"G"}
                self.letter = letters[random.randint(1, 3)]
            elif chancealpha in [10,11,12]:
                letters = {1:"C", 2:"M", 3:"P"}
                self.letter = letters[random.randint(1, 3)]
            elif chancealpha in [13,14]:
                letters = {1:"F", 2:"H", 3:"V", 4:"W", 5:"Y"}
                self.letter = letters[random.randint(1, 5)]
            elif chancealpha == 15:
                letters = {1:"J", 2:"X", 3:"K", 4:"Z", 5:"Q"}
                self.letter = letters[random.randint(1, 5)]
        lett = pygame.image.load(f"asset/word_rect/{self.letter}.png")
        word_list2.append(lett)
        word_list3.append(self.letter)
        self.__init__()
    def drawlist(self):
        p = 0
        for i in word_list:
            pygame.draw.rect(screen,RED,i)
        for l in word_list2:
            try:
                screen.blit(l, word_list[p])
                p += 1
            except IndexError:
                p = 0
    def createwordcheck(self):
        self.wordcheck = ""
        self.wordspawning = 0
class Word2():
    def __init__(self):
        self.x = random.randint(0, number)
        self.y = random.randint(0, number)
        self.pos = Vector2(self.x, self.y)
        posword.append(self.pos)
    def drawword(self):
        word_rect = pygame.Rect(int(self.pos.x * size),int(self.pos.y * size),size,size)
        word_list.append(word_rect)
        chancevowelalpha = random.randint(1, 2)
        if chancevowelalpha == 1:
            letters = {1:"A", 2:"E", 3:"O", 4:"U", 5:"I"}
            self.letter = letters[random.randint(1, 5)]
        elif chancevowelalpha == 2:
            chancealpha = random.randint(1,15)
            if chancealpha in [1,2,3,4,5]:
                letters = {1:"L", 2:"N", 3:"R", 4:"S", 5:"T"}
                self.letter = letters[random.randint(1, 5)]
            elif chancealpha in [6,7,8,9]:
                letters = {1:"B", 2:"D", 3:"G"}
                self.letter = letters[random.randint(1, 3)]
            elif chancealpha in [10,11,12]:
                letters = {1:"C", 2:"M", 3:"P"}
                self.letter = letters[random.randint(1, 3)]
            elif chancealpha in [13,14]:
                letters = {1:"F", 2:"H", 3:"V", 4:"W", 5:"Y"}
                self.letter = letters[random.randint(1, 5)]
            elif chancealpha == 15:
                letters = {1:"J", 2:"X", 3:"K", 4:"Z", 5:"Q"}
                self.letter = letters[random.randint(1, 5)]
        lett = pygame.image.load(f"asset/word_rect/{self.letter}.png")
        word_list2.append(lett)
        word_list3.append(self.letter)
        self.__init__()
    def drawlist(self):
        p = 0
        for i in word_list:
            pygame.draw.rect(screen,RED,i)
        for l in word_list2:
            try:
                screen.blit(l, word_list[p])
                p += 1
            except IndexError:
                p = 0
    def createwordcheck(self):
        self.wordcheck = ""
        self.wordcheck2 = ""
        self.wordspawning = 0
class obstacle():
    def __init__(self):
        self.x = random.randint(1, number-1)
        self.y = random.randint(1, number-1)
        self.pos = [Vector2(2,2), Vector2(17,2), Vector2(2,17), Vector2(17,17), Vector2(10,17), Vector2(10,2), Vector2(6,5), Vector2(6,15), Vector2(14,5), Vector2(14,15), Vector2(3, 10), Vector2(16, 10), Vector2(8,8), Vector2(12,12), Vector2(8,12), Vector2(12,8)]
        for i in self.pos:
            posobstacles.append(i)
    def createobstacles(self):
        self.obstaclespic1 = pygame.image.load("asset/obstacle1.png")
        self.obstaclespic2 = pygame.image.load("asset/obstacle2.png")
        for poses in self.pos:
            obstacle1 = pygame.Rect(int(poses.x * size),int(poses.y * size),size,size)
            obstacles_list1.append(obstacle1)
            self.__init__()
    def drawobtstacles(self):
        for i in obstacles_list1:
            pygame.draw.rect(screen, RED, i)
            screen.blit(self.obstaclespic1, i)
class Maingame1():
    def __init__(self):
        self.snake = Snake1()
        self.word = Word()
        self.obstacles = obstacle()
        self.timer = Timer()
        self.point = 0
        self.lengthlimit = int(stats.upgradeslist[0])
        self.health = int(stats.upgradeslist[1])
        self.death = False
    def update(self):
        if self.death == False:
            self.snake.movesnake()
            self.collision()
            self.fail()
            if self.timer.time == 0:
                self.gameover()
    def elements(self):
        self.word.drawlist()
        self.snake.drawbody()
        self.obstacles.drawobtstacles()
    def collision(self):
        for i in range(len(posword)):
            try:
                if self.snake.body[0] == posword[i] and self.snake.length < self.lengthlimit:
                    pickupsound.play()
                    word_list.remove(word_list[i])
                    word_list2.remove(word_list2[i])
                    posword.remove(posword[i])
                    self.word.wordcheck += word_list3[i]
                    word_list3.remove(word_list3[i])
                    self.snake.length += 1
                    print(self.word.wordcheck)
                    self.snake.addbody()
                    self.word.wordspawning -= 1
                elif posword[i] in posobstacles:
                    word_list.remove(word_list[i])
                    word_list2.remove(word_list2[i])
                    posword.remove(posword[i])
                    word_list3.remove(word_list3[i])
                    self.word.wordspawning -= 1
            except IndexError:
                pass
    def Score(self):
        self.read = []
        self.score = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,'Y': 4, 'Z': 10}
        file = open("asset/Letters.txt", "r")
        read = file.read()
        splitted = read.split()
        for i in splitted:
            if self.word.wordcheck == i.upper():
                for j in self.word.wordcheck:
                    self.point += self.score[j]
        self.word.wordcheck = ""
        self.snake.length = 0
    def showscore(self):
        self.font = get_font(30)
        self.showscores = self.font.render("SCORE:" + str(self.point), True, "#d7fcd4")
        screen.blit(self.showscores, Vector2(5, 15))
    def showword(self):
        self.showwords = ""
        u = 0
        for i in range(self.lengthlimit):
            self.showwords += "_"
        for i in self.word.wordcheck:
            if u < self.lengthlimit:
                self.showwords = self.showwords.replace(self.showwords[u], i, 1)
                u += 1
            else:
                pass
        self.showletter = self.font.render(str(self.showwords), True, RED)
        screen.blit(self.showletter, (580,10))
    def showtimer(self):
        self.font = get_font(40)
        self.showtime = str(self.timer.time)
        self.showtimers = self.font.render(self.showtime, True, "#d7fcd4")
        screen.blit(self.showtimers, (400,10))
    def fail(self):
        if not 0 <= self.snake.body[0].x < number or not 0 <= self.snake.body[0].y < number:
            print("out of bound")
            self.health -= 1
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                print("selfcollision")
                self.health -= 1
        if self.snake.body[0] in posobstacles:
            print("obstaclecollision")
            self.health -= 1
        if self.health == 0:
            self.gameover()
    def gameover(self):
        self.coin = ((self.point//10) * int(stats.upgradeslist[2])) * int(stats.upgradeslist[3]) + int(stats.Coins)
        gameoversound.play()
        print("gameover")
        pygame.time.wait(1000)
        with open("asset/Coin.txt", "w") as newcoin:
            newcoin.write(str(self.coin))
        self.death = True
class Maingame2():
    def __init__(self):
        self.snake = Snake1()
        self.snake2 = Snake2()
        self.word = Word2()
        self.timer = Timer()
        self.obstacles = obstacle()
        self.point = 0
        self.point2 = 0
        self.lengthlimit = int(stats.upgradeslist[0])
        self.health = int(stats.upgradeslist[1])
        self.death = False
    def update(self):
        if self.death == False:
            self.snake.movesnake()
            self.snake2.movesnake()
            self.collision()
            self.fail()
            if self.timer.time == 0:
                self.gameover()
    def elements(self):
        self.word.drawlist()
        self.snake.drawbody()
        self.snake2.drawbody()
        self.obstacles.drawobtstacles()
    def collision(self):
        for i in range(len(posword)):
            try:
                if self.snake.body[0] == posword[i] and self.snake.length < self.lengthlimit:
                    pickupsound.play()
                    word_list.remove(word_list[i])
                    word_list2.remove(word_list2[i])
                    posword.remove(posword[i])
                    self.word.wordcheck += word_list3[i]
                    word_list3.remove(word_list3[i])
                    self.snake.length += 1
                    print(self.word.wordcheck)
                    self.snake.addbody()
                    self.word.wordspawning -= 1
                elif self.snake2.body[0] == posword[i] and self.snake2.length < self.lengthlimit:
                    word_list.remove(word_list[i])
                    word_list2.remove(word_list2[i])
                    posword.remove(posword[i])
                    self.word.wordcheck2 += word_list3[i]
                    word_list3.remove(word_list3[i])
                    self.snake2.length += 1
                    print(self.word.wordcheck)
                    self.snake2.addbody()
                    self.word.wordspawning -= 1
                elif posword[i] in posobstacles:
                    word_list.remove(word_list[i])
                    word_list2.remove(word_list2[i])
                    posword.remove(posword[i])
                    word_list3.remove(word_list3[i])
                    self.word.wordspawning -= 1
            except IndexError:
                pass
    def Score(self):
        self.read = []
        self.score = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,'Y': 4, 'Z': 10}
        file = open("asset/Letters.txt", "r")
        read = file.read()
        splitted = read.split()
        for i in splitted:
            if self.word.wordcheck == i.upper():
                for j in self.word.wordcheck:
                    self.point += self.score[j]
        self.word.wordcheck = ""
        self.snake.length = 0
    def Score2(self):
        self.read = []
        self.score2 = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4,'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3,'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,'Y': 4, 'Z': 10}
        file = open("asset/Letters.txt", "r")
        read = file.read()
        splitted = read.split()
        for i in splitted:
            if self.word.wordcheck2 == i.upper():
                for j in self.word.wordcheck2:
                    self.point2 += self.score2[j]
        self.word.wordcheck2 = ""
        self.snake2.length = 0
    def showplayer1(self):
        self.font = get_font(30)
        self.showplayerone = self.font.render("PLAYER1", True, BLACK)
        screen.blit(self.showplayerone, Vector2(5, 15))
    def showplayer2(self):
        self.font = get_font(30)
        self.showplayertwo = self.font.render("PLAYER2", True, BLACK)
        screen.blit(self.showplayertwo, Vector2(530, 15))
    def showscore(self):
        self.font = get_font(30)
        self.showscores = self.font.render("SCORE:" + str(self.point), True, BLUE)
        screen.blit(self.showscores, Vector2(5, 70))
    def showscore2(self):
        self.font = get_font(30)
        self.showscores2 = self.font.render("SCORE:" + str(self.point2), True, RED)
        screen.blit(self.showscores2, Vector2(530, 70))
    def showtimer(self):
        self.font = get_font(40)
        self.showtime = str(self.timer.time)
        self.showtimers = self.font.render(self.showtime, True, "#d7fcd4")
        screen.blit(self.showtimers, (350,10))
    def showword(self):
        self.showwords = ""
        u = 0
        for i in range(self.lengthlimit):
            self.showwords += "_"
        for i in self.word.wordcheck:
            if u < self.lengthlimit:
                self.showwords = self.showwords.replace(self.showwords[u], i, 1)
                u += 1
            else:
                pass
        self.showletter = self.font.render(str(self.showwords), True, RED)
        screen.blit(self.showletter, (10,110))
    def showword2(self):
        self.showwords2 = ""
        u = 0
        for i in range(self.lengthlimit):
            self.showwords2 += "_"
        for i in self.word.wordcheck2:
            if u < self.lengthlimit:
                self.showwords2 = self.showwords2.replace(self.showwords2[u], i, 1)
                u += 1
            else:
                pass
        self.showletter = self.font.render(str(self.showwords2), True, RED)
        screen.blit(self.showletter, (530,110))
    def fail(self):
        if not 0 <= self.snake.body[0].x < number or not 0 <= self.snake.body[0].y < number:
            self.health -= 1
        elif not 0 <= self.snake2.body[0].x < number or not 0 <= self.snake2.body[0].y < number:
            self.health -= 1
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.health -= 1
        for block2 in self.snake2.body[1:]:
            if block2 == self.snake2.body[0]:
                self.health -= 1
        if self.snake.body[0] in posobstacles:
            self.health -= 1
        elif self.snake2.body[0] in posobstacles:
            self.health -= 1
        if self.health == 0:
            self.gameover()
    def gameover(self):
        self.coin = ((self.point//10) * int(stats.upgradeslist[2])) * int(stats.upgradeslist[3]) + int(stats.Coins)
        gameoversound.play()
        pygame.time.wait(1000)
        with open("asset/Coin.txt", "w") as newcoin:
            newcoin.write(str(self.coin))
        self.death = True
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
def get_font(size):
    return pygame.font.Font("asset/font.ttf", size)
background = pygame.image.load("asset/background1.png")
background2 = pygame.image.load("asset/shop.png")
playgrid = pygame.image.load("asset/Play grid.png")
noupgrade = pygame.image.load("asset/No upgrade.png")
upgraded = pygame.image.load("asset/Upgraded.png")
upgradebutton = pygame.image.load("asset/Upgrade button.png")
upgrademenu = pygame.image.load("asset/Upgrade menu.png")
coinpic = pygame.image.load("asset/Price.png")
pickupsound = pygame.mixer.Sound("asset/Pickup sound.mp3")
gameoversound = pygame.mixer.Sound("asset/gameover.mp3")
pygame.mixer.music.load("asset/Melody.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
font = pygame.font.SysFont("Roboto", 10)
screenupdate = pygame.USEREVENT
pygame.time.set_timer(screenupdate, 150)
GREEN = (175, 215, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0 , 0 , 0 , 150)
size = 40
number = 20
screen = pygame.display.set_mode((number * size, number * size))
clock = pygame.time.Clock()
surface = pygame.Surface((100, 200))
posword = []
word_list = []
word_list2 = []
word_list3 = []
obstacles_list1 = []
obstacles_list2 = []
obstacles_list3 = []
posobstacles = []
bodylist = []
stats = Stats()
def gamemode():
    while True:
        screen.blit(background, (0, 0))

        menumouse = pygame.mouse.get_pos()
        singleplayerbutton = Button(image=None, pos=(400, 250), 
                            text_input="Singleplayer", font=get_font(60), base_color="#d7fcd4", hovering_color=RED)
        versusbutton = Button(image=None, pos=(400, 370), 
                            text_input="1v1", font=get_font(60), base_color="#d7fcd4", hovering_color=RED)
        backbutton = Button(image=None, pos=(400, 490), 
                                text_input="BACK", font=get_font(60), base_color="#d7fcd4", hovering_color=RED)
        for button in [singleplayerbutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [versusbutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [backbutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if singleplayerbutton.checkForInput(menumouse):
                    life = True
                    singleplayer(life)
                if versusbutton.checkForInput(menumouse):
                    life = True
                    versus(life)
                if backbutton.checkForInput(menumouse):
                    main_menu()
            pygame.display.update()
def singleplayer(life):
    i = 0
    p = 0
    t = 0
    maingame = Maingame1()
    while True:
        screen.blit(playgrid, (0, 0))
        if i == 90 and maingame.word.wordspawning < 16 and maingame.death == False:
            maingame.word.drawword()
            i = 0
            maingame.word.wordspawning += 1
        elif i == 90 and maingame.word.wordspawning == 16:
            i = 0
        if t == 0:
            maingame.obstacles.createobstacles()
            maingame.word.createwordcheck()
            maingame.snake.lengthlimit()
            t += 1
        if p == 60 and maingame.timer.time > 0 and maingame.death == False:
            maingame.timer.countdown()
            p = 0
        maingame.elements()
        maingame.showscore()
        maingame.showword()
        maingame.showtimer()
        pygame.display.update()
        clock.tick(60)
        i += 1
        t += 1
        p += 1
        if maingame.death == True:
            maingame.word.wordspawning = 0
            word_list.clear()
            word_list2.clear()
            word_list3.clear()
            posword.clear()
            menumouse = pygame.mouse.get_pos()
            font = get_font(40)
            Playagain = font.render("PLAY AGAIN?", True, "#d7fcd4")
            screen.blit(Playagain, (200,300))
            screen.blit(maingame.showscores, (300,400))
            Yesbutton = Button(image=None, pos=(400, 500), 
                                text_input="YES", font=get_font(40), base_color="#d7fcd4", hovering_color=RED)
            Nobutton = Button(image=None, pos=(400, 600), 
                                text_input="No", font=get_font(40), base_color="#d7fcd4", hovering_color=RED)
            for button in [Yesbutton]:
                button.changeColor(menumouse)
                button.update(screen)
            for button in [Nobutton]:
                button.changeColor(menumouse)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Yesbutton.checkForInput(menumouse):
                        life = True
                        singleplayer(life)
                        print(word_list)
                        print(word_list2)
                        print(word_list3)
                    if Nobutton.checkForInput(menumouse):
                        main_menu()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == screenupdate:
                maingame.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and maingame.snake.direction != Vector2(0, 1):
                    maingame.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_s and maingame.snake.direction != Vector2(0, -1):
                    maingame.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_a and maingame.snake.direction != Vector2(1, 0):
                    maingame.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_d and maingame.snake.direction != Vector2(-1, 0):
                    maingame.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_RETURN:
                    maingame.snake.body = [maingame.snake.body[0], maingame.snake.body[1]]
                    maingame.Score()
def versus(life):
    i = 0
    p = 0
    t = 0
    maingame2 = Maingame2()
    while True:
        screen.blit(playgrid, (0, 0))
        if i == 150 and maingame2.word.wordspawning < 16 and maingame2.death == False:
            maingame2.word.drawword()
            i = 0
            maingame2.word.wordspawning += 1
        elif i == 150 and maingame2.word.wordspawning == 16:
            i = 0
        if t == 0:
            maingame2.obstacles.createobstacles()
            maingame2.word.createwordcheck()
            maingame2.snake.lengthlimit()
            maingame2.snake2.lengthlimit()
            t += 1
        if p == 60 and maingame2.timer.time > 0  and maingame2.death == False:
            maingame2.timer.countdown()
            p = 0
        maingame2.elements()
        maingame2.showtimer()
        maingame2.showscore()
        maingame2.showscore2()
        maingame2.showplayer1()
        maingame2.showplayer2()
        maingame2.showword()
        maingame2.showword2()
        pygame.display.update()
        clock.tick(60)
        i += 1
        t += 1
        p += 1
        if maingame2.death == True:
            maingame2.word.wordspawning = 0
            word_list.clear()
            word_list2.clear()
            word_list3.clear()
            posword.clear()
            menumouse = pygame.mouse.get_pos()
            font = get_font(40)
            Playagain = font.render("PLAY AGAIN?", True, "#d7fcd4")
            screen.blit(Playagain, (200,300))
            screen.blit(maingame2.showscores, (300,370))
            screen.blit(maingame2.showscores2, (300,420))
            Yesbutton = Button(image=None, pos=(400, 500), 
                                text_input="YES", font=get_font(40), base_color="#d7fcd4", hovering_color=RED)
            Nobutton = Button(image=None, pos=(400, 600), 
                                text_input="No", font=get_font(40), base_color="#d7fcd4", hovering_color=RED)
            for button in [Yesbutton]:
                button.changeColor(menumouse)
                button.update(screen)
            for button in [Nobutton]:
                button.changeColor(menumouse)
                button.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Yesbutton.checkForInput(menumouse):
                        life = True
                        versus(life)
                    if Nobutton.checkForInput(menumouse):
                        main_menu()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == screenupdate:
                maingame2.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and maingame2.snake.direction != Vector2(0, 1):
                    maingame2.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_s and maingame2.snake.direction != Vector2(0, -1):
                    maingame2.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_a and maingame2.snake.direction != Vector2(1, 0):
                    maingame2.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_d and maingame2.snake.direction != Vector2(-1, 0):
                    maingame2.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_RETURN:
                    maingame2.snake.body = [maingame2.snake.body[0], maingame2.snake.body[1]]
                    maingame2.Score()
                if event.key == pygame.K_UP and maingame2.snake2.direction != Vector2(0, 1):
                    maingame2.snake2.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and maingame2.snake2.direction != Vector2(0, -1):
                    maingame2.snake2.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT and maingame2.snake2.direction != Vector2(1, 0):
                    maingame2.snake2.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT and maingame2.snake2.direction != Vector2(-1, 0):
                    maingame2.snake2.direction = Vector2(1, 0)
                if event.key == pygame.K_RSHIFT:
                    maingame2.snake2.body = [maingame2.snake2.body[0], maingame2.snake2.body[1]]
                    maingame2.Score2()
def upgrade():
    lengthcode = str(stats.upgradecodelist[0])
    healthcode = str(stats.upgradecodelist[1])
    multicode = str(stats.upgradecodelist[2])
    coinmulticode = str(stats.upgradecodelist[3])
    length = int(stats.upgradeslist[0])
    health = int(stats.upgradeslist[1])
    multiplier = int(stats.upgradeslist[2])
    coinmul = int(stats.upgradeslist[3])
    playercoinx = 720 - (20 * len(str(stats.Coins)))
    lengthprice = 200 * (length - 4)
    healthprice = 150 * (health)
    multiprice = 50 * (multiplier)
    coinmulprice = 50 * (coinmul)
    playercoin = int(stats.Coins)
    while True:
        lengthx = 430
        healthx = 430
        multix = 430
        coinmutlix = 430
        screen.blit(background2, (0, 0))
        screen.blit(upgrademenu, (100, 220))
        amountfont = get_font(30)
        showplayercoin = amountfont.render(str(playercoin), True, BLACK)
        screen.blit(showplayercoin, (playercoinx, 15))
        screen.blit(coinpic, (740, 0))
        file = open("asset/Upgrades.txt", "r")
        read = file.read()
        splitted = read.split()
        if lengthprice <= 400:
            lengthpricepic = pygame.image.load(f"asset/{lengthprice}.png")
        else:
            lengthpricepic = pygame.image.load("asset/Max.png")
        if healthprice <= 300:
            healthpricepic = pygame.image.load(f"asset/{healthprice}.png")
        else:
            healthpricepic = pygame.image.load("asset/Max.png")
        if multiprice <= 200:
            multipricepic = pygame.image.load(f"asset/{multiprice}.png")
        else:
            multipricepic = pygame.image.load("asset/Max.png")
        if coinmulprice <= 200:
            coinmulpricepic = pygame.image.load(f"asset/{coinmulprice}.png")
        else:
            coinmulpricepic = pygame.image.load("asset/Max.png")
        screen.blit(lengthpricepic, (500, 480))
        screen.blit(healthpricepic, (500, 560))
        screen.blit(multipricepic, (500, 640))
        screen.blit(coinmulpricepic, (500, 720))
        screen.blit(coinpic, (540, 470))
        screen.blit(coinpic, (540, 550))
        screen.blit(coinpic, (540, 630))
        screen.blit(coinpic, (540, 710))
        for i in lengthcode:
            if i == "0":
                screen.blit(noupgrade, (lengthx, 470))
            elif i == "1":
                screen.blit(upgraded, (lengthx, 470))
            lengthx -= 40
        for i in healthcode:
            if i == "0":
                screen.blit(noupgrade, (healthx, 550))
            elif i == "1":
                screen.blit(upgraded, (healthx, 550))
            healthx -= 40
        for i in multicode:
            if i == "0":
                screen.blit(noupgrade, (multix, 630))
            elif i == "1":
                screen.blit(upgraded, (multix, 630))
            multix -= 40
        for i in coinmulticode:
            if i == "0":
                screen.blit(noupgrade, (coinmutlix, 710))
            elif i == "1":
                screen.blit(upgraded, (coinmutlix, 710))
            coinmutlix -= 40
        menumouse = pygame.mouse.get_pos()
        lengthupgrade = Button(image=upgradebutton, pos=(620, 500), 
                                text_input=None, font=get_font(90), base_color="#d7fcd4", hovering_color=RED)
        healthupgrade = Button(image=upgradebutton, pos=(620, 580), 
                                text_input=None, font=get_font(90), base_color="#d7fcd4", hovering_color=RED)
        multiplierupgrade = Button(image=upgradebutton, pos=(620, 660), 
                                text_input=None, font=get_font(90), base_color="#d7fcd4", hovering_color=RED)
        coinmultiplierupgrade = Button(image=upgradebutton, pos=(620, 740), 
                                text_input=None, font=get_font(90), base_color="#d7fcd4", hovering_color=RED)
        backbutton = Button(image=None, pos=(70, 30), 
                                text_input="BACK", font=get_font(30), base_color=BLACK, hovering_color="#d7fcd4")
        for button in [lengthupgrade]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [healthupgrade]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [multiplierupgrade]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [coinmultiplierupgrade]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [backbutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lengthupgrade.checkForInput(menumouse) and length < 7 and playercoin >= lengthprice:
                    lengthcode = lengthcode.replace("0", "1", 1)
                    length += 1
                    playercoin -= lengthprice
                    lengthprice += 200
                if healthupgrade.checkForInput(menumouse) and health < 3 and playercoin >= healthprice:
                    healthcode = healthcode.replace("0", "1", 1)
                    health += 1
                    playercoin -= healthprice
                    healthprice += 100
                if multiplierupgrade.checkForInput(menumouse) and multiplier < 5 and playercoin >= multiprice:
                    multicode = multicode.replace("0", "1", 1)
                    multiplier += 1
                    playercoin -= multiprice
                    multiprice += 50
                if coinmultiplierupgrade.checkForInput(menumouse) and coinmul < 5 and playercoin >= coinmulprice:
                    coinmulticode = coinmulticode.replace("0", "1", 1)
                    coinmul += 1
                    playercoin -= coinmulprice
                    coinmulprice += 50
                if backbutton.checkForInput(menumouse):
                    main_menu()
        with open("asset/Upgrades.txt", "w") as newupgrade:
            newupgrade.write("Lengthupgrade:" + str(length) + "\n")
            newupgrade.write("Healthupgrade:" + str(health) + "\n")
            newupgrade.write("Multiplierupgrade:" + str(multiplier) + "\n")
            newupgrade.write("Coinupgrade:" + str(coinmul) + "\n")
        with open("asset/Upgradecode.txt", "w") as newupgradecode:
            newupgradecode.write("lengthcode:" + lengthcode + "\n")
            newupgradecode.write("healthcode:" + healthcode + "\n")
            newupgradecode.write("multicode:" + multicode + "\n")
            newupgradecode.write("coinmulticode:" + coinmulticode + "\n")
        with open("asset/Coin.txt", "w") as newcoin:
            newcoin.write(str(playercoin))
        pygame.display.update()
def main_menu():
    menubackground = background
    while True:
        screen.blit(menubackground, (0, 0))
        menumouse = pygame.mouse.get_pos()
        playbutton = Button(image=None, pos=(140, 250), 
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color=RED)
        upgradebutton = Button(image=None, pos=(225, 370), 
                            text_input="UPGRADE", font=get_font(60), base_color="#d7fcd4", hovering_color=RED)
        for button in [playbutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for button in [upgradebutton]:
            button.changeColor(menumouse)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.checkForInput(menumouse):
                    gamemode()
                if upgradebutton.checkForInput(menumouse):
                    upgrade()
        pygame.display.update()
main_menu()
