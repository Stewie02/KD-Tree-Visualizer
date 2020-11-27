import pygame


class Graph:

    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('KD-tree')
        self.running = True
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.lines_to_show = []
        self.frame_count = 0

    def show_point(self, point):
        coordinate = (point.get_x(), point.get_y())
        color = (255, 255, 255)
        pygame.draw.circle(self.screen, color, coordinate, 5)
        pygame.display.flip()

    def show_line(self, line):
        color = (0, 0, 255)
        pygame.draw.line(self.screen, color, line.get_begin(), line.get_end(), 1)

    def show_lines(self, lines):
        self.lines_to_show.extend(lines)

    def run_graph(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.event_handler(event)

            if self.frame_count % 60 == 0:
                if len(self.lines_to_show) > 0:
                    line = self.lines_to_show.pop(0)
                    self.show_line(line)

            self.frame_count += 1
            pygame.display.flip()

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            self.running = False
