

class Line:

    def __init__(self, begin_x, begin_y, end_x, end_y):
        self.begin_x = begin_x
        self.begin_y = begin_y
        self.end_x = end_x
        self.end_y = end_y

    def get_begin(self):
        return self.begin_x, self.begin_y

    def get_end(self):
        return self.end_x, self.end_y

    def get_pygame_begin(self):
        return self.begin_x, self.begin_y

    def get_pygame_end(self):
        return self.end_x - self.begin_x, self.end_y - self.begin_y
