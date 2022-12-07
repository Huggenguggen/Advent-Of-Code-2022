from collections import defaultdict

def firstStar(lines):
  dir = defaultdict(int)
  root = []
  for line in lines:
    match line.split():
      case ['$', 'cd', '..']:
        root.pop()
      case ['$', 'cd', p]:
        root.append(p)
      case['$', 'ls']:
        pass
      case ['dir', p]:
        pass 
      case [s, f]:
        dir[tuple(root)] += int(s)
        # add file size to each parent
        path = root[:-1]
        while path:
          dir[tuple(path)] += int(s)
          path.pop()

  #part 1
  print("FIRST PART: ", sum([d for d in dir.values() if d <= 100000]))       

def secondStar(lines):
  dir = defaultdict(int)
  root = []
  for line in lines:
    match line.split():
      case ['$', 'cd', '..']:
        root.pop()
      case ['$', 'cd', p]:
        root.append(p)
      case['$', 'ls']:
        pass
      case ['dir', p]:
        pass 
      case [s, f]:
        dir[tuple(root)] += int(s)
        # add file size to each parent
        path = root[:-1]
        while path:
          dir[tuple(path)] += int(s)
          path.pop()

  #part 1
  free = 70000000 - dir[('/',)]
  print("SECOND PART: ", min([d for d in dir.values() if d + free >= 30000000])) 


if __name__ == "__main__":
  with open("inputs/day_7_input.txt") as f:
    lines = f.readlines()
  firstStar(lines) 
  secondStar(lines)