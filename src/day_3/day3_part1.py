def readFile(fileName):
    fileObj = open(fileName, 'r')
    inputs = fileObj.read().split('\n')
    (path1, path2) = (inputs[0].split(','), inputs[1].split(','))
    fileObj.close()
    return (path1, path2)


def cross_cables(fileName):
    (path1, path2) = readFile('input.txt')

    points_paths = [get_points_path(path) for path in [path1, path2]]
    crossed_points = cross_points(points_paths)

    min_cross_points = min([abs(i) + abs(j) for (i, j) in
                           crossed_points])
    return min_cross_points


def cross_points(points_paths):
    intersection = points_paths.pop()
    for points in points_paths:
        intersection = intersection & points.keys()
    return intersection


def get_points_path(path):
    dic = {}
    (i, j) = (0, 0)
    for point in path:
        (dir, steps) = (point[:1], int(point[1:]))
        if dir == 'U':
            for index in range(i, i + steps):
                i += 1
                index += 1
                dic[(index, j)] = True
        elif dir == 'D':
            for index in range(i - steps + 1, i + 1):
                i -= 1
                index -= 1
                dic[(index, j)] = True
        elif dir == 'R':
            for index in range(j, j + steps):
                j += 1
                index += 1
                dic[(i, index)] = True
        elif dir == 'L':
            for index in range(j - steps + 1, j + 1):
                j -= 1
                index -= 1
                dic[(i, index)] = True
    return dic


if __name__ == '__main__':
        print(cross_cables('input.txt'))
        # 280