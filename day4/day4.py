import sys
import re
import numpy as np


def part_1(content):     

    regex = re.compile(r'(?=XMAS|SAMX)')

    regex_count = lambda string: regex.subn(r'',string)[1]
    
    ro,co = content.shape
    num = 0 
    #rows
    num += sum(regex_count(''.join(r)) for r in content)
    #columns
    num += sum(regex_count(''.join(content[:,j])) for j in range(co))
    #main diagonals
    num += sum(regex_count(''.join(content.diagonal(d))) for d in range(-ro+4,co-3))
    #from top-right to bottom-left
    num += sum(regex_count(''.join(np.fliplr(content).diagonal(d))) for d in range(-ro+4,co-3))

    return num



def part_2(content):
    ro,co = content.shape
    is_sm = lambda mat: {mat[0,0], mat[2,2]} == {'S','M'} and {mat[0,2], mat[2,0]} == {'S','M'}

    num = sum(1 for i in range(1,ro-1) for j in range(1,co-1) if content[i,j]=='A' and is_sm(content[i-1:i+2,j-1:j+2]))
    return num

def day_4(filename,first=True):
    
    with open(filename) as file:
        content = np.array([list(l.strip()) for l in file])

    if first:
        return part_1(content)
    
    return part_2(content)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day4 part 1: {day_4(arg, True)}')
        print(f'day4 part 2: {day_4(arg, False)}')