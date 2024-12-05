import heapq
import sys

def part_1(locations):

    left = []
    right = []
    heapq.heapify(left)
    heapq.heapify(right)

    for location in locations:
        l, r = location
        heapq.heappush(left,  l)
        heapq.heappush(right, r)

    distance = 0
    while left and right:
        l = heapq.heappop(left)
        r = heapq.heappop(right)
        distance += abs(l-r)

    return distance

def part_2(locations):
    left = set()
    right = dict()
    total = 0
    for location in locations:
        l, r = location
        left.add(l)
        right[r] = right.get(r,0)+1
    for n in left:
        total += n * right.get(n,0)
    return total

def day_1(filename, first=True):
    locations = []

    with open(filename) as file:
        for line in file:
            l, r = list(map(int,line.split()))
            locations.append((l,r))

    if first:
        return part_1(locations)
    
    return part_2(locations)

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(f'day1 part 1: {day_1(arg, True)}')
        print(f'day1 part 2: {day_1(arg, False)}')
