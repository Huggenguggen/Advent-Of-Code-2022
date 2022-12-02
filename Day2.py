from sys import stdin

ShapePoints = {"X": 1, "Y": 2, "Z": 3} #Rock paper sciccors
WinPoints = {"W": 6, "D": 3, "L": 0} # win draw loss
WinCondition = {"X": [0, 2], "Y": [3, 0], "Z": [6, 1]} # Gives winPoints and how many to add to opponent shape
Opponent = {"A": 0, "B": 1, "C": 2}

def firstStar():
  points = 0
  for line in stdin:
    line.strip()
    a, b = line.split(" ")
    b = b[0]
    points += ShapePoints[b] #points for shape chosen
    # compare the ORD of the char, diff of 23 between A and X
    a_val = ord(a)
    b_val = ord(b) - 23
    if (a_val - b_val == -2):
      points += WinPoints["L"]
    elif (a_val - b_val == 2):
      points += WinPoints["W"]
    else:
      res = a_val - b_val
      if res == 0:
        points += WinPoints["D"]
      elif res == 1:
        points += WinPoints["L"]
      else:
        points += WinPoints["W"]
    #print("a: ", a)
    #print("b: ", b)
  
def secondStar():
  points = 0
  for line in stdin:
    line.strip()
    a, b  = line.split(" ")
    b = b[0]
    check = WinCondition[b]
    points += check[0]
    points += ((Opponent[a] + check[1]) % 3) + 1
    

  print("POINTS: ", points)

if __name__ == "__main__":
  #firstStar()
  secondStar()


