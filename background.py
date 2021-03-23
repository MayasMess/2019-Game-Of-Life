import pygame


class Background:
    def __init__(self, surface, screen_width, screen_height):
        self.surface = surface
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect_size = 20
        self.black_color = (0, 0, 0)
        self.black_rects = []

    def draw(self):
        for x in range(self.screen_width//self.rect_size):
            for y in range(self.screen_height//self.rect_size):
                pygame.draw.rect(self.surface, self.black_color, ((x*self.rect_size) - 1, (y*self.rect_size) - 1,
                                                                  self.rect_size, self.rect_size), 1)
        for pos in self.black_rects:
            pygame.draw.rect(self.surface, self.black_color, (pos[0], pos[1], self.rect_size, self.rect_size))

    def get_new_pos(self, position):
        new_pos = []
        for x in position:
            new_x = (x//self.rect_size)*self.rect_size
            new_pos.append(new_x)
        return tuple(new_pos)

    def change_color_on_click(self, position):
        if position is not None:
            new_pos = self.get_new_pos(position)
            self.black_rects.append(new_pos)

    def start_life_game(self):
        new_black_rects = []
        cell_to_create = []
        rs = self.rect_size
        for index, cell in enumerate(self.black_rects):
            cell_around = 0
            for x in range(len(self.black_rects)):
                try:
                    for around_cell in [(cell[0]+rs, cell[1]), (cell[0]-rs, cell[1]), (cell[0], cell[1]+rs),
                                        (cell[0], cell[1]-rs), (cell[0]+rs, cell[1]+rs), (cell[0]-rs, cell[1]+rs),
                                        (cell[0]+rs, cell[1]-rs), (cell[0]-rs, cell[1]-rs)]:
                        if around_cell[0] == self.black_rects[x][0] and around_cell[1] == self.black_rects[x][1]:
                            cell_around += 1
                        else:
                            if index == x:
                                cell_to_create.append(around_cell)
                except IndexError as e:
                    print(f'index error: {e}')
            if 1 < cell_around < 4:
                new_black_rects.append(cell)
        to_create_dict = {i: cell_to_create.count(i) for i in cell_to_create}
        for key, value in to_create_dict.items():
            if value == 3:
                new_black_rects.append(key)
        new_black_rects = list(dict.fromkeys(new_black_rects))
        self.black_rects = new_black_rects
