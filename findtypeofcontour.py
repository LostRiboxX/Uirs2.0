import math
from Excel_inputer import write_data_to_excel
from crop import croped
from filter import filter
from diff import imgContours
from cont import drawconts
from tests1 import drawconnectionslines
from Diikstra import dijkstra
from homie import drawwheels
from WheelRec import get_wheel_frag
from Draw_path import draw_path, rotate_wheels_draw, line_wheels_draw, seg_line
import numpy as np
import cv2

# 220 - 1030
#  18 -  x

speeds = np.array([46, 46, 5.7])
disc = 0.1
imgnameprime = '1.jpg'
dict = {'red': 10, 'blue': 4, 'gray': 1, 'darkgray': 5, 'lightgreen': 2, 'green': 3, 'pink': 2, 'lightbrown': 4,
        'brown': 5}
seq1 = ['gray', 'blue', 'brown', 'lightgreen', 'lightgreen', 'red', 'gray', 'brown', 'red', 'darkgray', 'gray',
        'lightgreen', 'brown', 'red', 'green', 'darkgray', 'gray', 'blue', 'gray', 'pink', 'lightgreen', 'green',
        'lightbrown']

speeds_for_pic = speeds * disc
print(speeds_for_pic)

# Обрезаем картинку
imgcroped = croped(imgnameprime)
# Фильтруем  изображение
imgfiltered = filter(imgcroped)

imgdone = cv2.imread("1.jpg_croped.png_done.png")
imgconts = "1.jpg_croped.png_filtered.png_contours.png"

# Получаем массив координат центров фрагментов и их контуры
centersmass, contours = drawconts(imgconts, imgcroped)
# print(centersmass)
# Получаем массив связей фрагментов между собой
connections = drawconnectionslines(imgcroped, contours, centersmass, 100)

# Это для будущего

start_angle = 131
end_angle = -90

wheels_coords_start = drawwheels(imgconts, imgcroped, 13, start_angle)
wheels_coords_end = drawwheels(imgconts, imgcroped, 1, -90)

# Формируем граф в виде словря словарей
dict_graph = {}
for i in range(len(connections)):
    tmp = {}
    for j in range(len(connections[i])):
        tmp[connections[i][j]] = dict[seq1[connections[i][j]]]
    dict_graph[i] = tmp

value, path = dijkstra(dict_graph, 13, 1)

img_w_path_name, lines_data = draw_path(imgdone, centersmass, path)
print(lines_data)
# rotate_wheels_draw(img_w_path_name, lines_data[0][0], start_angle, lines_data[0][5], speeds_for_pic[2], "rot0")
# for i in range(len(lines_data)):
#     try:
#         line_wheels_draw(img_w_path_name, lines_data[i][0], lines_data[i][1], speeds_for_pic[0], lines_data[i][4], lines_data[i][5], f"line{i+1}")
#         rotate_wheels_draw(img_w_path_name, lines_data[i+1][0], lines_data[i][5], lines_data[i+1][5], speeds_for_pic[2], f"rot{i+1}")
#     except:
#         rotate_wheels_draw(img_w_path_name, lines_data[i][1], lines_data[i][5], end_angle, speeds_for_pic[2], f"rot{i+1}")
# 22 --- 4

data = []
iters_num = int((lines_data[0][5] - start_angle) // speeds_for_pic[2])
for i in range(int(math.fabs(iters_num))):
    if iters_num < 0:
        data.append([f"(0, 0, -0.1)", f"{start_angle - (i * speeds_for_pic[2])}", f'{lines_data[0][0]}'])
    else:
        data.append([f"(0, 0, 0.1)", f"{start_angle + (i * speeds_for_pic[2])}", f'{lines_data[0][0]}'])
if iters_num < 0:
    data.append([f"(0, 0, -0.1)", f"{lines_data[0][5]}", f'{lines_data[0][0]}'])
else:
    data.append([f"(0, 0, 0.1)", f"{lines_data[0][5]}", f'{lines_data[0][0]}'])
for j in range(len(lines_data)):
    try:
        num_points = int(lines_data[j][4] / speeds_for_pic[0])
        points = seg_line(lines_data[j][0], lines_data[j][1], num_points)
        for i in points:
            data.append([f'(0.1, 0, 0)', f'{lines_data[j][5]}', f'{i}'])
        iters_num = int((lines_data[j+1][5] - lines_data[j][5]) // speeds_for_pic[2])
        for q in range(int(math.fabs(iters_num))):
            if iters_num < 0:
                data.append([f"(0, 0, -0.1)", f"{lines_data[j][5] - (q * speeds_for_pic[2])}", f'{lines_data[j][1]}'])
            else:
                data.append([f"(0, 0, 0.1)", f"{lines_data[j][5] + (q * speeds_for_pic[2])}", f'{lines_data[j][1]}'])
        if iters_num < 0:
            data.append([f"(0, 0, -0.1)", f"{lines_data[j+1][5]}", f'{lines_data[j][1]}'])
        else:
            data.append([f"(0, 0, 0.1)", f"{lines_data[j+1][5]}", f'{lines_data[j][1]}'])
    except:
        iters_num = int((end_angle - lines_data[j][5]) // speeds_for_pic[2])
        for v in range(int(math.fabs(iters_num))):
            if iters_num < 0:
                data.append([f"(0, 0, -0.1)", f"{lines_data[j][5] - (v * speeds_for_pic[2])}", f'{lines_data[j][1]}'])
            else:
                data.append([f"(0, 0, 0.1)", f"{lines_data[j][5] + (v * speeds_for_pic[2])}", f'{lines_data[j][1]}'])
        if iters_num < 0:
            data.append([f"(0, 0, -0.1)", f"{end_angle}", f'{lines_data[j][1]}'])
        else:
            data.append([f"(0, 0, 0.1)", f"{end_angle}", f'{lines_data[j][1]}'])

write_data_to_excel(data=data, output_path='output/data.xlsx')