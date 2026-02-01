import pygame
import time
import random

# 定义一些常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 定义蛇和食物的初始位置
snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, SCREEN_WIDTH//BLOCK_SIZE)*BLOCK_SIZE, random.randrange(1, SCREEN_HEIGHT//BLOCK_SIZE)*BLOCK_SIZE]
food_spawn = True

# 定义方向
direction = 'RIGHT'
change_to = direction

    
# 定义颜色
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0,255,0)
BLUE = (50, 153, 213)

# 游戏循环
while True:
    # 检查按键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.K_ESCAPE:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # 确保蛇不能向相反的方向移动
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # 移动蛇
    if direction == 'UP':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] - BLOCK_SIZE) % SCREEN_HEIGHT])
    if direction == 'DOWN':
        snake_pos.insert(0, [snake_pos[0][0], (snake_pos[0][1] + BLOCK_SIZE) % SCREEN_HEIGHT])
    if direction == 'LEFT':
        snake_pos.insert(0, [(snake_pos[0][0] - BLOCK_SIZE) % SCREEN_WIDTH, snake_pos[0][1]])
    if direction == 'RIGHT':
        snake_pos.insert(0, [(snake_pos[0][0] + BLOCK_SIZE) % SCREEN_WIDTH, snake_pos[0][1]])

    # 游戏结束条件
    # 删除原有的游戏结束条件

    # 蛇吃食物,只要蛇头与食物的距离小于20
    if abs(snake_pos[0][0] - food_pos[0]) < 20 and abs(snake_pos[0][1] - food_pos[1]) < 20:
        food_spawn = False
    else:
        snake_pos.pop()

    # 生成新的食物
    if not food_spawn:
        food_pos = [random.randrange(1, SCREEN_WIDTH//BLOCK_SIZE)*BLOCK_SIZE, random.randrange(1, SCREEN_HEIGHT//BLOCK_SIZE)*BLOCK_SIZE]
    food_spawn = True


    # 刷新屏幕
    screen.fill(WHITE)
    for pos in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

    # 控制游戏速度
    pygame.time.Clock().tick(30)
    

