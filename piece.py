import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, img, x, y, species, faction):
        pygame.sprite.Sprite.__init__(self)

        self.alive = True        # 棋子是否存活
        self.x = x               # 棋子的坐标
        self.y = y
        self.species = species   # 棋子的类别
        self.faction = faction   # 棋子的阵营
        self.image = img
        self.selected = False    # 是否被选中
        self.x_last = x          # 上次位置
        self.y_last = y
        self.target = False      # 是否被选中为目标


