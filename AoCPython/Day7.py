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
            findObjList = [x for x in progs if x.name == programDesc[0]]
            if len(findObjList) > 0:
                findObjList[0].weight = int(programDesc[1][1:-1])
                findObjList[0].children = childProgList
            else:
                newProg = Program(programDesc[0], int(programDesc[1][1:-1]), childProgList)
                progs.append(newProg)

            for c in children:
                filtList = [x for x in progs if x.name == c]
                if len(filtList) > 0:
                    filtList[0].parent = newProg
                else:
                    childProg = Program(c, 0)
                    childProg.parent = newProg
                    progs.append(childProg)
        parentLess = [x for x in progs if x.parent == None]
        print(parentLess[0].name)

if __name__ == "__main__":
    AoC7()
