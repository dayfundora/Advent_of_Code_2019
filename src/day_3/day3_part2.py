def readFile(fileName):
    fileObj = open(fileName, 'r')
    inputs = fileObj.read().split('\n')
    (path1, path2) = (inputs[0].split(','), inputs[1].split(','))
    fileObj.close()
    return (path1, path2)


def crooss_cables_by_steps(fileName):
    (path1, path2) = readFile('input.txt')

    points_path1 = get_points_path(path1)
    points_path2 = get_points_path(path2)

    crossed_points = cross_points([points_path1, points_path2])

    min_cross_points = min([points_path1[point] + points_path2[point]
                           for point in crossed_points])
    return min_cross_points


def cross_points(points_paths):
    intersection = points_paths.pop()
    for points in points_paths:
        intersection = intersection & points.keys()
    return intersection


def get_points_path(path):
    dic = {}
    (i, j, step) = (0, 0, 0)
    for point in path:
        (dir, steps) = (point[:1], int(point[1:]))
        if dir == 'U':
            for index in range(i, i + steps):
                step += 1
                i += 1
                index += 1
                if (index, j) not in dic:
                    dic[(index, j)] = step
        elif dir == 'D':
            for index in range(i, i - steps, -1):
                step += 1
                i -= 1
                index -= 1
                if (index, j) not in dic:
                    dic[(index, j)] = step
        elif dir == 'R':
            for index in range(j, j + steps):
                step += 1
                j += 1
                index += 1
                if (i, index) not in dic:
                    dic[(i, index)] = step
        elif dir == 'L':
            for index in range(j, j - steps, -1):
                step += 1
                j -= 1
                index -= 1
                if (i, index) not in dic:
                    dic[(i, index)] = step
    return dic


if __name__ == '__main__':
        print(crooss_cables_by_steps('input.txt'))
        # 10554