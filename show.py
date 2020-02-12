from graphics import *


def main():
    size = (500, 500)
    win = GraphWin('GridWorld', size[0], size[1]) # give title and dimensions

    for g in range(0, size[0], 10):
        v_line = Line(Point(0, g), Point(size[0], g))
        v_line.draw(win)
        h_line = Line(Point(g, 0), Point(g, size[1]))
        h_line.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()