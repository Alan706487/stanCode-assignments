"""
File: 
Name: Alan
----------------------
TODO:
"""

from campy.graphics.gobjects import *
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage

window = GWindow(700, 500)


def main():
    """
    作品名稱: 全家福
    創作理念: 有多久沒有跟家人來張溫馨的全家福呢?希望大家都能夠像妹妹一樣帶著笑容面對這個世界，哥哥們厚實的臂膀永遠是你最堅強的後盾。
    """
    bg = GRect(700, 500)  # background
    window.add(bg)
    bg.filled = True
    bg.fill_color = "mintcream"

    man(195, 60)
    man(60, 150)
    man(600, 25)
    man(465, 100)
    man(330, 90)

    sofa1 = GPolygon()
    sofa1.add_vertex((0, window.height-120))
    sofa1.add_vertex((130, window.height-100-50))
    sofa1.add_vertex((130, window.height-80))
    sofa1.add_vertex((0, window.height))
    sofa1.filled = True
    sofa1.fill_color = "lightgray"
    window.add(sofa1)

    sofa2 = GPolygon()
    sofa2.add_vertex((130, window.height-100-50))
    sofa2.add_vertex((320, window.height-100-50))
    sofa2.add_vertex((320, window.height-80))
    sofa2.add_vertex((130, window.height-80))
    sofa2.filled = True
    sofa2.fill_color = "lightgray"
    window.add(sofa2)

    sofa21 = GPolygon()
    sofa21.add_vertex((0, window.height))
    sofa21.add_vertex((130, window.height-80))
    sofa21.add_vertex((320, window.height-80))
    sofa21.add_vertex((300, window.height))
    sofa21.filled = True
    sofa21.fill_color = "lightgray"
    window.add(sofa21)

    sofa3 = GPolygon()
    sofa3.add_vertex((320, window.height-100-50))
    sofa3.add_vertex((510, window.height-100-50))
    sofa3.add_vertex((510, window.height-80))
    sofa3.add_vertex((320, window.height-80))
    window.add(sofa3)
    sofa3.filled = True
    sofa3.fill_color = "lightgray"

    sofa31 = GPolygon()
    sofa31.add_vertex((320, window.height-80))
    sofa31.add_vertex((510, window.height-80))
    sofa31.add_vertex((530, window.height))
    sofa31.add_vertex((300, window.height))
    window.add(sofa31)
    sofa31.filled = True
    sofa31.fill_color = "lightgray"

    sofa4 = GPolygon()
    sofa4.add_vertex((510, window.height-100-50))
    sofa4.add_vertex((window.width, window.height-100-50))
    sofa4.add_vertex((window.width, window.height-80))
    sofa4.add_vertex((510, window.height - 80))
    window.add(sofa4)
    sofa4.filled = True
    sofa4.fill_color = "lightgray"

    sofa41 = GPolygon()
    sofa41.add_vertex((510, window.height - 80))
    sofa41.add_vertex((window.width, window.height-80))
    sofa41.add_vertex((window.width, window.height))
    sofa41.add_vertex((530, window.height))
    window.add(sofa41)
    sofa41.filled = True
    sofa41.fill_color = "lightgray"

    pillow(40, 290)
    pillow(610, 330)

    woman = GImage("woman.png")
    window.add(woman, 350, 300)


def man(x, y):
    face = GOval(60, 80)
    face.filled = True
    face.fill_color = "saddlebrown"
    window.add(face,x, y)

    shirt1 = GRect(130, 250)
    shirt1.filled = True
    shirt1.fill_color = "white"
    window.add(shirt1, x-shirt1.width/2+face.width/2, y+face.height)

    shirt2 = GPolygon()
    shirt2.add_vertex((shirt1.x, shirt1.y))
    shirt2.add_vertex((shirt1.x+shirt1.width, shirt1.y))
    shirt2.add_vertex((shirt1.x+shirt1.width+40, shirt1.y+70))
    shirt2.add_vertex((shirt1.x-40, shirt1.y+70))
    shirt2.filled = True
    shirt2.fill_color = "white"
    window.add(shirt2)

    arm1 = GRect(30, 180)
    arm1.filled = True
    arm1.fill_color = "saddlebrown"
    window.add(arm1, shirt1.x-40, shirt1.y+70)

    arm2 = GRect(30, 180)
    arm2.filled = True
    arm2.fill_color = "saddlebrown"
    window.add(arm2, shirt1.x+shirt1.width+40-30, shirt1.y+70)


def pillow(x, y):
    pillow = GRect(150, 150)
    pillow.filled = True
    pillow.fill_color = "skyblue"
    window.add(pillow, x, y)


if __name__ == '__main__':
    main()
