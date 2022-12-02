from sys import stdin


ShapePoints = {"X": 1, "Y": 2, "Z": 3} #Rock paper sciccors
WinPoints = {"W": 6, "D": 3, "L": 0} # win draw loss

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
  

  print("POINTS: ", points)

if __name__ == "__main__":
  firstStar()


