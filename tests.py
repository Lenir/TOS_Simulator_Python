from UserCharacter import *
from Cleric import *
import unittest

class TestCharRank(unittest.TestCase):
    def testChar(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        # user.printJobStacks()
        # user.printAvailableSkills()
        self.assertEqual(2, user.rankNum)

    def test2RankCleric(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        # user.printJobStacks()
        # user.printAvailableSkills()
        self.assertEqual(2, user.jobStack[1].jobRankNum)

    def test3RankCKC(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        # user.printJobStacks()
        # user.printAvailableSkills()
        self.assertEqual(2, user.jobStack[2].jobRankNum)

    def test4RankCKKC(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        # user.printJobStacks()
        # user.printAvailableSkills()
        # user.printAvaliableJobs()
        self.assertEqual(2, user.jobStack[2].jobRankNum)

    def test5RankCKKCC(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        # user.printJobStacks()
        # user.printAvailableSkills()
        # user.printAvaliableJobs()
        self.assertEqual(2, user.jobStack[2].jobRankNum)


    def test4RankCKKKP(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Krivi())

        user.setMaxClassLevel()
        user.increase1rank(Paladin())

        # user.printJobStacks()
        # user.printAvailableSkills()
        # user.printAvaliableJobs()
        self.assertEqual(2, user.jobStack[2].jobRankNum)

    def test9RankCCCBBBPPP(self):
        user = UserCharacter()
        user.setJobClass("Cleric")

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        user.setMaxClassLevel()
        user.increase1rank(Cleric())

        user.setMaxClassLevel()
        user.increase1rank(Bokor())

        user.setMaxClassLevel()
        user.increase1rank(Bokor())

        user.setMaxClassLevel()
        user.increase1rank(Bokor())

        user.setMaxClassLevel()
        user.increase1rank(PlagueDoctor())

        user.setMaxClassLevel()
        user.increase1rank(PlagueDoctor())

        user.setMaxClassLevel()
        user.increase1rank(PlagueDoctor())

        user.printJobStacks()
        user.printAvailableSkills()
        user.printAvaliableJobs()
        self.assertEqual("PlagueDoctor", user.getLastJobStack().__class__.__name__)

if __name__ == "__main__":
    unittest.main()