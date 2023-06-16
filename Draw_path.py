import cv2
import math
import numpy as np
import os


def calculate_line_equation(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    k = (y2 - y1) / (x2 - x1)

    b = y1 - k * x1

    return k, b


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    diff_x = x2 - x1
    diff_y = y2 - y1

    distance = math.sqrt(diff_x ** 2 + diff_y ** 2)

    return distance


def draw_path(img, centermass: list, path: list):
    p1_p2_k_b_len_mass = []
    for i in range(len(path)):
        try:
            cv2.line(img, centermass[path[i]], centermass[path[i + 1]], (255, 0, 0), 3)
            k, b = calculate_line_equation(centermass[path[i]], centermass[path[i + 1]])
            length = calculate_distance(centermass[path[i]], centermass[path[i + 1]])
            if k < 0:
                p1_p2_k_b_len_mass.append(
                   [centermass[path[i]], centermass[path[i + 1]], k, b, length, 180 + (math.atan(k) * 180 / math.pi)])
            else:
                p1_p2_k_b_len_mass.append(
                    [centermass[path[i]], centermass[path[i + 1]], k, b, length, math.atan(k) * 180 / math.pi])
        except:
            break
    img_name = f"1_Path_{path}.png"
    cv2.imwrite(img_name, img)
    return img_name, p1_p2_k_b_len_mass


def drawwheels_x_y(image, point, angle0, name_num, pathname: str) -> None:
    angle = angle0 + 180

    center_x, center_y = point[0], point[1]

    radius1 = 90

    angle1 = angle * math.pi / 180
    angle2 = (2 * math.pi / 3) + (angle * math.pi / 180)
    angle3 = (4 * math.pi / 3) + (angle * math.pi / 180)

    center1_x = int(center_x + radius1 * math.cos(angle1))
    center1_y = int(center_y + radius1 * math.sin(angle1))
    center2_x = int(center_x + radius1 * math.cos(angle2))
    center2_y = int(center_y + radius1 * math.sin(angle2))
    center3_x = int(center_x + radius1 * math.cos(angle3))
    center3_y = int(center_y + radius1 * math.sin(angle3))

    axesLength = (28, 48)

    rot = angle
    rot1 = angle + 120
    rot2 = angle + 240

    cv2.ellipse(image, (center1_x, center1_y), axesLength, rot, 0, 360, (0, 0, 255), 2)
    cv2.ellipse(image, (center2_x, center2_y), axesLength, rot1, 0, 360, (255, 0, 0), 2)
    cv2.ellipse(image, (center3_x, center3_y), axesLength, rot2, 0, 360, (255, 0, 0), 2)

    name = f'{pathname}/{name_num}.png'
    cv2.imwrite(name, image)
    # return ((center1_x, center1_y), (center2_x, center2_y), (center3_x, center3_y))


# Отрисовка поворота
def rotate_wheels_draw(image_name, point, start_anlge, end_angle, r_speed, path):
    os.mkdir(path)
    iters_num = int((end_angle - start_anlge) // r_speed)
    for i in range(int(math.fabs(iters_num))):
        image = cv2.imread(image_name)
        if iters_num < 0:
            drawwheels_x_y(image, point, start_anlge - (i * r_speed), i, path)
        else:
            drawwheels_x_y(image, point, start_anlge + (i * r_speed), i, path)
    drawwheels_x_y(image, point, end_angle, math.fabs(iters_num) + 1, path)


def seg_line(start, end, num_points):

    x1, y1 = start
    x2, y2 = end

    if x1 != x2:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
    else:

        k, b = None, None


    x_values = np.linspace(x1, x2, num_points)

    if k is not None and b is not None:

        y_values = k * x_values + b
    else:

        y_values = np.full(shape=num_points, fill_value=x1)


    points = np.column_stack((x_values, y_values))

    return points


def line_wheels_draw(image_name, point_start, point_end, speed, length, anlge, path0):
    os.mkdir(path0)
    num_points = int(length / speed)
    points = seg_line(point_start, point_end, num_points)
    len1 = len(points)
    for i in range(len1):
        image = cv2.imread(image_name)
        drawwheels_x_y(image, points[i], anlge, i, path0)
