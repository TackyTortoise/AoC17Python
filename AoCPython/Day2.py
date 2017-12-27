def AoC2():
    checkSum = 0
    checkSum2 = 0
    with open("Input_02.txt") as f:
        for line in f:
            nums = [int(s) for s in line.split() if s.isdigit()]
            checkSum += max(nums) - min(nums)
            for x in nums:
                for y in nums:
                    if x != y and x % y == 0:
                        checkSum2 += x // y
                        break
                else:
                    continue
                break
    
    print("Solution part 1: {}".format(checkSum))
    print("Solution part 2: {}".format(checkSum2))

if __name__ == "__main__":
    AoC2()
