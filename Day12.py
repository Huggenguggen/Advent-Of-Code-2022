from string import ascii_lowercase
 
 
def part1(path: str):
    the_map, start, end = get_map(path)
    print("part1:", travel_map(the_map, start, 'E', can_go_forward))
 
 
def part2(path: str):
    the_map, start, end = get_map(path)
    print("part2:", travel_map(the_map, end, 'a', can_go_back))
 
 
def travel_map(the_map: list, start: tuple, end: str, cross_function):
    dm = get_distance_matrix(the_map)
    set_distance_matrix_mark(dm, start, 1)
 
    visiting_cells = [start]
    visiting_cells_index = -1
    while True:
        visiting_cells_index += 1
        if visiting_cells_index >= len(visiting_cells):
            break
 
        current = visiting_cells[visiting_cells_index]
 
        if get_map_cell(the_map, current) == end:
            return get_distance_matrix_mark(dm, current) - 1
 
        for target, cell in iterate_surroundings(the_map, current):
            if (
                    cross_function(get_map_cell(the_map, current), get_map_cell(the_map, target))
                    and get_distance_matrix_mark(dm, target) == 0
            ):
                visiting_cells.append(target)
                current_mark = get_distance_matrix_mark(dm, current)
                set_distance_matrix_mark(dm, target, current_mark + 1)
 
 
def get_map(path: str):
    the_map = open(path, 'r').read().split('\n')
    for x, y, cell in iterate_map(the_map):
        if cell == 'S':
            start = (x, y)
 
        elif cell == 'E':
            end = (x, y)
 
    return the_map, start, end
 
 
def iterate_map(the_map: list):
    for y in range(len(the_map)):
        for x in range(len(the_map[0])):
            yield x, y, the_map[y][x]
 
 
def can_cross_index(current: str, target: str):
    transform = {
        'S': 'a',
        'E': 'z',
    }
    current = transform.get(current, current)
    target = transform.get(target, target)
 
    return ascii_lowercase.index(target) - ascii_lowercase.index(current)
 
 
def can_go_forward(current: str, target: str):
    return can_cross_index(current, target) <= 1
 
 
def can_go_back(current: str, target: str):
    return can_cross_index(current, target) >= -1
 
 
def get_distance_matrix(the_map: list):
    return [[0] * len(the_map[0]) for _ in range(len(the_map))]
 
 
def get_map_cell(the_map: list, coord: tuple):
    x, y = coord
    if x < 0 or y < 0:
        return None
    try:
        return the_map[y][x]
    except:
        return None
 
 
def iterate_surroundings(the_map: list, coord: tuple):
    x, y = coord
    for i in ((x + 1, y + 0), (x - 1, y + 0), (x + 0, y + 1), (x + 0, y - 1)):
        if (value := get_map_cell(the_map, i)) is not None:
            yield i, value
 
 
def get_distance_matrix_mark(dm: list, coord: tuple):
    x, y = coord
    return dm[y][x]
 
 
def set_distance_matrix_mark(dm: list, coord: tuple, value: int):
    x, y = coord
    dm[y][x] = value
 
 
def get_lowest_result(results: list):
    return min([x for x in results if x >= 0])
 
 
if __name__ == '__main__':
    # file = 'day12-example.txt'
    file = 'inputs/day_12_input.txt'
    part1(file)  
    part2(file)  