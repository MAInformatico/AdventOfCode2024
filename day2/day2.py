import sys

def check_valid_report(levels):
    is_increasing = check_increasing_sequence(levels)
    is_decreasing = check_decreasing_sequence(levels)

    if not is_increasing and not is_decreasing:
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        if diff < 1 or diff > 3:
            return False

    return True

    
def check_increasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True


def check_decreasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            return False
    return True



def part_1(reports):
    safes_reports = 0       
    
    for report in reports:
        levels = list(map(int, report))
        if check_valid_report(levels):
            safes_reports += 1
            
    return safes_reports      

def part_2(reports):
    safes_reports = 0

    for report in reports:
        levels = list(map(int, report))
        if check_valid_report(levels):
            safes_reports += 1
            continue

        validate_with_dampener = False
        for i in range(len(levels)):            
            edited_report = [x for j, x in enumerate(levels) if j != i]
            
            if check_valid_report(edited_report):
                validate_with_dampener = True
                break

        if validate_with_dampener:
            safes_reports += 1
    return safes_reports



def day_2(filename, first=True):
    reports = []

    with open(filename) as file:
        reports = [line.split() for line in file]

    if first:
        return part_1(reports)
    
    return part_2(reports)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day2 part 1: {day_2(arg, True)}')
        print(f'day2 part 2: {day_2(arg, False)}')