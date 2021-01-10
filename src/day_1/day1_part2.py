def calculate_fuel_forgetful_elf(masa):
    total_fuel = 0
    masa = calculate_fuel(masa)

    while masa > 0:
        total_fuel += masa
        masa = calculate_fuel(masa)

    return total_fuel


if __name__ == '__main__':
    from day1_part1 import calculate_fuel, spaceship_fuel
    print(spaceship_fuel('input.txt', calculate_fuel_forgetful_elf))
    # 5068210