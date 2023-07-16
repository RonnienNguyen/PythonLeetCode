class Solution:
    usedDict = {}  # A map used to store the state of the game. {key : True/False}, key represents a state
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True
        
        used = ['0' for _ in range(maxChoosableInteger + 1)]
          
        return self.helper(used, desiredTotal)
    
    def helper(self, used, desiredTotal):
        if desiredTotal <= 0:  # If the desiredTotal <= 0 means total has reached initial target, so lose
            return False
        
        key = self.transform(used)  # key is an integer tranformed by used, representing the selecting situation 
        
        if key not in self.usedDict:  # if this situation didn't appear before
            for n in range(1, len(used)):
                if used[n] != '1':
                    used[n] = '1'
                    if not self.helper(used, desiredTotal - n):
                        self.usedDict[key] = True
                        used[n] = '0'
                        return True
                    
                    used[n] = '0'
            
            self.usedDict[key] = False
        
        return self.usedDict.get(key)
    
    def transform(self, used):
        string = ''.join(used)
        return int(string, 2)