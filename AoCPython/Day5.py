def AoC5():
    part2 = True
    with open("Input_05.txt") as f:
        nums = [int(v) for v in f.readlines()]
        curIndex = 0
        steps = 0
        while curIndex >= 0 and curIndex < len(nums):
            offset = nums[curIndex]
            nums[curIndex] += -1 if part2 and offset >= 3 else 1
            curIndex += offset
            steps += 1
        print(steps)

if __name__ == "__main__":
    AoC5()
