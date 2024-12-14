import sys
import re

def part_1(mul_list):
    
    total = 0
    for operation in mul_list:        
        total += int(operation[0])*int(operation[1])        
    return total

def part_2(mul_list):
    is_enabled = True  # At the start, mul instructions are enabled
    total = 0

    for match in mul_list:
        if match == "do()":
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        elif match.startswith("mul") and is_enabled:
            x, y = get_numbers(match)
            total += x * y
    return total

def get_numbers(match):
    numbers = re.findall(r"\d{1,3}", match)
    return int(numbers[0]), int(numbers[1])

def day_3(filename, first=True):    
    mul_list = []

    with open(filename) as file:
        content = [line.split() for line in file]
    #Parsing text
    mul_list = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", str(content))
    
    if first:
        return part_1(mul_list)
    
    mul_list = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", str(content))
    return part_2(mul_list)




if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day3 part 1: {day_3(arg, True)}')
        print(f'day3 part 2: {day_3(arg, False)}')