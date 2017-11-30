from Jobs import JobClass
from Skill import *


class Cleric(JobClass):
    def __init__(self, rankNum = 1):
        super(Cleric, self).__init__()
        heal = Skill("Heal", 1)
        heal.addPassive(PassiveSkill("Heal : Improve", 1))
        heal.addPassive(PassiveSkill("Heal : Additional Generate", 1, 5))
        heal.addPassive(PassiveSkill("Heal : Remove Damage", 1, 1))

        cure = Skill("Cure", 1)
        cure.addPassive(PassiveSkill("Cure : Improve", 1))
        cure.addPassive(PassiveSkill("Cure : Damage Period", 2, 1))

        depzone = Skill("Deprotected Zone", 1)
        depzone.addPassive(PassiveSkill("Deprotected Zone : Holding Time", 1, 5))
        depzone.addPassive(PassiveSkill("Deprotected Zone : Sword Attack", 1, 1))
        depzone.addPassive(PassiveSkill("Deprotected Zone : Improve", 1, 50, 3))

        safety = Skill("Safety Zone", 1)
        safety.addPassive(PassiveSkill("Safety Zone : Extend Range", 1, 1))
        safety.addPassive(PassiveSkill("Safety Zone : Defence Count", 2, 20))

        divine = Skill("Divine Might", 2)
        divine.addPassive(PassiveSkill("Divine Might - Demons Damage", 2, 1))

        fade = Skill("Fade", 2)

        patron = Skill("Patron Saint", 3)
        patron.addPassive(PassiveSkill("Patron Saint : Swap Target", 3, 1))
        patron.addPassive(PassiveSkill("Patron Saint : Reduce Damage", 3, 10))

        skills = [heal, cure, depzone, safety, divine, fade, ]
        passiveSkills = [Skill("Weapon Swap", 2), Skill("One handed blunt Mastery : Stun", 1)]
        self.skills.setLockedActiveSkills(skills)
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.setJobRankNum(rankNum)


class Krivi(JobClass):
    def __init__(self):
        super(Krivi, self).__init__()
        self.unlockRank = 2

        aukuras = Skill("Aukuras", 1)
        aukuras.addPassive(PassiveSkill("Aukuras : Improve", 1, 50))
        aukuras.addPassive(PassiveSkill("Aukuras : Fire Resistance", 1, 3))
        aukuras.addPassive(PassiveSkill("Aukuras : Godess of Fire", 2, 1))

        daino = Skill("Daino", 1)
        daino.addPassive(PassiveSkill("Daino : Holding Time", 1, 3))

        zaibas = Skill("Zaibas", 1)
        zaibas.addPassive(PassiveSkill("Zaibas : Splash", 2, 1))
        zaibas.addPassive(PassiveSkill("Zaibas : Improve", 1))

        zalciai = Skill("Zalciai", 1)
        zalciai.addPassive(PassiveSkill("Zalciai : Magical Amplification", 1))
        zalciai.addPassive(PassiveSkill("Zalciai : Improve", 1))
        zalciai.addPassive(PassiveSkill("Zalciai : Holding Time", 1))

        divine = Skill("Divine Stigma", 2)
        divine.addPassive(PassiveSkill("Divine Stigma : Holding Time", 2, 5))
        divine.addPassive(PassiveSkill("Divine Stigma : Improve", 2))
        divine.addPassive(PassiveSkill("Divine Stigma : Punishing Demons", 2, 5, 10))

        melstis = Skill("Melstis", 3)

        skills = [aukuras, daino, zaibas , zalciai, divine, melstis]
        passiveSkills = [PassiveSkill("Krivi : Fire Resistance", 1, 5)]
        self.skills.setLockedActiveSkills(skills)
        self.skills.setLockedPassiveSkills(passiveSkills)


class Priest(JobClass):
    def __init__(self):
        super(Priest, self).__init__()
        self.unlockRank = 2

        monst = Skill("Monstrance", 1)
        monst.addPassive(PassiveSkill("Monstrance : Buff Holding Time", 1, 5))

        resur = Skill("Resurrection", 1)
        resur.addPassive(PassiveSkill("Resurrection : Resurrect Count", 1, 5))

        aspersion = Skill("Aspersion", 1)
        aspersion.addPassive(PassiveSkill("Aspersion : Improve", 1))

        blessing = Skill("Blessing", 1)
        blessing.addPassive(PassiveSkill("Blessing : Additional Buff", 1, 5))
        blessing.addPassive(PassiveSkill("Blessing : Improve", 1))

        massheal = Skill("Mass Heal", 2)

        revive = Skill("Revive", 2)
        revive.addPassive(PassiveSkill("Revive : Holding Time", 2, 5, 2))

        sacrament = Skill("Sacrament", 2)
        sacrament.addPassive(PassiveSkill("Sacrament : Dark Resistance", 2, 5))

        stoneskin = Skill("Stone Skin", 3)

        exorcise = Skill("Exorcise", 3)
        exorcise.addPassive(PassiveSkill("Exorcise : Improve", 3))
        exorcise.addPassive(PassiveSkill("Exorcise : Holding Time", 3, 5))

        skills = [monst, resur, aspersion, blessing, massheal, revive, sacrament, stoneskin, exorcise]
        passiveSkills = [PassiveSkill("Increase Holding Weight", 1, 10)]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)



class Bokor(JobClass):
    def __init__(self):
        super(Bokor, self).__init__()
        self.unlockRank = 3
        effigy = Skill("Effigy", 1)
        effigy.addPassive(PassiveSkill("", 1))

        hexing = Skill("Hexing", 1)

        tet = Skill("Tet Mamak La", 1)

        zombify = Skill("Zombify", 1)

        bwa = Skill("Bwa Kayiman", 2)
        bwa.addPassive(PassiveSkill("Bwa Kayiman : Improve", 2))
        bwa.addPassive(PassiveSkill("Bwa Kayiman : Zombie Defence", 2, 5))

        mackangdal = Skill("Mackangdal", 2)
        mackangdal.addPassive(PassiveSkill("Mackangdal : Reduce stacked damage", 2, 100, 3))

        samdi = Skill("Samdiveve", 2)

        ogu = Skill("Oguveve", 3)

        damballa = Skill("Damballa", 3)
        damballa.addPassive(PassiveSkill("Damballa : Improve", 3))
        damballa.addPassive(PassiveSkill("Damballa : Remove Knock down", 3, 1))
        damballa.addPassive(PassiveSkill("Damballa : Zombie Regeneration Chance", 3, 5))

        skills = [effigy, hexing, tet, zombify, bwa, mackangdal, samdi, ogu, damballa]
        passiveSkills = []
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Dievdirbys(JobClass):
    def __init__(self):
        super(Dievdirbys, self).__init__()
        self.unlockRank = 3
        skills = [Skill("Carve", 1), Skill("Carve Laima", 1), Skill("Carve Vakarine", 1), Skill("Carva Zemina", 1),
                        Skill("Carve Aukuras Koks", 2), Skill("Carve Owl", 2), Skill("Carve Ausirine", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Paladin(JobClass):
    def __init__(self):
        super(Paladin, self).__init__()
        self.unlockRank = 4
        skills = [Skill("Resist Elements", 1), Skill("Restoration", 1), Skill("Smite", 1), Skill("Turn Undead", 1),
                        Skill("Conversion", 2),Skill("Barrier", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Sadhu(JobClass):
    def __init__(self):
        super(Sadhu, self).__init__()
        self.unlockRank = 4
        skills = [Skill("Astral Body Explosion", 1), Skill("Out of body", 1), Skill("Prakriti", 1), Skill("Vashita Siddhi", 1),
                        Skill("Possession", 2),Skill("Transmit Prana", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Monk(JobClass):
    def __init__(self):
        super(Monk, self).__init__()
        self.unlockRank = 5
        skills = [Skill("Double Punch", 1), Skill("Hand Knife", 1), Skill("Iron Skin", 1), Skill("Palm Strike", 1),
                        Skill("1 Inch Punch", 2), Skill("Energy Blast", 2), Skill("God Finger Flicking", 2), Skill("Golden Bell Shield", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Pardoner(JobClass):
    def __init__(self):
        super(Pardoner, self).__init__()
        self.unlockRank = 5
        skills = [Skill("Discern Evil", 1), Skill("Increase Magic DEF", 1), Skill("Indulgentia", 1), Skill("Simony", 1),
                        Skill("Spell Shop", 2).setMaxLevel(5), Skill("Oblation", 2), Skill("Dekatos", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Oracle(JobClass):
    def __init__(self):
        super(Oracle, self).__init__()
        self.unlockRank = 6
        skills = [Skill("Arcane Energy", 1), Skill("Change", 1), Skill("Clairvoyance", 1).setMaxLevel(1), Skill("Counter Spell", 1),
                        Skill("Prophecy", 1), Skill("Resetting", 1).setMaxLevel(1), Skill("Forecast", 1).setMaxLevel(1), Skill("Death Verdict", 2), Skill("Switch Gender", 3).setMaxLevel(1),
                        Skill("Twist of Fate", 3), Skill("Foretell", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Druid(JobClass):
    def __init__(self):
        super(Druid, self).__init__()
        self.unlockRank = 6
        skills = [Skill("Carnivory", 1), Skill("Chorstasmata", 1), Skill("Shape Shifting", 1), Skill("Telepath", 1),
                        Skill("Transform", 2), Skill("Sterea Trofh", 2), Skill("Henge Stone", 3), Skill("Lycanthropy", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class PlagueDoctor(JobClass):
    def __init__(self):
        super(PlagueDoctor, self).__init__()
        self.unlockRank = 7
        skills = [Skill("Fumigate", 1), Skill("Healing Factor", 1), Skill("Incineration", 1), Skill("Beak Mask", 1), Skill("Bloodletting", 1).setMaxLevel(5), Skill("Pandemic", 1),
                        Skill("Plague Vapours", 2), Skill("Disenchent", 2), Skill("Methadone", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Kabbalist(JobClass):
    def __init__(self):
        super(Kabbalist, self).__init__()
        self.unlockRank = 7
        skills = [Skill("Ayin sof", 1), Skill("Gematria", 1).setMaxLevel(1), Skill("Merkabah", 1), Skill("Notarikon", 1).setMaxLevel(1), Skill("Reduce Level", 1).setMaxLevel(1), Skill("Revenged Seven Fold", 1),
                        Skill("Multiple Hit Chance", 2), Skill("Clone", 2), Skill("Gevura", 3)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Daoshi(JobClass):
    def __init__(self):
        super(Daoshi, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Begone Demon", 1), Skill("Creeping Death", 1).setMaxLevel(1), Skill("Dark sight", 1), Skill("Storm Calling", 1), Skill("Tri Disaster", 1),
                        Skill("Divine Punishment", 2), Skill("Elevate magic square", 2)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Inquisitor(JobClass):
    # Nobody expects SPANISH INQUISITION!!
    def __init__(self):
        super(Inquisitor, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Breaking Wheel", 1), Skill("God Smash", 1), Skill("Malleus Maleficarum", 1), Skill("Pear of Anguish", 1),
                        Skill("Iron Maiden", 2), Skill("Judgement", 2)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)


class Zealot(JobClass):
    # My life for AIUR!
    def __init__(self):
        super(Zealot, self).__init__()
        self.unlockRank = 8
        skills = [Skill("Beady Eyed", 1), Skill("Fanaticism", 1), Skill("Immolation", 1), Skill("Invulnerable", 1),
                  Skill("Blind Faith", 2), Skill("Fanatic Illusion", 2)]
        passiveSkills = [Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),
                         Skill("", 1), Skill("", 1), Skill("", 1), Skill("", 1),]
        self.skills.setLockedPassiveSkills(passiveSkills)
        self.skills.setLockedActiveSkills(skills)
