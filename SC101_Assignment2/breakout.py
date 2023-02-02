"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    global NUM_LIVES
    while True:
        if NUM_LIVES == 0:
            print("you loss")
            break
        elif graphics.total_brick == 0:
            print("you win")
            break
        else:
            pause(FRAME_RATE)
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            # 邊界反彈條件
            if graphics.ball.x < 0 or graphics.ball.x > graphics.window.width-graphics.ball.width:
                graphics.reverse_direction(graphics.get_dx())
            if graphics.ball.y < 0:
                graphics.reverse_direction(graphics.get_dy())
            if graphics.ball.y > graphics.window.height-graphics.ball.height:  # 球超過下界
                graphics.reset_ball()  # 球歸位且不會移動
                graphics.switch = True  # 開關變True 之後再點球就能產生隨機速度
                NUM_LIVES -= 1

            # 物件反彈條件
            leftup_ball = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            rifhtup_ball = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            leftdown_ball = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
            rifhtdown_ball = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                           graphics.ball.y + graphics.ball.height)

            # paddle反彈條件
            if (graphics.paddle == leftdown_ball or graphics.paddle == rifhtdown_ball) and \
                    graphics.get_dy() > 0:  # graphics.get_dy()使球沒超過paddle下緣都還可以反彈
                graphics.reverse_direction(graphics.get_dy())  # 反彈只會改變y方向 入射角等於反射角

            # bricks移除反彈條件(偵測到的一定是磚塊)
            if (graphics.paddle != leftup_ball and leftup_ball is not None) or \
                    (graphics.paddle != rifhtup_ball and rifhtup_ball is not None) or \
                    (graphics.paddle != leftdown_ball and leftdown_ball is not None) or \
                    (graphics.paddle != rifhtdown_ball and rifhtdown_ball is not None):
                # 其中之一邊偵測到磚塊就移除磚塊且反彈
                if leftup_ball is not None:
                    graphics.window.remove(leftup_ball)
                elif rifhtup_ball is not None:
                    graphics.window.remove(rifhtup_ball)
                elif leftdown_ball is not None:
                    graphics.window.remove(leftdown_ball)
                else:
                    graphics.window.remove(rifhtdown_ball)
                graphics.reverse_direction(graphics.get_dy())
                graphics.total_brick -= 1


if __name__ == '__main__':
    main()
