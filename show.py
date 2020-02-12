from graphics import GraphWin, Text, Line, Point
import json

class Show_Q:

    def __init__(self, filename):
        self.read_q_values(filename)
        self.grid_size = max(self.data)
        self.size = {'x': 1000, 'y': 500}
        self.win = GraphWin('GridWorld', self.size['x'], self.size['y']) # give title and dimensions
        


    def show_grid(self):
        for position in range(0, self.size['y'], int(self.size['y']/self.grid_size[1])):
            h_line = Line(Point(0, position), Point(self.size['x'], position))
            h_line.draw(self.win)
        for position in range(0, self.size['x'], int(self.size['x']/self.grid_size[0])):
            v_line = Line(Point(position, 0), Point(position, self.size['y']))
            v_line.draw(self.win)

    def read_q_values(self, filename):
        with open(filename, 'r') as qfile:
            content = qfile.read()
        self.data = eval(content)


    def show_values(self):
        for grid in self.data:
            qs = [self.data[grid][element] for element in self.data[grid]]
            x = (self.size['x']/self.grid_size[0])*grid[0]+8
            y = (self.size['y']/self.grid_size[1])*grid[1]+5
            data_text = Text(Point(x, y), f"{max(qs):.1f}")
            data_text.setSize(7)
            data_text.draw(self.win)


    def analyze(self):
        message = Text(Point(self.win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(self.win)
        click = self.win.getMouse()
        x, y = click.getX(), click.getY()
        print(f'Click on x: {x}, y: {y}')
        self.win.close()
    
    def finish(self):
        self.win.close()

q_show = Show_Q('agent0-options.log')
q_show.show_grid()
q_show.show_values()
q_show.analyze()

