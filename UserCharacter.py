from Cleric import *
from Skill import *

MAX_RANK = 9

class UserCharacter:

    def __init__(self):
        self.jobClass = None
        self.rankNum = 1
        self.jobStack = []
        self.availableJobs = list()

    def getLastJobStack(self):
        return self.jobStack[len(self.jobStack)-1]

    def setMaxClassLevel(self):
        self.getLastJobStack().setMaxClassLevel()

    def increase1rank(self, job):
        if self.rankNum is not MAX_RANK:
            if self.getLastJobStack().classLevel is 15:
                self.rankNum += 1
                jobRankNum = self.getSameClassNum(job) + 1
                self.stacksJobRank(job)
                self.getLastJobStack().setJobRankNum(jobRankNum)
            else:
                print("not in Maximum Class Level!")
        else:
            print("Already in Maximum Rank!")

    def getSameClassNum(self, jobRank):
        result = 0
        for job in self.jobStack:
            if job.__class__ is jobRank.__class__:
                result += 1
        return result

    def stacksJobRank(self, jobRank):
        self.jobStack.append(jobRank)

    def getJobClass(self, jobRank):
        for job in self.jobStack:
            if job.__class__ is jobRank.__class__:
                return job

    def setJobClass(self, jobClass):
        if jobClass is "Cleric":
            self.jobClass = Cleric()
            self.stacksJobRank(Cleric())
            jobs = [Cleric(), Krivi(), Priest(), Bokor(), Dievdirbys(), Paladin(), Sadhu(),
                        Monk(), Pardoner(), Oracle(), Druid(), PlagueDoctor(), Kabbalist(), Daoshi(), Inquisitor(), Zealot()]
            self.availableJobs.extend(jobs)

    def printAvaliableJobs(self):
        result = ""
        for job in self.availableJobs:
            result += "[" + ": " + str(job) + job.jobRankNum + "rank" +"] "
        print(result)

    def printJobStacks(self):
        result = ""
        i = 1
        for job in self.jobStack:
            result += "[" + str(i) + ": " + str(job) + "] "
            i += 1
        print(result)

    def printAvailableSkills(self):
        result = ""
        skills = self.getAvailableActiveSkills()
        for skill in skills:
            result += "[" + str(skill) + "] "
        print(result)

    def getAvailableActiveSkills(self):
        skills = list()
        for job in self.getMaxRanks():
            for skill in job.availableActiveSkills:
                skills.append(skill)
        return skills

    def isSameJobIn(self, jobRank):
        for job in self.jobStack:
            if job.__class__ == jobRank.__class__:
                return True
        return False

    def getMaxRanks(self):
        ranks = set()
        for job in self.jobStack:
            maxNum = self.getSameClassNum(job)
            if job.jobRankNum == maxNum:
                ranks.add(job)
        return ranks

