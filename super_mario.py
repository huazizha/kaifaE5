import pygame
import random

# 初始化Pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# 颜色
WHITE = (255, 255, 255)

# 超级玛丽尺寸
MARIO_WIDTH, MARIO_HEIGHT = 50, 50

# 初始化窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("超级玛丽")

# 超级玛丽类
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        super(Mario, self).__init__()
        self.image = pygame.Surface((MARIO_WIDTH, MARIO_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT - MARIO_HEIGHT
        self.vel_x = 0
        self.vel_y = 0
        self.jump_power = -10

    def update(self):
        self.vel_y += 1  # 添加重力
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0

        if keys[pygame.K_SPACE] and self.rect.bottom >= SCREEN_HEIGHT:
            self.vel_y = self.jump_power

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# 金币类
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 20)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
        self.rect.y = random.randint(50, SCREEN_HEIGHT - 50)

# 创建超级玛丽对象
mario = Mario()

# 创建金币组和敌人组
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# 添加超级玛丽到所有精灵组
all_sprites.add(mario)

# 生成一些金币
for i in range(10):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

# 生成一些敌人
for i in range(5):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新所有精灵
    all_sprites.update()

    # 碰撞检测
    hits_coins = pygame.sprite.spritecollide(mario, coins, True)
    for hit in hits_coins:
        print("收集到金币!")

    hits_enemies = pygame.sprite.spritecollide(mario, enemies, False)
    if hits_enemies:
        print("被敌人撞到，游戏结束!")
        running = False

    # 绘制背景
    screen.fill((0, 0, 0))

    # 绘制所有精灵
    all_sprites.draw(screen)

    # 刷新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
