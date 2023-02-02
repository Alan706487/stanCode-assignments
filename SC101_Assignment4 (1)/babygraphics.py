"""
File: babygraphics.py
Name: Alan
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    line_gap = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE+year_index*line_gap
    return int(x_coordinate)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    for year_index in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), 0, get_x_coordinate(CANVAS_WIDTH, year_index),
                           CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=str(YEARS[year_index]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    real_thousandths = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000  # 扣掉保留長度後的縱軸長度均分一千等分
    # 用lookup_names的長度調整COLORS元素的循環次數，保證lookup_names的索引可以對應到colors_lst的索引
    # 不直接*len(COLORS)只是不想colors_lst太長
    colors_lst = COLORS*int(len(lookup_names)/len(COLORS)+1)
    for name in lookup_names:  # lookup_names的名字一定在name_data裡才會被查到
        color = colors_lst[lookup_names.index(name)]  # lookup_names中的name索引會和color索引對應
        year_lst = list(name_data[name].keys())  # str:因不同名字榜上有名的次數(m,m<=len(YEARS))不同，包成串列為了之後用index挑出特定的年份
        rank_lst = list(name_data[name].values())  # str:也取出名次，索引與year_lst對應
        for i in range(len(YEARS) - 1):  # n年區間有n-1個線段 (但文字在線段端點都要出現，會少寫一次，故設計線段端點交疊處重複寫，不影響呈現)
            x_start = get_x_coordinate(CANVAS_WIDTH, i)
            x_end = get_x_coordinate(CANVAS_WIDTH, i+1)
            y_bottom = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE  # 排名在一千以外的那年線段頂點貼在底部
            # 畫線須同時傳值起點與終點，因存在邊界，且不同人非每年都有名次，因此分以下四種情況討論
            if str(YEARS[i]) in year_lst and str(YEARS[i+1]) in year_lst:  # 連續兩點(線段起終點年份)皆有上榜(有名次)
                # 排名第n的頂點落在第n-1千分位real_thousandths
                y_start = GRAPH_MARGIN_SIZE + real_thousandths * (int(rank_lst[year_lst.index(str(YEARS[i]))]) - 1)
                y_end = GRAPH_MARGIN_SIZE + real_thousandths * (int(rank_lst[year_lst.index(str(YEARS[i + 1]))]) - 1)
                canvas.create_line(x_start, y_start, x_end, y_end, width=LINE_WIDTH, fill=color)
                canvas.create_text(x_start+TEXT_DX, y_start, text=f'{name} {rank_lst[year_lst.index(str(YEARS[i]))]}',
                                   anchor=tkinter.SW, fill=color)
                canvas.create_text(x_end + TEXT_DX, y_end, text=f'{name} {rank_lst[year_lst.index(str(YEARS[i+1]))]}',
                                   anchor=tkinter.SW, fill=color)
            elif str(YEARS[i]) not in year_lst and str(YEARS[i+1]) in year_lst:  # 起點年沒上，但終點年有上榜
                y_end = GRAPH_MARGIN_SIZE + real_thousandths * (int(rank_lst[year_lst.index(str(YEARS[i + 1]))]) - 1)
                canvas.create_line(x_start, y_bottom, x_end, y_end, width=LINE_WIDTH, fill=color)
                canvas.create_text(x_start + TEXT_DX, y_bottom, text=f'{name} *', anchor=tkinter.SW, fill=color)
                canvas.create_text(x_end + TEXT_DX, y_end, text=f'{name} {rank_lst[year_lst.index(str(YEARS[i + 1]))]}',
                                   anchor=tkinter.SW, fill=color)
            elif str(YEARS[i]) in year_lst and str(YEARS[i+1]) not in year_lst:  # 起點年有上榜，而終點年無
                y_start = GRAPH_MARGIN_SIZE + real_thousandths * (int(rank_lst[year_lst.index(str(YEARS[i]))]) - 1)
                canvas.create_line(x_start, y_start, x_end, y_bottom, width=LINE_WIDTH, fill=color)
                canvas.create_text(x_start + TEXT_DX, y_start, text=f'{name} {rank_lst[year_lst.index(str(YEARS[i]))]}',
                                   anchor=tkinter.SW, fill=color)
                canvas.create_text(x_end + TEXT_DX, y_bottom, text=f'{name} *', anchor=tkinter.SW, fill=color)
            else:  # 起終點年皆無上榜
                canvas.create_line(x_start, y_bottom, x_end, y_bottom, width=LINE_WIDTH, fill=color)
                canvas.create_text(x_start + TEXT_DX, y_bottom, text=f'{name} *', anchor=tkinter.SW, fill=color)
                canvas.create_text(x_end + TEXT_DX, y_bottom, text=f'{name} *', anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
