def AoC6():
    part2 = True
    with open("Input_06.txt") as f:
        nums = [int(n) for n in f.read().split('\t')]
        seen = list()
        firstTimeIteration = 0
        for i in range(2 if part2 else 1):
            while nums not in seen:
                seen.append(nums[:])
                maxV = max(nums)
                maxI = nums.index(maxV)
                nums[maxI] = 0
                while maxV > 0:
                    maxI += 1
                    nums[maxI % len(nums)] += 1
                    maxV -= 1     
            if i == 0 and part2:
                 seen.clear()
        print(len(seen) - firstTimeIteration)

if __name__ == "__main__":
    AoC6();
