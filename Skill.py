class Skill:
    def __init__(self, name, availableRank):
        self.name = name
        self.curLevel = 0
        self.maxLevel = 15 - (availableRank-1)*5
        self.availableRank = availableRank

    def setMaxLevel(self, maxLevel):
        self.maxLevel = maxLevel

    def __str__(self):
        return self.name
