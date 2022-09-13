class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        '''
        1. convert all data into binary form
        2. on each data[i], we have 2 choices:
            i. if we are in the middle of a verification => then check if the first two bits are '10'
            ii. if we are to start a new verification => count the num of 1s from the left
        3. Corner Cases: nBytes == 1 or nBytes > 4 => return False
        '''
        for i in range(len(data)):
            data[i] = format(data[i], '08b')
            
        i = 0
        while i < len(data):
            cur = data[i]
            nBytes = 0
            
            for j in cur:
                if j == '1':
                    nBytes += 1
                else:
                    break
            
            if nBytes > 4 or nBytes == 1:
                return False
            
            j = i+1
            while j < nBytes + i:
                if j >= len(data):
                    return False
                if not (data[j][0] == '1' and data[j][1] == '0'):
                    return False
                j += 1
            i = j
        return True
