import math

def read_points(file_name):
    points_list = []
    with open(file_name, 'r') as file:
        for line in file:
            points = map(int, line.strip().split())
            points_list.append([tuple(points[i:i+2]) for i in range(0, len(points), 2)])
    return points_list

def find_start_point(points):
    min_y = float('inf')
    start_point = None
    for point in points:
        x, y = point
        if y < min_y:
            min_y = y
            start_point = point
        elif y == min_y and x < start_point[0]:
            start_point = point
    return start_point

def sort_points(points, start_point):
    angles = {}
    for point in points:
        angle = math.atan2(point[1] - start_point[1], point[0] - start_point[0])
        angles[point] = angle
    return [point for point, _ in sorted(angles.items(), key=lambda item: item[1])]

def is_parallel(p1, p2, p3, p4):
    dx1 = p1[0] - p2[0]
    dy1 = p1[1] - p2[1]
    dx2 = p3[0] - p4[0]
    dy2 = p3[1] - p4[1]
    cross_product = dx1 * dy2 - dy1 * dx2
    return cross_product == 0

def check_parallelogram(input_file, output_file):
    points_list = read_points(input_file)
    with open(output_file, 'w') as out:
        for points in points_list:
            if len(set(points)) == 1:
                continue
            start_point = find_start_point(points)
            sorted_points = sort_points(points, start_point)
            p1, p2, p3, p4 = sorted_points[:4]
            if is_parallel(p1, p2, p3, p4):
                out.write("1\n")
            else:
                out.write("0\n")

check_parallelogram("parallelogram.inp", "parallelogram.out")

