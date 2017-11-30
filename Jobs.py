MAX_JOB_RANK = 3

class JobClass:
    def __init__(self, jobRankNum = 1, unlockRank = 1):
        self.jobRankNum = jobRankNum
        self.unlockRank = unlockRank
        self.classLevel = 1
        self.leftSkillPoint = 1
        self.activeSkills = []
        self.passiveSkills = []
        self.availableActiveSkills = set()
        self.availablePassiveSkills = []
        self.lockedActiveSkills = []

    def increase1rank(self):
        if self.jobRankNum is not MAX_JOB_RANK:
            self.jobRankNum += 1
            self.unlockSkills()
        else:
            print("Already in Maximum Job Rank!")

    def setJobRankNum(self, num):
        if num > 3 or num < 1:
            print("Invalid rank number!")
        else:
            self.jobRankNum = num
            self.unlockSkills()

    def increase1ClassLevel(self):
        if self.classLevel is not 15:
            self.classLevel += 1
            self.leftSkillPoint += 1
        else:
            print("Already in Maximum Class Level!")

    def setMaxClassLevel(self):
        self.classLevel = 15

    def __str__(self):
        return self.__class__.__name__ + " " + str(self.jobRankNum) + " rank, " + str(self.classLevel) + "Lv"

    def unlockSkills(self):
        skills = list(filter(lambda skill : skill.availableRank == self.jobRankNum, self.lockedActiveSkills))
        for unlocked in skills:
            self.lockedActiveSkills.remove(unlocked)
            self.availableActiveSkills.add(unlocked)
