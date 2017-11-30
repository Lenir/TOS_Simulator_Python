class Skills:
    def __init__(self):
        self.activeSkills = []
        self.passiveSkills = []
        self.availableActiveSkills = set()
        self.availablePassiveSkills = set()
        self.lockedActiveSkills = []
        self.lockedPassiveSkills = []

    def unlockActiveSkill(self, skill):
        self.lockedActiveSkills.remove(skill)
        self.availableActiveSkills.add(skill)

    def unlockPassiveSkill(self, skill):
        self.lockedPassiveSkills.remove(skill)
        self.availablePassiveSkills.add(skill)


    def setLockedActiveSkills(self, locked):
        self.lockedActiveSkills.extend(locked)

    def setLockedPassiveSkills(self, locked):
        self.lockedPassiveSkills.extend(locked)