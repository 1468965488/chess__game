import pygame
import traceback
from pygame.locals import *
import sys
import numpy as np
import piece

pygame.init()

bg_size = height, weight = 804, 812
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("象棋游戏")
background = pygame.image.load("H:/chess/images/board.png").convert()
# 表示棋盘格某一个位置是否有棋子的二位数组
board = np.zeros((10, 9))


# 所有棋子图片
B_boss = pygame.image.load("H:/chess/images/B_boss.png").convert_alpha()
B_knight = pygame.image.load("H:/chess/images/B_knight.png").convert_alpha()
B_knight_2 = pygame.image.load("H:/chess/images/B_knight_2.png").convert_alpha()
B_bishop = pygame.image.load("H:/chess/images/B_elep.png").convert_alpha()
B_bishop_2 = pygame.image.load("H:/chess/images/B_elep_2.png").convert_alpha()
B_horse = pygame.image.load("H:/chess/images/B_horse.png").convert_alpha()
B_horse_2 = pygame.image.load("H:/chess/images/B_horse_2.png").convert_alpha()
B_rook = pygame.image.load("H:/chess/images/B_rook.png").convert_alpha()
B_rook_2 = pygame.image.load("H:/chess/images/B_rook_2.png").convert_alpha()
B_gun = pygame.image.load("H:/chess/images/B_gun.png").convert_alpha()
B_gun_2 = pygame.image.load("H:/chess/images/B_gun_2.png").convert_alpha()
B_soldier = pygame.image.load("H:/chess/images/B_soilder.png").convert_alpha()
B_soldier_2 = pygame.image.load("H:/chess/images/B_soilder.png").convert_alpha()
B_soldier_3 = pygame.image.load("H:/chess/images/B_soilder.png").convert_alpha()
B_soldier_4 = pygame.image.load("H:/chess/images/B_soilder.png").convert_alpha()
B_soldier_5 = pygame.image.load("H:/chess/images/B_soilder.png").convert_alpha()
R_boss = pygame.image.load("H:/chess/images/R_boss.png").convert_alpha()
R_knight = pygame.image.load("H:/chess/images/R_knight.png").convert_alpha()
R_knight_2 = pygame.image.load("H:/chess/images/R_knight_2.png").convert_alpha()
R_bishop = pygame.image.load("H:/chess/images/R_elep.png").convert_alpha()
R_bishop_2 = pygame.image.load("H:/chess/images/R_elep_2.png").convert_alpha()
R_horse = pygame.image.load("H:/chess/images/R_horse.png").convert_alpha()
R_horse_2 = pygame.image.load("H:/chess/images/R_horse_2.png").convert_alpha()
R_rook = pygame.image.load("H:/chess/images/R_rook.png").convert_alpha()
R_rook_2 = pygame.image.load("H:/chess/images/R_rook_2.png").convert_alpha()
R_gun = pygame.image.load("H:/chess/images/R_gun.png").convert_alpha()
R_gun_2 = pygame.image.load("H:/chess/images/R_gun_2.png").convert_alpha()
R_soldier = pygame.image.load("H:/chess/images/R_soilder.png").convert_alpha()
R_soldier_2 = pygame.image.load("H:/chess/images/R_soilder.png").convert_alpha()
R_soldier_3 = pygame.image.load("H:/chess/images/R_soilder.png").convert_alpha()
R_soldier_4 = pygame.image.load("H:/chess/images/R_soilder.png").convert_alpha()
R_soldier_5 = pygame.image.load("H:/chess/images/R_soilder.png").convert_alpha()


# 位置计算 定义横轴为y,纵轴为x   ,可能用不上了
def real_pos(x, y):
    real_x = 45 + x * 81 - 40 - 8
    real_y = 89 + y * 80 - 40
    real_position = (real_y, real_x)
    return real_position


# 根据鼠标点击的位置判断玩家在点棋盘的那个格子
def pos_locate(position):
    x_part_1 = int(abs(position[1] - 38) / 81)
    x_part_2 = abs(position[1]-38) % 81
    if x_part_2 >= 40:
        x_part_2 = 1
    else:
        x_part_2 = 0

    y_part_1 = int((position[0] - 81) / 80)
    y_part_2 = (position[0]-81) % 80
    if y_part_2 >= 40:
        y_part_2 = 1
    else:
        y_part_2 = 0

    # 左右边界限定
    if position[0] < 90:
        y_part_1 = 0
        y_part_2 = 0
    if position[0] > 720:
        y_part_1 = 8
        y_part_2 = 0

    position = (x_part_2+x_part_1, y_part_2+y_part_1)
    return position


# 后来想起来，创建一个列表就可以，但是现在再改就太麻烦了
def all_pieces_init(group):
    pieces = piece.Piece(R_rook, 0, 0, "rook", "red")
    group.add(pieces)
    pieces = piece.Piece(R_horse, 0, 1, "horse", "red")
    group.add(pieces)
    pieces = piece.Piece(R_bishop, 0, 2, "bishop", "red")
    group.add(pieces)
    pieces = piece.Piece(R_knight, 0, 3, "knight", "red")
    group.add(pieces)
    pieces = piece.Piece(R_boss, 0, 4, "boss", "red")
    group.add(pieces)
    pieces = piece.Piece(R_knight_2, 0, 5, "knight", "red")
    group.add(pieces)
    pieces = piece.Piece(R_bishop_2, 0, 6, "bishop", "red")
    group.add(pieces)
    pieces = piece.Piece(R_horse_2, 0, 7, "horse", "red")
    group.add(pieces)
    pieces = piece.Piece(R_rook_2, 0, 8, "rook", "red")
    group.add(pieces)
    pieces = piece.Piece(R_gun, 2, 1, "gun", "red")
    group.add(pieces)
    pieces = piece.Piece(R_gun_2, 2, 7, "gun", "red")
    group.add(pieces)
    pieces = piece.Piece(R_soldier, 3, 0, "soldier", "red")
    group.add(pieces)
    pieces = piece.Piece(R_soldier_2, 3, 2, "soldier", "red")
    group.add(pieces)
    pieces = piece.Piece(R_soldier_3, 3, 4, "soldier", "red")
    group.add(pieces)
    pieces = piece.Piece(R_soldier_4, 3, 6, "soldier", "red")
    group.add(pieces)
    pieces = piece.Piece(R_soldier_5, 3, 8, "soldier", "red")
    group.add(pieces)

    pieces = piece.Piece(B_rook, 9, 0, "rook", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_horse, 9, 1, "horse", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_bishop, 9, 2, "bishop", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_knight, 9, 3, "knight", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_boss, 9, 4, "boss", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_knight_2, 9, 5, "knight", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_bishop_2, 9, 6, "bishop", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_horse_2, 9, 7, "horse", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_rook_2, 9, 8, "rook", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_gun, 7, 1, "gun", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_gun_2, 7, 7, "gun", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_soldier, 6, 0, "soldier", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_soldier_2, 6, 2, "soldier", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_soldier_3, 6, 4, "soldier", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_soldier_4, 6, 6, "soldier", "blue")
    group.add(pieces)
    pieces = piece.Piece(B_soldier_5, 6, 8, "soldier", "blue")
    group.add(pieces)

    board[0] = 1
    board[9] = 1
    board[2][1] = 1
    board[2][7] = 1
    board[7][1] = 1
    board[7][7] = 1
    board[3][0] = 1
    board[3][2] = 1
    board[3][4] = 1
    board[3][6] = 1
    board[3][8] = 1
    board[6][0] = 1
    board[6][2] = 1
    board[6][4] = 1
    board[6][6] = 1
    board[6][8] = 1
    print(board)


def move(i, position):

    i.x = position[0]  # 棋子的新位置
    i.y = position[1]

    board[i.x][i.y] = 1
    board[i.x_last][i.y_last] = 0  # 在棋盘上显示棋子移动

    i.selected = False
    i.x_last = position[0]
    i.y_last = position[1]


def kile(group, e):
    for i in group:
        if i.target:
            i.alive = False
            i.target = False
    e.selected = False


def save(group, position, e):
    for i in group:
        if i.target:
            i.target = False

    e.selected = False
    board[position[0]][position[1]] = 1


# choice 表示的是这条线是横着还是竖着
def count_empty(i, position, choice):
    counting = 0
    if choice == 1:
        if i.y > position[1]:
            if i.y - position[1] > 1:
                for each in range(position[1], i.y):
                    if board[i.x][each] == 1:
                        counting += 1
            else:
                counting = 0
        else:
            if position[1] - i.y > 1:
                for each in range(i.y+1, position[1]):
                    if board[i.x][each] == 1:
                        counting += 1
            else:
                counting = 0
    else:
        if i.x > position[0]:
            if i.x - position[0] > 1:
                for each in range(position[0], i.x):
                    if board[each][i.y] == 1:
                        counting += 1
            else:
                counting = 0
        else:
            if position[0] - i.x > 1:
                for each in range(i.x+1, position[0]):
                    if board[each][i.y] == 1:
                        counting += 1
            else:
                counting = 0
    return counting


def main():
    turn_counting = 0  # 用于计数
    full = False
    faction = None
    clock = pygame.time.Clock()
    all_pieces = pygame.sprite.Group()
    all_pieces_init(all_pieces)
    # 表示是否拿起棋子的变量，拿起之后才能走
    waiting = False
    # 表示是否有棋子的第二个变量
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                position = pos_locate(event.pos)
                print(position)
                if turn_counting % 2 == 0:
                    turn = "red"
                else:
                    turn = "blue"

                # 选定要走的位置
                if waiting:
                    for i in all_pieces:
                        if i.selected and i.alive:                  # 找到上次选中的棋子
                            # 如果选定位置与原来位置相同
                            if position[0] == i.x and position[1] == i.y:
                                pass
                            else:
                                if board[position[0]][position[1]] == 1:
                                    # 如果有棋子就先把它吃掉, 吃掉以后这里就没有棋子了,就可以满足下一个条件
                                    for each in all_pieces:
                                        if each.x == position[0] and each.y == position[1]:
                                            # 把这个棋子标记为目标，并且清空所在棋盘上位置
                                            each.target = True
                                            board[position[0]][position[1]] = 0

                                for each in all_pieces:
                                    if each.alive and each.x == position[0] and position[1] == each.y:
                                        full = True
                                        faction = each.faction

                                # 如果新位置没有棋子(如果有，先清空就没有了, 所以这里是必然会进来的)
                                if board[position[0]][position[1]] == 0:

                                    # 选中卒
                                    if i.species == "soldier":
                                        print(i.species)
                                        # 如果是红方的卒，只能往下或者左右一个单位
                                        if i.faction == "red":
                                            # 检查这个地放是否有棋子而且记录其阵营
                                            if i.y == position[1] and position[0] - i.x == 1:
                                                if not full or i.faction != faction:
                                                    move(i, position)   # 代码复用部分，之后不再赘述
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            elif i.x > 4 and i.x == position[0] and abs(i.y-position[1]) == 1:
                                                if not full or i.faction != faction:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        # 如果是蓝色方的卒
                                        else:
                                            if i.y == position[1] and position[0] - i.x == -1:
                                                if not full or i.faction != faction:
                                                    move(i, position)  # 代码复用部分，之后不再赘述
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            elif i.x < 5 and i.x == position[0] and abs(i.y-position[1]) == 1:
                                                if not full or i.faction != faction:
                                                    move(i, position)  # 代码复用部分，之后不再赘述
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False

                                    # 选中炮
                                    elif i.species == "gun":
                                        # 横着走
                                        if position[0] == i.x:
                                            count = count_empty(i, position, 1)
                                            for each in all_pieces:
                                                if each.alive and each.x == position[0] and position[1] == each.y:
                                                    full = True
                                                    faction = each.faction
                                            if not full:
                                                if count == 0:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                                    full = False
                                            else:
                                                if count == 1:
                                                    if faction != i.faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                        # 竖着走
                                        elif position[1] == i.y:
                                            count = count_empty(i, position, 2)
                                            for each in all_pieces:
                                                if each.alive and each.x == position[0] and position[1] == each.y:
                                                    full = True
                                                    faction = each.faction
                                            if not full:
                                                if count == 0:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                                    full = False
                                            else:
                                                if count == 1:
                                                    if i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                        else:
                                            save(all_pieces, position, i)
                                            waiting = False

                                    # 选中车
                                    elif i.species == "rook":
                                        # 横着走
                                        if position[0] == i.x:
                                            count = count_empty(i, position, 1)
                                            if count == 0:
                                                if not full or i.faction != faction:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        # 竖着走
                                        elif position[1] == i.y:
                                            count = count_empty(i, position, 2)
                                            if count == 0:
                                                if not full or i.faction != faction:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        else:
                                            save(all_pieces, position, i)
                                            waiting = False

                                    # 选中马
                                    elif i.species == "horse":
                                        # 情况1
                                        if abs(position[0] - i.x) == 2 and abs(position[1] - i.y) == 1:
                                            # 没有别马腿
                                            if board[int((position[0]+i.x)/2)][i.y] == 0:
                                                if not full or i.faction != faction:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        elif abs(position[0] - i.x) == 1 and abs(position[1] - i.y) == 2:
                                            # 没有别马腿
                                            if board[i.x][int((position[1] + i.y)/2)] == 0:
                                                if not full or i.faction != faction:
                                                    move(i, position)
                                                    kile(all_pieces, i)
                                                    waiting = False
                                                    turn_counting += 1
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        else:
                                            save(all_pieces, position, i)
                                            waiting = False

                                    # 选中象

                                    elif i.species == "bishop":
                                        # 象是不可以过河的
                                        if i.faction == "red":
                                            if abs(i.x - position[0]) == 2 and abs(i.y - position[1]) == 2 and \
                                                    position[0] < 5:
                                                # 如果没有憋象腿
                                                if board[int((i.x+position[0])/2)][int((i.y+position[1])/2)] == 0:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        else:
                                            if abs(i.x - position[0]) == 2 and abs(i.y - position[1]) == 2 and \
                                                    position[0] > 4:
                                                # 如果没有憋象腿
                                                if board[int((i.x+position[0])/2)][int((i.y+position[1])/2)] == 0:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False

                                    # 选中士
                                    elif i.species == "knight":
                                        # 士是不可以过河的
                                        if i.faction == "red":
                                            if abs(i.x - position[0]) == 1 and abs(i.y - position[1]) == 1:
                                                if 2 < position[1] and position[1] < 6 and position[0] < 3:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        else:
                                            if abs(i.x - position[0]) == 1 and abs(i.y - position[1]) == 1:
                                                if 2 < position[1] and position[1] < 6 and position[0] >6:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False

                                    # 选中老将
                                    elif i.species == "boss":
                                        # 老将是不可以出格的
                                        if i.faction == "red":
                                            if abs(i.x - position[0]) + abs(i.y - position[1]) == 1:
                                                if 2 < position[1] and position[1] < 6 and position[0] < 3:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False
                                        else:
                                            if abs(i.x - position[0]) + abs(i.y - position[1]) == 1:
                                                if 2 < position[1] and position[1] < 6 and position[0] > 6:
                                                    if not full or i.faction != faction:
                                                        move(i, position)
                                                        kile(all_pieces, i)
                                                        waiting = False
                                                        turn_counting += 1
                                                    else:
                                                        save(all_pieces, position, i)
                                                        waiting = False
                                                else:
                                                    save(all_pieces, position, i)
                                                    waiting = False
                                            else:
                                                save(all_pieces, position, i)
                                                waiting = False

                else:
                    if board[position[0], position[1]] == 1 and not waiting:
                        for each in all_pieces:
                            if each.x == position[0] and each.y == position[1] and each.alive:
                                if each.faction == turn:
                                    each.selected = True
                                    full = False
                                    waiting = True
                                else:
                                    pass

                print(waiting)
                print(turn)

        # 绘制背景图片
        screen.blit(background, (0, -8))
        # 绘制所有棋子
        for each in all_pieces:
            if each.alive:
                screen.blit(each.image, (real_pos(each.x, each.y)))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
