import pygame
import random
pygame.init()
score=0
win = pygame.display.set_mode((600, 600))
font1=pygame.font.SysFont('comicsans',50,True)
font2=pygame.font.SysFont('comicsans',50,True)

pygame.display.set_caption('Snake Game')
headImg = pygame.image.load('final_head.png')
bodyImg = pygame.image.load('final_body.png')
foodImg=pygame.image.load('final_food.png')

screenWidth = 600
clock = pygame.time.Clock()
playing=True

def redraw_window(body,food,score,playing):
    win.fill((255, 255, 255))
    if playing == False:
        text = font2.render('GAME OVER', 1, (0, 0, 0))
        win.blit(text, (200, 250))
        pygame.display.update()
        pygame.time.delay(10000)
        pygame.quit()
    text = font1.render('Score: ' + str(score), 1, (0, 0, 0))

    win.blit(text, (10, 10))
    win.blit(foodImg, (food.x, food.y))


    for i in range(len(body)):
        if i==0:
            win.blit(headImg, (body[i].x, body[i].y))
        else:
            win.blit(bodyImg,(body[i].x, body[i].y))



    pygame.display.update()

class SnakeBlock:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Snake:
    def __init__(self):
        self.body=[]

    def ate_food(self,head,food):
        if(head.x==food.x and head.y==food.y):
            return True
        return False

    def check_collision(self):
        head=self.body[0]

        for i in range(1,len(self.body)):
            if(head.x==self.body[i].x and head.y==self.body[i].y):
                return True

        return False


class Food:
    def __init__(self):
        self.x = round((random.randrange(0, 600 - 30) / 30)) * 30
        self.y = round((random.randrange(0, 600 - 30) / 30)) * 30


    def create_food(self):
        self.x=round((random.randrange(0,600-30)/30))*30
        self.y=round((random.randrange(0,600-30)/30))*30

food=Food()
food.create_food()
snake=Snake()
snake_head=SnakeBlock(300,300)
snake.body.append(snake_head)

x1_new=0
y1_new=0
going_left=False
going_right=False
going_up=False
going_down=False

while playing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False

    curr_head = snake.body[0]
    curr_tail=snake.body[len(snake.body)-1]
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and going_right==False:
        going_left = True
        going_up= False
        going_right = False
        going_down = False
        x1_new=-30
        y1_new=0

    elif keys[pygame.K_RIGHT] and going_left==False:
        going_right = True
        going_left = False
        going_up = False
        going_down = False
        x1_new=30
        y1_new=0

    elif keys[pygame.K_UP] and going_down==False:
        going_up=True
        going_down = False
        going_left = False
        going_right = False
        x1_new=0
        y1_new=-30

    elif keys[pygame.K_DOWN] and going_up==False:
        going_down = True
        going_left = False
        going_right = False
        going_up = False
        x1_new = 0
        y1_new = 30

    if(snake.ate_food(curr_head,food)==True):
        score+=1
        food.create_food()
        if(x1_new>0):
            new_block=SnakeBlock(curr_tail.x-30,curr_tail.y)

        elif(x1_new<0):
            new_block=SnakeBlock(curr_tail.x+30,curr_tail.y)

        elif (y1_new < 0):
            new_block = SnakeBlock(curr_tail.x, curr_tail.y+30)

        elif (y1_new > 0):
            new_block = SnakeBlock(curr_tail.x, curr_tail.y-30)

        snake.body.append(new_block)

    if snake.check_collision():
        playing=False

    if curr_head.x<=0 or curr_head.y<=0 or curr_head.x+30 >= 600 or curr_head.y+30 >= 600:
        playing=False

    new_x=curr_head.x+x1_new
    new_y=curr_head.y+y1_new

    new_block=SnakeBlock(new_x,new_y)
    snake.body.pop(len(snake.body) - 1)
    snake.body.insert(0,new_block)

    redraw_window(snake.body,food,score,playing)
    clock.tick(8)

pygame.quit()