from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)
        
        for word in strs:
            sort_str = ''.join(sorted(word))
            anagrams[sort_str].append(word)
        
        return list(anagrams.values())


if __name__ == "__main__":
    result = Solution()
    print(result.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(result.groupAnagrams([""]))
    print(result.groupAnagrams(["a"]))