from Jobs import JobClass
from Skill import *


class Cleric(JobClass):
    def __init__(self):
        super(Cleric, self).__init__()
        skills = [Skill("Heal", 1), Skill("Cure", 1), Skill("Deprotected Zone", 1), Skill("Safety Zone", 1),
                        Skill("Divine Might", 2), Skill("Fade", 2), Skill("Patron Saint", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Krivi(JobClass):
    def __init__(self):
        super(Krivi, self).__init__()
        self.unlockRank = 2
        skills = [Skill("Aukuras", 1), Skill("Daino", 1), Skill("Zaibas", 1), Skill("Zalciai", 1),
                        Skill("Divine Stigma", 2), Skill("Melstis", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Priest(JobClass):
    def __init__(self):
        super(Priest, self).__init__()
        self.unlockRank = 2
        skills = [Skill("Monstrance", 1), Skill("Resurrection", 1), Skill("Aspersion", 1), Skill("Blessing", 1),
                        Skill("Mass Heal", 2), Skill("Revive", 2), Skill("Sacrament", 2), Skill("Stone Skin", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Bokor(JobClass):
    def __init__(self):
        super(Bokor, self).__init__()
        self.unlockRank = 3
        skills = [Skill("Effigy", 1), Skill("Hexing", 1), Skill("Tet Mamak La", 1), Skill("Zombify", 1),
                        Skill("Bwa Kayiman", 2), Skill("Mackangdal", 2), Skill("Samdiveve", 2), Skill("Oguveve", 3), Skill("Damballa", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Dievdirbys(JobClass):
    def __init__(self):
        super(Dievdirbys, self).__init__()
        self.unlockRank = 3
        skills = [Skill("Carve", 1), Skill("Carve Laima", 1), Skill("Carve Vakarine", 1), Skill("Carva Zemina", 1),
                        Skill("Carve Aukuras Koks", 2), Skill("Carve Owl", 2), Skill("Carve Ausirine", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Paladin(JobClass):
    def __init__(self):
        super(Paladin, self).__init__()
        self.unlockRank = 4
        skills = [Skill("Resist Elements", 1), Skill("Restoration", 1), Skill("Smite", 1), Skill("Turn Undead", 1),
                        Skill("Conversion", 2),Skill("Barrier", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Sadhu(JobClass):
    def __init__(self):
        super(Sadhu, self).__init__()
        self.unlockRank = 4
        skills = [Skill("Astral Body Explosion", 1), Skill("Out of body", 1), Skill("Prakriti", 1), Skill("Vashita Siddhi", 1),
                        Skill("Possession", 2),Skill("Transmit Prana", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Monk(JobClass):
    def __init__(self):
        super(Monk, self).__init__()
        self.unlockRank = 5
        skills = [Skill("Double Punch", 1), Skill("Hand Knife", 1), Skill("Iron Skin", 1), Skill("Palm Strike", 1),
                        Skill("1 Inch Punch", 2), Skill("Energy Blast", 2), Skill("God Finger Flicking", 2), Skill("Golden Bell Shield", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Pardoner(JobClass):
    def __init__(self):
        super(Pardoner, self).__init__()
        self.unlockRank = 5
        skills = [Skill("Discern Evil", 1), Skill("Increase Magic DEF", 1), Skill("Indulgentia", 1), Skill("Simony", 1),
                        Skill("Spell Shop", 2).setMaxLevel(5), Skill("Oblation", 2), Skill("Dekatos", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Oracle(JobClass):
    def __init__(self):
        super(Oracle, self).__init__()
        self.unlockRank = 6
        skills = [Skill("Arcane Energy", 1), Skill("Change", 1), Skill("Clairvoyance", 1, 1), Skill("Counter Spell", 1),
                        Skill("Prophecy", 1), Skill("Resetting", 1).setMaxLevel(1), Skill("Forecast", 1).setMaxLevel(1), Skill("Death Verdict", 2), Skill("Switch Gender", 3).setMaxLevel(1),
                        Skill("Twist of Fate", 3), Skill("Foretell", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Druid(JobClass):
    def __init__(self):
        super(Druid, self).__init__()
        self.unlockRank = 6
        skills = [Skill("Carnivory", 1), Skill("Chorstasmata", 1), Skill("Shape Shifting", 1), Skill("Telepath", 1),
                        Skill("Transform", 2), Skill("Sterea Trofh", 2), Skill("Henge Stone", 3), Skill("Lycanthropy", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class PlagueDoctor(JobClass):
    def __init__(self):
        super(PlagueDoctor, self).__init__()
        self.unlockRank = 7
        skills = [Skill("Fumigate", 1), Skill("Healing Factor", 1), Skill("Incineration", 1), Skill("Beak Mask", 1), Skill("Bloodletting", 1, 5), Skill("Pandemic", 1),
                        Skill("Plague Vapours", 2), Skill("Disenchent", 2), Skill("Methadone", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Kabbalist(JobClass):
    def __init__(self):
        super(Kabbalist, self).__init__()
        self.unlockRank = 7
        skills = [Skill("Ayin sof", 1), Skill("Gematria", 1, 1), Skill("Merkabah", 1), Skill("Notarikon", 1, 1), Skill("Reduce Level", 1, 1), Skill("Revenged Seven Fold", 1),
                        Skill("Multiple Hit Chance", 2), Skill("Clone", 2), Skill("Gevura", 3)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Daoshi(JobClass):
    def __init__(self):
        super(Daoshi, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Begone Demon", 1), Skill("Creeping Death", 1, 1), Skill("Dark sight", 1), Skill("Storm Calling", 1), Skill("Tri Disaster", 1),
                        Skill("Divine Punishment", 2), Skill("Elevate magic square", 2)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Inquisitor(JobClass):
    # Nobody expects SPANISH INQUISITION!!
    def __init__(self):
        super(Inquisitor, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Breaking Wheel", 1), Skill("God Smash", 1), Skill("Malleus Maleficarum", 1), Skill("Pear of Anguish", 1),
                        Skill("Iron Maiden", 2), Skill("Judgement", 2)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()


class Zealot(JobClass):
    # My life for AIUR!
    def __init__(self):
        super(Zealot, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Beady Eyed", 1), Skill("Fanaticism", 1), Skill("Immolation", 1), Skill("Invulnerable", 1),
                  Skill("Blind Faith", 2), Skill("Fanatic Illusion", 2)]
        self.lockedActiveSkills.extend(skills)
        self.unlockSkills()