from collections import deque

def process(lines, Monkeys):
    idx = 0
    for line in lines:
      line = line.strip()
      if line.startswith("Monkey"):
        idx = int(line[-2])
      #print("idx", idx)
      elif "Starting items" in line:
        items = line.split(" ")
        items = items[2:]
        items = deque([int(item.replace(",", "")) for item in items])
      #print("items", items)
        if idx not in Monkeys:
          Monkeys[idx] = []
        Monkeys[idx].append(items)
      elif "Operation" in line:
        operation = line.split(" ")
        operation = operation[1:]
        op = None
        if operation[-2] == '*':
          if operation[-1].isnumeric():
            op = lambda x: x * int(operation[-1])
          else:
            op = lambda x: x * x
        elif operation[-2] == '+':
          op = lambda x: x + int(operation[-1])
        #print("TESTING OP with 1:", op(1))
        Monkeys[idx].append(op)
      elif "Test" in line:
        test = line.split(" ")
        test = int(test[-1])
        test_func = lambda x: x % test == 0
        #print("TESTING test with 5:", test_func(5))
        Monkeys[idx].append(test_func)
      elif "true" in line:
        line = line.split(" ")
        if_true = int(line[-1])
        Monkeys[idx].append(if_true)
      elif "false" in line:
        line = line.split(" ")
        if_false = int(line[-1])
        Monkeys[idx].append(if_false)

    return Monkeys

def manual(Monkeys):
  Monkeys[0] = []
  Monkeys[0].append(deque([80]))
  Monkeys[0].append(lambda x: x * 5)
  Monkeys[0].append(lambda x: x % 2 == 0)
  Monkeys[0].append(4)
  Monkeys[0].append(3)
  Monkeys[1] = []
  Monkeys[1].append(deque([75, 83, 74]))
  Monkeys[1].append(lambda x: x + 7)
  Monkeys[1].append(lambda x: x % 7 == 0)
  Monkeys[1].append(5)
  Monkeys[1].append(6)
  Monkeys[2] = []
  Monkeys[2].append(deque([86, 67, 61, 96, 52, 63, 73]))
  Monkeys[2].append(lambda x: x + 5)
  Monkeys[2].append(lambda x: x % 3 == 0)
  Monkeys[2].append(7)
  Monkeys[2].append(0)
  Monkeys[3] = []
  Monkeys[3].append(deque([85, 83, 55, 85, 57, 70, 85, 52]))
  Monkeys[3].append(lambda x: x + 8)
  Monkeys[3].append(lambda x: x % 17 == 0)
  Monkeys[3].append(1)
  Monkeys[3].append(5)
  Monkeys[4] = []
  Monkeys[4].append(deque([67, 75, 91, 72, 89]))
  Monkeys[4].append(lambda x: x + 4)
  Monkeys[4].append(lambda x: x % 11 == 0)
  Monkeys[4].append(3)
  Monkeys[4].append(1)
  Monkeys[5] = []
  Monkeys[5].append(deque([66, 64, 68, 92, 68, 77]))
  Monkeys[5].append(lambda x: x * 2)
  Monkeys[5].append(lambda x: x % 19 == 0)
  Monkeys[5].append(6)
  Monkeys[5].append(2)
  Monkeys[6] = []
  Monkeys[6].append(deque([97, 94, 79, 88]))
  Monkeys[6].append(lambda x: x * x)
  Monkeys[6].append(lambda x: x % 5 == 0)
  Monkeys[6].append(2)
  Monkeys[6].append(7)
  Monkeys[7] = []
  Monkeys[7].append(deque([77, 85]))
  Monkeys[7].append(lambda x: x + 6)
  Monkeys[7].append(lambda x: x % 13 == 0)
  Monkeys[7].append(4)
  Monkeys[7].append(0)
  modulo = 13 * 5 * 19 * 11 * 17 * 3 * 7 * 2
  return Monkeys, modulo
  

def firstStar(lines):
  Monkeys = {}
  #Monkeys = process(lines, Monkeys)
  Monkeys, modulo = manual(Monkeys)
  # first elem is items holding
  # second elem is operation
  # third is test
  # fourth and fifth is true and false res
  inspect = [0] * len(Monkeys)
  for _ in range(10000):
    for monke in range(len(Monkeys)):
      things = Monkeys[monke]
      #print("THINGS.", things)
      while len(things[0]) > 0:
        curr = things[0].popleft()
        #print("THINGS[1]", things[1](3))
        curr = things[1](curr)
        #print("curr", curr)
        #curr = curr // 3
        #print("MONKEY", monke, "curr item thrown", curr)
        curr = curr % modulo
        if things[2](curr):
          Monkeys[things[3]][0].append(curr)
        else:
          Monkeys[things[4]][0].append(curr)
        inspect[monke] += 1
    print("\nROUND: ", _)
    #print("CURRENT STATE: \n", Monkeys)
  print(inspect)
  inspect = sorted(inspect)
  print("MONKEY BUSINESS: ", inspect[-1] * inspect[-2])


def secondStar(lines):
  monkeyOperations = [(lines[x][23:]) for x in range(2, len(lines), 7)]
  monkeyTest = [int(lines[x][21:]) for x in range(3, len(lines), 7)]
  monkeyConditions = [[int(lines[x][29:]), int(lines[x+1][30:])] for x in range(4, len(lines), 7)]

  modulo = 1
  for i in monkeyTest:
      modulo *= i

  def main(part):
    monkeyInspections = [0 for _ in range(len(monkeyTest))]
    monkeyItems = [[[int(x) for x in (lines[y][18:]).split(", ")] for y in range(1, len(lines), 7)]][0]
    for _ in range(0, (20 if part == 1 else 10000 if part == 2 else 0)):
        for i in range(0, len(monkeyInspections)):
            for j in range(0, len(monkeyItems[i])):
                current = monkeyItems[i][j]
                if monkeyOperations[i] == "* old":
                    current *= current
                elif monkeyOperations[i][:2] == "* ":
                    current *= int(monkeyOperations[i][2:])
                elif monkeyOperations[i][:2] == "+ ":
                    current += int(monkeyOperations[i][2:])
                current = current // 3 if part == 1 else current % modulo
                if current % monkeyTest[i] == 0:
                    monkeyItems[monkeyConditions[i][0]].append(current)
                else:
                    monkeyItems[monkeyConditions[i][1]].append(current)
                monkeyInspections[i] += 1
            monkeyItems[i] = []
    return sorted(monkeyInspections)[-1]*sorted(monkeyInspections)[-2]
  print("PART 1: ", main(1))
  print("PART 2: ", main(2))


if __name__ == "__main__":
  with open("inputs/day_11_input.txt") as f:
    lines = f.read().splitlines()
  firstStar(lines)
  secondStar(lines)