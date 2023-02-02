"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width-self.paddle.width)/2,
                        self.window.height-paddle_offset-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width-self.ball.width)/2, (self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Bricks
        self.total_brick = brick_cols*brick_rows
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset
        self.brick_width = brick_width
        self.brick_height = brick_height
        # Draw bricks
        self.draw_brick()

        # Initialize our mouse listeners
        self.switch = True
        onmouseclicked(self.click)
        onmousemoved(self.drag_paddle)

    def click(self, mouse):  # 點第一下給出球隨機速度
        if self.switch:
            self.set_ball_velocity()
            self.switch = False  # 點第一下變false 之後點都沒用

    def reset_ball(self):
        # 球置中
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height) / 2
        # 讓球超過下界後不會移動
        self.__dx = 0
        self.__dy = 0

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED  # 下降與反彈速度固定
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def draw_brick(self):
        for i in range(self.brick_cols):
            for j in range(self.brick_rows):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                if j < 2:
                    brick.fill_color = 'red'
                elif j < 4:
                    brick.fill_color = 'orange'
                elif j < 6:
                    brick.fill_color = 'yellow'
                elif j < 8:
                    brick.fill_color = 'green'
                else:  # 第九列以上顏色固定
                    brick.fill_color = 'blue'
                self.window.add(brick, i*(brick.width+self.brick_spacing),
                                self.brick_offset+j*(brick.height+self.brick_spacing))

    def drag_paddle(self, mouse):
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def reverse_direction(self, x_or_y):
        if x_or_y == self.get_dx():
            self.__dx *= -1
        else:
            self.__dy *= -1

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy



