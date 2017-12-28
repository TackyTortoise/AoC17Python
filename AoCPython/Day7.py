class Program:
    def __init__(self, name, weight, children = None):
        self.name = name
        self.weight = weight
        self.children = children if children is not None else []
        self.parent = None
    def __str__(self):
        return ""

def AoC7():
    with open("Input_07.txt") as f:
        progs = []
        for line in f:
            split = line.strip().split(" -> ")
            programDesc = split[0].split(" ")
            children = split[1].split(", ") if len(split) > 1 else []
            childProgList = [x for x in progs for cn in children if x.name == cn]
            findObj = next((x for x in progs if x.name == programDesc[0]), None)
            if findObj is not None:
                findObj.weight = int(programDesc[1][1:-1])
                findObj.children = childProgList
            else:
                newProg = Program(programDesc[0], int(programDesc[1][1:-1]), childProgList)
                progs.append(newProg)

            for c in children:
                firstChildMatch = next((x for x in progs if x.name == c), None)
                if firstChildMatch is not None:
                    firstChildMatch.parent = newProg
                else:
                    childProg = Program(c, 0)
                    childProg.parent = newProg
                    progs.append(childProg)

        parentLess = next((x for x in progs if x.parent == None), None)
        print(parentLess.name)

if __name__ == "__main__":
    AoC7()
