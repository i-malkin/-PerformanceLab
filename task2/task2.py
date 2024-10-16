import math
import sys


def get_circle_data(file1):
    with open(file1, 'r') as f:
        x_c, y_c, r = map(float, f.read().split())
    return x_c, y_c, r


def get_points_data(file2):
    points = []
    with open(file2, 'r') as f:
        for line in f:
            points.append(tuple(map(float, line.split())))
    return points


def check_point_position(x_c, y_c, r, x_p, y_p):
    distance = math.sqrt((x_p - x_c) ** 2 + (y_p - y_c) ** 2)

    if distance == r:
        return 0  # точка на окружности
    elif distance < r:
        return 1  # точка внутри
    else:
        return 2  # точка снаружи

def main():
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    x_c, y_c, r = get_circle_data(file1)
    points = get_points_data(file2)

    for x_p, y_p in points:
        result = check_point_position(x_c, y_c, r, x_p, y_p)
        print(result)


if __name__ == "__main__":
    main()

