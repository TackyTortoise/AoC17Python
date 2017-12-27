def AoC4():
    validLines = 0
    part1 = False
    with open("Input_03.txt") as f:
        for line in f:
            w = line.split() if part1 else [sorted(s) for s in line.split()]
            for i, x in enumerate(w):
                if x in w[:i] + w[i + 1:]:
                    break
            else:
                validLines += 1

    print(validLines)

if __name__ == "__main__":
    AoC4()
