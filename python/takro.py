import sys
import numpy as np
from random import randrange,choice
import arcade
from practicum import find_mcu_boards, McuBoard, PeriBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Takro"
BALL_COLORS = [
    arcade.color.RED,
    arcade.color.GREEN,
    arcade.color.YELLOW,
    arcade.color.BLUE,
    arcade.color.MAGENTA,
    arcade.color.CYAN,
]

mcu = McuBoard(find_mcu_boards()[0])
peri = PeriBoard(mcu)

#########################################
class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)
        self.score = 0
        self.lives = len(BALL_COLORS)
        self.is_over = False
        self.balls = []
        self.player = Player()
        peri.set_led_value(self.lives)

        for color in BALL_COLORS:
            ball = Ball(self)
            ball.set_velocity(np.array([
                randrange(-50,50),
                randrange(-50,50),
            ]))
            ball.set_color(color)
            self.balls.append(ball)

    #def on_mouse_motion(self, x, y, delta_x, delta_y):
    #    self.player.pos = x

    def update(self,dt):
        self.player.update(dt)
        for ball in self.balls:
            ball.update(dt)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for ball in self.balls:
            ball.draw()

#########################################
class Ball:

    def __init__(self, game, radius=10, color=arcade.color.WHITE,
            pos=np.array([SCREEN_WIDTH/2,SCREEN_HEIGHT/2]),
            vel=np.array([100,0])):
        self.game = game
        self.pos = pos.astype(float)
        self.vel = vel.astype(float)
        self.radius = radius
        self.color = color

    def set_velocity(self,vel):
        self.vel = vel.astype(float)

    def set_color(self,color):
        self.color = color

    def update(self,dt):
        self.vel += np.array([0,-90.8])*dt
        self.pos += self.vel*dt

        # player-hitting check
        if self.game.player.hit(self):
            self.game.score += 1
            # bounce ball back, also increase speed and add some jerk
            self.vel[1] = abs(self.vel[1])*1.1
            self.vel[0] += randrange(-50,50)

        # reduce lives when ball hits the ground
        if self.pos[1] < self.radius:
            self.game.balls.remove(self)
            self.game.lives -= 1
            peri.set_led_value(self.game.lives)
            if self.game.lives == 0:
                self.game.is_over = True
                print("******* GAME OVER *******")
                sys.exit(0)

        # make ball bounce if hitting other three walls
        if self.pos[0] < self.radius:
            self.vel[0] = abs(self.vel[0])
        if self.pos[0] > SCREEN_WIDTH-self.radius:
            self.vel[0] = -abs(self.vel[0])
        if self.pos[1] > SCREEN_HEIGHT-self.radius:
            self.vel[1] = -abs(self.vel[1])

    def draw(self):
        x,y = self.pos
        arcade.draw_circle_filled(x,y,self.radius,self.color)

#########################################
class Player:

    THICKNESS = 10

    def __init__(self, pos=SCREEN_WIDTH/2, width=100, color=arcade.color.GREEN):
        self.width = width
        self.pos = pos
        self.color = color
        self.light_min = 0
        self.light_max = 100

    def set_light_range(self,light_min,light_max):
        self.light_min = light_min
        self.light_max = light_max

    def hit(self, ball):
        return ball.pos[1]-ball.radius < self.THICKNESS and \
            self.pos-self.width/2 < ball.pos[0] < self.pos+self.width/2

    def update(self,dt):
        newpos = np.interp(peri.get_light(),
                [self.light_min,self.light_max],
                [0,SCREEN_WIDTH])
        self.pos = 0.9*self.pos + 0.1*newpos

    def draw(self):
        arcade.draw_rectangle_filled(
                self.pos,self.THICKNESS/2,
                self.width,self.THICKNESS,
                color=self.color)

print("-------------------------")
input("Cover the light sensor and press ENTER...")
light_min = peri.get_light()
input("Remove your hand and press ENTER...")
light_max = peri.get_light()
game = Game()
game.player.set_light_range(light_min,light_max)
arcade.run()
