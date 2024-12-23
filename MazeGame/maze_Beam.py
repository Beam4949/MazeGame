from pygame import *

window_width = 800
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption('A maze zing game')

bg = transform.scale(image.load('background.jpg'), (window_width, window_height))

class Character():
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed):
        self.filename = filename
        self.img = transform.scale(image.load(filename), (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def draw(self):
        #draw.rect(window, (255, 0, 0), self.rect)
        window.blit(self.img, (self.rect.x, self.rect.y))
        
class Enemy(Character):
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed, route_list):
        self.route_list = route_list
        self.route_id = 0
        self.ok_x = False
        self.ok_y = False
        super().__init__(filename, size_x, size_y, pos_x, pos_y, speed)
    def move(self):
        target_x, target_y = self.route_list[self.route_id]
        distance_x = abs(target_x - self.rect.x)
        distance_y = abs(target_y - self.rect.y)
        if self.rect.x < target_x:
            self.rect.x += min(self.speed, distance_x)
        elif self.rect.x > target_x:
            self.rect.x -= min(self.speed, distance_x)
        else:
            self.ok_x = True

        if self.rect.y < target_y:
            self.rect.y += min(self.speed, distance_y)
        elif self.rect.y > target_y:
            self.rect.y -= min(self.speed, distance_y)
        else:
            self.ok_y = True

        if self.ok_x and self.ok_y:
            self.route_id += 1
            if self.route_id == len(self.route_list):
                self.route_id = 0
            self.ok_x = False
            self.ok_y = False
class Wall(Enemy):
    def __init__(self, size_x, size_y, pos_x, pos_y):
        self.img = Surface((size_x, size_y))
        self.R = 255
        self.G = 0
        self.B = 0
        self.img.fill((self.R, self.G, self.B))
        self.size_x = size_x
        self.size_y = size_y
        self.rect = self.img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.route_list = [(pos_x, pos_y), (pos_x, pos_y + 20), (pos_x + 20, pos_y + 20), (pos_x + 20, pos_y)]
        self.route_id = 0
        self.ok_x = False
        self.ok_y = False
        self.speed = 100
        
        
wall_list = []
x = 0
y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 110, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 165, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 220, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 275, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 330, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 385, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 440, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 495, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 550, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 605, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 660, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 715, y))
    y += 55

y = 0
for i in range(10):
    wall_list.append(Wall(10, 10, 770, y))
    y += 55


enemy_list = []
route1 = [(100, 50), (111, 75), (300, 200), (400, 100), (123, 123), (100, 100), (435, 213), (750, 20)]
enemy_list.append(Enemy('cyborg.png', 25, 25, 600, 50, 10, route1))
route2 = [(100, 150), (222, 150), (200, 300), (550, 150), (234, 234), (100, 100), (534, 312), (750, 100)]
enemy_list.append(Enemy('cyborg.png', 50, 50, 500, 350, 10, route2))
route3 = [(100, 250), (333, 225), (300, 200), (400, 100), (345, 345), (100, 100), (435, 213), (750, 200)]
enemy_list.append(Enemy('cyborg.png', 75, 75, 400, 200, 10, route3))
route4 = [(100, 350), (444, 300), (200, 300), (550, 150), (234, 234), (100, 100), (534, 312), (750, 300)]
enemy_list.append(Enemy('cyborg.png', 100, 50, 500, 50, 10, route4))
route5 = [(100, 450), (555, 375), (300, 200), (400, 100), (123, 123), (100, 100), (435, 213), (750, 400)]
enemy_list.append(Enemy('cyborg.png', 50, 100, 600, 350, 10, route5))
route6 = [(725, 0), (100, 0)]
enemy_list.append(Enemy('car.png', 50, 30, 725, 0, 50, route6))
route7 = [(725, 100), (100, 100)]
enemy_list.append(Enemy('car.png', 50, 30, 725, 100, 50, route7))
route8 = [(725, 200), (100, 200)]
enemy_list.append(Enemy('car.png', 50, 30, 725, 200, 50, route8))
route9 = [(725, 300), (100, 300)]
enemy_list.append(Enemy('car.png', 50, 30, 725, 300, 50, route9))
route10 = [(725, 400), (100, 400)]
enemy_list.append(Enemy('car.png', 50, 30, 725, 400, 50, route10))


hero = Character('hero.png', 5, 5, 5, 5, 2)
hero.hp = 3
treasure = Character('treasure.png', 50, 50, 700, 400, 0)



font.init()
lose = font.SysFont(None, 100)
mixer.init()
mixer.music.load('jungles.ogg')
#mixer.music.play()

clock = time.Clock()
fps = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(fps)
    display.update()
    window.blit(bg, (0, 0))
    treasure.draw()
    hero.draw()
    for enemy in enemy_list:
        enemy.draw()
        enemy.move()
    for wall in wall_list:
        wall.draw()
        wall.move()
    hp_box = lose.render(str(hero.hp), True, (255, 0, 0))
    window.blit(hp_box, (20, 20))

    
    if finish == False:
        for enemy in enemy_list:
            isCollide = sprite.collide_rect(hero, enemy)
            if isCollide:
                print('you lose')
                effect = mixer.Sound('kick.ogg')
                effect.play()
                test = lose.render('you lose', True, (255, 0, 0))
                window.blit(test, (400, 250))
                hero.hp -= 1
                hero.rect.x = 5
                hero.rect.y = 5
        for wall in wall_list:
            isCollide = sprite.collide_rect(hero, wall)
            if isCollide:
                print('you hit the wall')
                effect = mixer.Sound('kick.ogg')
                effect.play()
                test = lose.render('you hit the wall', True, (255, 0, 0))
                window.blit(test, (400, 250))
                hero.hp -= 1
                hero.rect.x = 5
                hero.rect.y = 5
        if hero.hp <= 0:
            isWin = False
            finish = True
        isCollide = sprite.collide_rect(hero, treasure)
        if isCollide:
            print('you win')
            effect = mixer.Sound('money.ogg')
            effect.play()
            isWin = True
            finish = True
    
    

        keys = key.get_pressed()
        if (keys[K_w] and hero.rect.y > 0):
            hero.rect.y -= hero.speed
        if (keys[K_a] and hero.rect.x > 0):
            hero.rect.x -= hero.speed
        if (keys[K_s] and hero.rect.y < window_height - hero.size_y):
            hero.rect.y += hero.speed
        if (keys[K_d] and hero.rect.x < window_width - hero.size_x):
            hero.rect.x += hero.speed

    else:
        if isWin == False:
            test = lose.render('you lose', True, (255, 0, 0))
            window.blit(test, (200, 300))
        if isWin == True:
            test = lose.render('you win', True, (0, 255, 0))
            window.blit(test, (200, 300))