"""
File: 
Name: Alan
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
count = 0  # 超過右側邊界次數
vy = 0  # y方向位移
switch = True  # 控制點按有無影響的開關


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(click)


def click(mouse):  # mouse 用不到
    global count, vy, switch
    if switch:
        switch = False  # 點按進來後 即關閉開關 使整顆球尚未超過右界前的點按皆無作用
        while True:
            # print(ball.y)
            if count < 3:  # 先判斷以免多位移一次
                # y方向不論正負皆在一單位時間(DELAY)內受重力影響增加(+1)的位移 vy = 1, 1+1, 1+1+1, ...., 30, -26, -25, ..., 0
                vy += GRAVITY
                ball.move(VX, vy)
                if ball.y + ball.height >= window.height:  # 球一旦超過下界
                    ball.y = window.height - ball.height  # 把跳超過的部分歸位
                    vy *= -REDUCE  # 因為ball.y已經歸位 vy只會被調一次 vy=30*-0.9, 27*-0.9, ...
                    ball.move(VX, vy)  # 嚴謹一點考量 為了讓每次反彈高度都是上次的REDUCE倍
                if ball.x >= window.width:  # 一旦整顆球超過右界
                    count += 1
                    vy = 0  # 須歸零以避免還保留超過右側邊界前的位移
                    ball.x = START_X
                    ball.y = START_Y
                    switch = True  # 直到整顆球超過右界 開關才會打開
                    break
                pause(DELAY)
            else:  # count為三次以上時執行此 避免迴圈無法結束
                break


if __name__ == "__main__":
    main()
