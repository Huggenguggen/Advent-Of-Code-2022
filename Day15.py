def possible(x, y):
    if x < 0 or x > 4000000 or y < 0 or y > 4000000:
      return False
    for sx, sy, d in sensors:
        if abs(x - sx) + abs(y - sy) <= d and (x, y) not in beacons:
            return False
    return True

def p1():
    ct = 0
    y = 2_000_000
    for x in range(min(x-d for x, _, d in sensors), max(x+d for x, _, d in sensors)):
        if not possible(x, y) and (x, y) not in beacons:
            ct += 1
    return ct

def p2():
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in [(-1, 1), (1, -1), (-1, -1), (1, 1)]:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not(0 <= 4_000_000 and 0<=y<=4_000_000):
                    continue
                if possible(x, y):
                    print("x:",x,"y:",y)
                    return x * 4_000_000 + y

data = open("inputs/day_15_input.txt").read().strip()
sensors, beacons = set(), set()
for line in data.split("\n"):
    parts = line.split()
    sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
    bx, by = int(parts[8][2:-1]), int(parts[9][2:])
    d = abs(sx - bx) + abs(sy - by)
    sensors.add((sx, sy, d))
    beacons.add((bx, by))
print(f"Part 1: {p1()}")
print(f"Part 2: {p2()}")