def readFile(fileName):
    fileObj = open(fileName, 'r')
    inputs = fileObj.read().splitlines()
    fileObj.close()
    return inputs


def calculate_fuel(masa):
    return masa // 3 - 2


def fuel_requirement(masas, function_calculate_fuel):
    return sum([function_calculate_fuel(int(m)) for m in masas])


def spaceship_fuel(fileName,
                          function_calculate_fuel=calculate_fuel):
    masas = readFile(fileName)
    return fuel_requirement(masas,
                                   function_calculate_fuel)


if __name__ == '__main__':
    print(spaceship_fuel('input.txt'))
    # 3380731
