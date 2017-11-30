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
                self.stacksJobRank(job)
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
        if self.isSameJobIn(jobRank):
            rankNum = self.getSameClassNum(jobRank) + 1
            self.jobStack.append(jobRank)
            self.getLastJobStack().setJobRankNum(rankNum)
            if rankNum == 3:
                self.availableJobs.remove(self.getJobInAvailables(jobRank))
            else:
                self.getJobInAvailables(jobRank).setJobRankNum(rankNum + 1)
        else:
            self.jobStack.append(jobRank)
            self.getJobInAvailables(jobRank).setJobRankNum(2)
        self.getLastJobStack().unlockSkills()

    def getJobClass(self, jobRank):
        for job in self.jobStack:
            if job.__class__ is jobRank.__class__:
                return job

    def getJobInAvailables(self, jobRank):
        for job in self.availableJobs:
            if jobRank.__class__ == job.__class__:
                return job

    def setJobClass(self, jobClass):
        if jobClass is "Cleric":
            self.jobClass = Cleric()
            jobs = [Cleric(), Krivi(), Priest(), Bokor(), Dievdirbys(), Paladin(), Sadhu(),
                    Monk(), Pardoner(), Oracle(), Druid(), PlagueDoctor(), Kabbalist(), Daoshi(), Inquisitor(),
                    Zealot()]
            self.availableJobs.extend(jobs)
            self.stacksJobRank(Cleric())


    def printAvaliableJobs(self):
        result = "Avaliable Jobs : "
        for job in self.availableJobs:
            if job.unlockRank <= self.rankNum:
                result += "[" + str(job.__class__.__name__) + " " +str(job.jobRankNum) + "rank" +"] "
        print(result)

    def printJobStacks(self):
        result = ""
        i = 1
        for job in self.jobStack:
            result += "[" + str(i) + ": " + str(job) + "] "
            i += 1
        print(result)

    def printAvailableActiveSkills(self):
        result = "Active : "
        skills = self.getAvailableActiveSkills()
        for skill in skills:
            result += "[" + str(skill) + "] "
        print(result)

    def printAvailablePassiveSkills(self):
        result = "Passive : "
        skills = self.getAvailablePassiveSkills()
        for skill in skills:
            result += "[" + str(skill) + "] "
        print(result)

    def getAvailableActiveSkills(self):
        skills = list()
        for job in self.getMaxRanks():
            for skill in job.skills.availableActiveSkills:
                skills.append(skill)
        return skills

    def getAvailablePassiveSkills(self):
        skills = list()
        for job in self.getMaxRanks():
            for skill in job.skills.availablePassiveSkills:
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

