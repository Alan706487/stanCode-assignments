"""
File: 
Name: Alan
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hollow circle
SIZE = 30
# Global Variable
window = GWindow()
circle = GOval(SIZE, SIZE)  # let circle be global object
count = 0  # let circle be global variable


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle_or_line)


def circle_or_line(mouse):
    global count  # for changing global variable--count
    if count % 2 == 0:  # count is even
        window.add(circle, mouse.x-circle.width/2, mouse.y-circle.height/2)
    else:  # count is odd
        # put (x0, y0) at the center of circle
        line = GLine(circle.x+circle.width/2, circle.y+circle.height/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
    count += 1


if __name__ == "__main__":
    main()
