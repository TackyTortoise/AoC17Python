def AoC8():
    with open("Input_08.txt") as f:
        d = dict()
        maxValue = -5000
        for line in f:
            splits = line.split()
            regCheck = splits[4]
            cond = splits[5]
            checkNum = splits[6]
            conditionMet = False
            if (cond == ">"):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue > int(checkNum)
            elif (cond == "<"):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue < int(checkNum)
            elif (cond == ">="):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue >= int(checkNum)
            elif(cond == "=="):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue == int(checkNum)
            elif(cond == "<="):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue <= int(checkNum)
            elif(cond == "!="):
                regValue = d[regCheck] if regCheck in d else 0
                conditionMet = regValue != int(checkNum)

            if not conditionMet:
                continue
            regValue = d[splits[0]] if splits[0] in d else 0
            if (splits[1] == "inc"):
                d[splits[0]] = regValue + int(splits[2])
                if d[splits[0]] > maxValue:
                    maxValue = d[splits[0]]
            elif (splits[1] == "dec"):
                d[splits[0]] = regValue - int(splits[2])
                if d[splits[0]] > maxValue:
                    maxValue = d[splits[0]]

        print("Highest registery value at end: {}".format(d[max(d, key = d.get)]))
        print("Highest value ever in registery: {}".format(maxValue))


if __name__ == "__main__":
    AoC8()