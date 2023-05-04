from collections import deque
class Solution:
    def predictPartyVictory(self,senate):
        n=len(senate)
        # Keep track of the voters indexes ie the radiants and the dires
        radiant=deque()
        dire=deque()
        # loop through the word to take not of the indexes of each voter
        for i,s in enumerate(senate):
            if s=="R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            radiant_idx=radiant.popleft()
            dire_idx=dire.popleft()
            # get the voters indexes and compare them,if the index is lesser than the other
            # add it at the back of the list by the offset of the number of voters in the word
            if radiant_idx < dire_idx:
                radiant.append(radiant_idx+n)
            else:
                dire.append(dire_idx+n)
        return "Radiant" if radiant else "Dire"