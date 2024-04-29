from turtle import *
import random

class Platform(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.goto(x,y)
        self.shape("platform.gif")
        self.st()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.speed(0)
        self.penup()
        self.color("red")
        self.shape("circle")
        self.st()
        self.count = 0
        self.alive = True
        screen.onkeypress(self.jump_left,"Left")
        screen.onkeypress(self.jump_right,"Right")
        screen.onkeypress(self.jump, "Up")

    def jump_left(self):
        self.setx(self.xcor()-15)
    
    def jump_right(self):
        self.setx(self.xcor()+15)

    def jump(self):
        global platforms
        if self.count<=100 and not self.is_blocked(platforms):
            self.sety(self.ycor()+10)
            self.count+=1
        else:
            while self.is_blocked(platforms):
                self.gravity()
    
    def gravity(self):
        self.sety(self.ycor()-10)
        

    def land(self,platform):
        pTop = self.ycor()+10
        pRight = self.xcor()+10
        pBottom = self.ycor()-10
        pLeft = self.xcor()-10

        lTop = platform.ycor()+10
        lRight = platform.xcor()+10
        lBottom = platform.ycor()-10
        lLeft = platform.xcor()-10

        if pBottom<=lTop and pLeft<lRight and pRight>lLeft and pTop>lBottom:
            return True
        else: 
            return False

    def has_landed(self,platforms):
        for platform in platforms:
            if self.land(platform):
                self.count = 0
                return True
        return False

    def block(self,platform):
        pTop = self.ycor()+10
        pRight = self.xcor()+10
        pBottom = self.ycor()-10
        pLeft = self.xcor()-10

        lTop = platform.ycor()+10
        lRight = platform.xcor()+10
        lBottom = platform.ycor()-10
        lLeft = platform.xcor()-10

        # jumping up through platform
        if pTop>lBottom and pLeft<lRight and pRight>lLeft and pBottom<lBottom:
            return True
        # jump right through platform
        # jump left through platform
        return False

    def is_blocked(self, platforms):
        for platform in platforms:
            if self.block(platform):
                return True
        return False
    
def generate_platforms():
    x=0
    for y in range(-300,400,50):
        deltax = random.choice([-70,70])
        x += deltax
        platforms.append(Platform(x,y))

def update():
    if player.alive:
        if not player.has_landed(platforms):
            player.gravity()
        if player.ycor()<-400:
            player.alive = False
        screen.ontimer(update,50)
    else:
        screen.bgcolor("red")
        t = Turtle()
        t.pu()
        t.goto(-150,0)
        t.ht()
        t.color("white")
        t.write("Game Over", font=("Arial", 50, "normal"))

screen = Screen()
screen.register_shape("platform.gif")
screen.bgcolor("light blue")
screen.listen()

platforms=[]
platforms.append(Platform(0,-350))

player = Player()

while not player.land(platforms[0]):
    player.gravity()

generate_platforms()

update()

screen.mainloop()















