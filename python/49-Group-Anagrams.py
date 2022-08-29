class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = {}

        for s in strs:
            ch_freq = [0]*26

            for i in range(len(s)):
                ch_freq[ord(s[i]) - ord('a')] += 1

            ch_str = str(ch_freq)

            if lookup.get(ch_str):
                lookup[ch_str].append(s)
            else:
                lookup[ch_str] = [s]

        return lookup.values()
