from sys import stdin


def firstStar():
  res = 0
  for line in stdin:
    first, second = line.split(',')
    first_lo, first_hi = first.split('-')
    second_lo, second_hi = second.split('-')
    if (int(first_lo) - int(second_lo) < 0):
      #second lo is higher so at best first is larger
      if (int(first_hi) - int(second_hi) >= 0):
        res += 1
      else:
        continue
    elif (int(first_lo) - int(second_lo) > 0):
      #second lo is lower so at best second is larger
      if (int(first_hi) - int(second_hi) <= 0):
        res += 1
    else:
      # second lo == first lo
      res += 1
  print("NUMBER OF TOTAL OVERLAP: ", res)

def secondStar():
  res = 0
  for line in stdin:
    first, second = line.split(',')
    #default second is the higher interval (higher hi)
    first_lo, first_hi = first.split('-')
    second_lo, second_hi = second.split('-')
    if (int(first_hi) > int(second_hi)):
      temp_lo, temp_hi = first_lo, first_hi
      first_lo, first_hi = second_lo, second_hi
      second_lo, second_hi = temp_lo, temp_hi
    # so now second is always higher
    if (int(second_lo) <= int(first_hi)):
      res += 1
  print("NUMBER OF PARTIAL OVERLAP: ", res)


if __name__ == "__main__":
  #firstStar()
  secondStar()