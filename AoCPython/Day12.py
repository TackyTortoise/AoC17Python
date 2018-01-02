class Program:
    def __init__(self, programId, progChildren=None):
        self.id = programId
        self.children = progChildren if progChildren is not None else list()

def GetChildren(startProgram, programList):
    allChildren = list()
    if startProgram not in programList:
        return allChildren
    programList.remove(startProgram)
    for cp in [x for x in programList for ci in startProgram.children if x.id == ci]:
        startProgram.children.remove(cp.id)
        allChildren += GetChildren(cp, programList)

    allChildren.append(startProgram.id)
    return allChildren

def AoC12():
    with open("Input_12.txt") as f:
        programs = list()
        for line in f:
            splits = line.split(" <-> ")
            progId = int(splits[0])
            children = [int(s) for s in splits[1].split(", ")]
            programs.append(Program(progId, children))

        programsInFirst = -1
        programCount = 0
        while len(programs) > 0:
            programCount += 1
            c = GetChildren(programs[0], programs)
            if programsInFirst == -1:
                programsInFirst = len(c)
        
        print("Programs in group 0: {}".format(programsInFirst))
        print("Amount of program groups: {}".format(programCount))

if __name__ == "__main__":
    AoC12()
