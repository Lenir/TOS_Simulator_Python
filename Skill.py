class Skill:
    def __init__(self, name, availableRank):
        self.name = name
        self.curLevel = 0
        self.maxLevel = 15 - (availableRank-1)*5
        self.availableRank = availableRank
        self.passiveSkills = list()

    def setMaxLevel(self, maxLevel):
        self.maxLevel = maxLevel
        return self

    def addPassive(self, passiveSkill):
        self.passiveSkills.append(passiveSkill)

    def __str__(self):
        return self.name

class PassiveSkill:
    def __init__(self, name, availableRank, maxLevel = 100, requireLevel = 1):
        self.name = name
        self.curLevel = 0
        self.maxLevel = maxLevel
        self.availableRank = availableRank
        self.requireLevel = requireLevel

    def setMaxLevel(self, maxLevel):
        self.maxLevel = maxLevel
        return self

    def __str__(self):
        return self.name