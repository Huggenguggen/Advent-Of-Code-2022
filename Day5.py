

def load_data(lines):
    vals = {i_bin+1: [c for l in lines if '[' in l and (c := l[i_bin*4+1]) != ' '][::-1] for i_bin in range(len(lines[0])//4)}
    instructions = [[int(l.strip().split(' ')[i]) for i in (1,3,5)] for l in lines if l[0] == 'm'] 
    return vals, instructions

def firstStar(lines):
  (d1, inst), (d2, _) = load_data(lines), load_data(lines)
  for n, f, t in inst:
    d1[t].extend([d1[f].pop() for i in range(n)])
    d2[t].extend([d2[f].pop(i) for i in range(-n,0)])
  for i, d in enumerate((d1, d2)):
    print(f'{i})\t' + ''.join(d[i+1].pop() for i in range(len(d))))


if __name__ == "__main__":
  with open("inputs/day_5_input.txt") as f:
    lines = f.readlines()
  firstStar(lines)