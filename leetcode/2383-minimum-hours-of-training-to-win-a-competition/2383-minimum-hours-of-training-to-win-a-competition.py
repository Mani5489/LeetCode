class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        ee = 0
        if initialEnergy < (sum(energy) + 1):
            ee = (sum(energy) + 1) - initialEnergy
        et = 0
        for opp in experience:
            if initialExperience > opp:
                initialExperience += opp
            elif initialExperience <= opp:
                while initialExperience <= opp:
                    initialExperience += 1
                    et += 1
                if initialExperience > opp:
                    initialExperience += opp
        return ee + et


        